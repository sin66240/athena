from __future__ import annotations
from enum import IntEnum
from dataclasses import dataclass, field
from athena.core.player import Player, PlayerStatus


class Street(IntEnum):
    """Enumeration representing the betting rounds (streets) in a poker hand,
    ordered sequentially from preflop to showdown.
    """
    PREFLOP = 1
    FLOP = 2
    TURN = 3
    RIVER = 4
    SHOWDOWN = 5


@dataclass(slots=True)
class GameState:
    """Represents the complete state of a poker tournament at a specific moment,
    managing players, pot, blinds, and the current phase of the hand.
    """
    tournament_id: str
    blinds: tuple[int, int]  # (Small Blind, Big Blind)
    current_level: int
    players: list[Player] = field(default_factory=list)
    dealer_position: int = 0
    current_player: int = 0
    pot: int = 0
    street: Street = Street.PREFLOP

    def __post_init__(self) -> None:
        """Validates critical game state attributes upon initialization."""
        if not self.tournament_id or not str(self.tournament_id).strip():
            raise ValueError("tournament_id is required and cannot be empty.")
        if self.current_level < 1:
            raise ValueError(f"current_level must be >= 1. Got: {self.current_level}")
        if self.pot < 0:
            raise ValueError(f"pot cannot be negative. Got: {self.pot}")
        if len(self.blinds) != 2 or self.blinds[0] < 0 or self.blinds[1] < 0:
            raise ValueError(f"blinds must be a tuple of two non-negative integers. Got: {self.blinds}")

    def add_player(self, player: Player) -> None:
        """Adds a new player to the game state.
        
        Args:
            player: The Player object to add.
            
        Raises:
            ValueError: If a player with the same player_id already exists.
        """
        if any(p.player_id == player.player_id for p in self.players):
            raise ValueError(f"Player with ID {player.player_id} is already in the game.")
        
        self.players.append(player)

    def remove_player(self, player_id: str) -> None:
        """Removes a player from the game state by their player_id.
        
        Args:
            player_id: The unique identifier of the player to remove.
            
        Raises:
            ValueError: If the player_id is not found in the current players list.
        """
        original_count = len(self.players)
        self.players = [p for p in self.players if p.player_id != player_id]
        
        if len(self.players) == original_count:
            raise ValueError(f"Player with ID {player_id} not found in the game.")
            
        # Optional safeguard: ensure position indices do not point out of bounds 
        # after a player is removed. Complex pointer reassignment is deferred to game logic.
        self.dealer_position = min(self.dealer_position, max(0, len(self.players) - 1))
        self.current_player = min(self.current_player, max(0, len(self.players) - 1))

    def advance_street(self) -> None:
        """Advances the game state to the next street (e.g., PREFLOP -> FLOP).
        
        Raises:
            ValueError: If the current street is already SHOWDOWN.
        """
        if self.street == Street.SHOWDOWN:
            raise ValueError("Cannot advance street past SHOWDOWN.")
            
        self.street = Street(self.street.value + 1)

    def update_pot(self, amount: int) -> None:
        """Adds chips to the main pot.
        
        Args:
            amount: The positive integer amount of chips to add.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError(f"Cannot add a negative amount to the pot. Got: {amount}")
            
        self.pot += amount

    def get_active_players(self) -> list[Player]:
        """Retrieves a list of all players currently active in the hand.
        An active player is one who has not folded (can be ACTIVE or ALL_IN).
        
        Returns:
            A list of Player objects actively participating in the hand.
        """
        return [p for p in self.players if p.status != PlayerStatus.FOLDED]