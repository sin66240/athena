from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Optional, Sequence
from athena.core.card import Card


class PlayerStatus(Enum):
    """Enumeration representing the current active state of a player in a hand."""
    ACTIVE = auto()
    FOLDED = auto()
    ALL_IN = auto()


@dataclass(slots=True)
class Player:
    """Represents a poker player in a tournament environment, managing 
    their chips, position, private cards, and current hand status.
    """
    player_id: str
    name: str
    stack: int
    position: Optional[str] = None
    hole_cards: tuple[Card, ...] = field(default_factory=tuple)
    status: PlayerStatus = PlayerStatus.ACTIVE

    def __post_init__(self) -> None:
        """Validates critical player attributes upon initialization."""
        if not self.player_id or not str(self.player_id).strip():
            raise ValueError("player_id is required and cannot be empty.")
        if self.stack < 0:
            raise ValueError(f"Player stack cannot be negative. Got: {self.stack}")

    def add_chips(self, amount: int) -> None:
        """Adds a specified amount of chips to the player's stack.
        
        Args:
            amount: The positive integer amount of chips to add.
            
        Raises:
            ValueError: If the amount to add is negative.
        """
        if amount < 0:
            raise ValueError(f"Cannot add a negative amount of chips. Got: {amount}")
        self.stack += amount

    def remove_chips(self, amount: int) -> None:
        """Removes a specified amount of chips from the player's stack.
        Automatically updates status to ALL_IN if the stack reaches exactly zero.
        
        Args:
            amount: The positive integer amount of chips to remove.
            
        Raises:
            ValueError: If the amount is negative or exceeds the current stack.
        """
        if amount < 0:
            raise ValueError(f"Cannot remove a negative amount of chips. Got: {amount}")
        if amount > self.stack:
            raise ValueError(f"Insufficient chips. Cannot remove {amount} from stack of {self.stack}.")
            
        self.stack -= amount
        
        if self.stack == 0:
            self.status = PlayerStatus.ALL_IN

    def receive_cards(self, cards: Sequence[Card]) -> None:
        """Assigns exactly two private hole cards to the player.
        
        Args:
            cards: A sequence (list or tuple) of exactly two Card objects.
            
        Raises:
            ValueError: If the number of cards provided is not exactly two.
        """
        if len(cards) != 2:
            raise ValueError(f"Texas Hold'em requires exactly 2 hole cards. Got: {len(cards)}")
        self.hole_cards = tuple(cards)

    def fold(self) -> None:
        """Marks the player's status as folded and discards their hole cards."""
        self.status = PlayerStatus.FOLDED
        self.hole_cards = ()

    def reset_hand(self) -> None:
        """Resets the player's state for a new hand.
        Clears hole cards and sets status back to ACTIVE (or ALL_IN if stack is 0).
        """
        self.hole_cards = ()
        if self.stack > 0:
            self.status = PlayerStatus.ACTIVE
        else:
            self.status = PlayerStatus.ALL_IN