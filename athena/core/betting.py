from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Dict


class Action(Enum):
    """Enumeration of possible betting actions in Texas Hold'em."""
    FOLD = auto()
    CHECK = auto()
    CALL = auto()
    BET = auto()
    RAISE = auto()
    ALL_IN = auto()


@dataclass(frozen=True, slots=True)
class BettingAction:
    """Represents a discrete betting action taken by a player.
    
    Attributes:
        player_id: The unique identifier of the player taking the action.
        action: The type of Action being executed.
        amount: The incremental amount of chips added to the pot in this action.
    """
    player_id: str
    action: Action
    amount: int = 0

    def __post_init__(self) -> None:
        """Validates that the action data is logically consistent."""
        if not self.player_id or not str(self.player_id).strip():
            raise ValueError("player_id is required.")
        if self.amount < 0:
            raise ValueError("Betting amount cannot be negative.")
        if self.action in (Action.FOLD, Action.CHECK) and self.amount != 0:
            raise ValueError(f"{self.action.name} action must have an amount of 0.")


@dataclass(slots=True)
class BettingEngine:
    """Manages the mechanics, mathematics, and state of betting rounds 
    in a No Limit Hold'em tournament structure.
    """
    pot: int = 0
    current_bet: int = 0
    minimum_raise: int = 0
    contributions: Dict[str, int] = field(default_factory=dict)

    def get_player_contribution(self, player_id: str) -> int:
        """Gets the total amount of chips a player has contributed during the current betting round.
        
        Args:
            player_id: The unique identifier of the player.
            
        Returns:
            The integer amount of chips contributed on this street.
        """
        return self.contributions.get(player_id, 0)

    def calculate_call_amount(self, player_id: str) -> int:
        """Calculates the exact amount of chips a player needs to add to call the current bet.
        
        Args:
            player_id: The unique identifier of the player.
            
        Returns:
            The integer amount needed to match the current bet.
        """
        return max(0, self.current_bet - self.get_player_contribution(player_id))

    def add_contribution(self, player_id: str, amount: int) -> None:
        """Adds chips from a player to the pot and tracks their contribution for the current round.
        
        Args:
            player_id: The unique identifier of the player.
            amount: The incremental amount of chips being added.
            
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError(f"Cannot add negative contribution. Got: {amount}")
        if amount > 0:
            self.contributions[player_id] = self.get_player_contribution(player_id) + amount
            self.pot += amount

    def apply_action(self, action: BettingAction) -> None:
        """Applies a betting action to the engine, validating rules and updating state.
        
        Args:
            action: The BettingAction object to process.
            
        Raises:
            ValueError: If the action violates No Limit Hold'em betting rules.
        """
        incremental = action.amount
        player_id = action.player_id
        new_total_contribution = self.get_player_contribution(player_id) + incremental

        if action.action == Action.FOLD:
            pass  # Folds do not alter the pot or bets

        elif action.action == Action.CHECK:
            if self.calculate_call_amount(player_id) > 0:
                raise ValueError("Cannot CHECK when there is a pending bet to call.")

        elif action.action == Action.CALL:
            call_amount = self.calculate_call_amount(player_id)
            if incremental != call_amount:
                raise ValueError(f"CALL amount must exactly match the pending bet. Expected {call_amount}, got {incremental}.")
            self.add_contribution(player_id, incremental)

        elif action.action == Action.BET:
            if self.current_bet > 0:
                raise ValueError("Cannot BET if a bet has already been made this round. Use RAISE.")
            if incremental < self.minimum_raise:
                raise ValueError(f"BET amount must be at least the minimum raise ({self.minimum_raise}).")
            self.add_contribution(player_id, incremental)
            self.current_bet = new_total_contribution
            self.minimum_raise = incremental  # In NLHE, the next min raise is the size of the previous bet

        elif action.action == Action.RAISE:
            if self.current_bet == 0:
                raise ValueError("Cannot RAISE if no bet has been made. Use BET.")
            if new_total_contribution < self.current_bet + self.minimum_raise:
                raise ValueError(f"RAISE must total at least {self.current_bet + self.minimum_raise}. Attempted total: {new_total_contribution}.")
            self.add_contribution(player_id, incremental)
            # Min raise increases by the difference between the new bet and the old bet
            self.minimum_raise = new_total_contribution - self.current_bet
            self.current_bet = new_total_contribution

        elif action.action == Action.ALL_IN:
            self.add_contribution(player_id, incremental)
            if new_total_contribution > self.current_bet:
                raised_amount = new_total_contribution - self.current_bet
                # Standard NLHE rule: a partial all-in raise does not necessarily reopen betting,
                # but it does establish a new current_bet. It only updates minimum_raise if it's a full raise.
                if raised_amount >= self.minimum_raise:
                    self.minimum_raise = raised_amount
                self.current_bet = new_total_contribution

    def reset_round(self, initial_minimum_raise: int = 0) -> None:
        """Resets the betting variables for a new street (preflop, flop, turn, river).
        Pot remains intact.
        
        Args:
            initial_minimum_raise: The minimum bet/raise for the new street (usually the big blind).
        """
        self.contributions.clear()
        self.current_bet = 0
        self.minimum_raise = initial_minimum_raise