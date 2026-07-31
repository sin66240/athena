from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class BlindLevel:
    """Represents a specific blind level in a tournament structure."""
    level: int
    small_blind: int
    big_blind: int
    ante: int = 0

    def __post_init__(self) -> None:
        """Validates that blind level configurations are logically sound."""
        if self.level < 1:
            raise ValueError(f"Level must be 1 or greater. Got: {self.level}")
        if self.small_blind < 0 or self.big_blind < 0 or self.ante < 0:
            raise ValueError("Blinds and ante cannot be negative.")
        if self.small_blind > self.big_blind:
            raise ValueError(
                f"Small blind ({self.small_blind}) cannot be greater than big blind ({self.big_blind})."
            )


class TournamentStage(Enum):
    """Enumeration representing the macro-phases of a Multi-Table Tournament (MTT)."""
    EARLY = auto()
    MIDDLE = auto()
    LATE = auto()
    FINAL_TABLE = auto()


@dataclass(slots=True)
class TournamentState:
    """Manages the macro-state of a poker tournament, including blinds progression,
    field size, and average stack metrics.
    """
    tournament_id: str
    buy_in: float
    players_count: int
    current_level: int
    blind_level: BlindLevel
    total_chips: int
    total_entries: int = field(default=0)
    average_stack: float = field(init=False, default=0.0)

    def __post_init__(self) -> None:
        """Validates critical tournament metrics upon initialization and calculates initial averages."""
        if not self.tournament_id or not str(self.tournament_id).strip():
            raise ValueError("tournament_id is required.")
        if self.buy_in < 0:
            raise ValueError("buy_in cannot be negative.")
        if self.players_count < 0:
            raise ValueError("players_count cannot be negative.")
        if self.total_chips < 0:
            raise ValueError("total_chips cannot be negative.")
        
        # Default total entries to players_count if not provided
        if self.total_entries < self.players_count:
            self.total_entries = self.players_count
            
        self.update_average_stack()

    def advance_level(self, next_blind_level: BlindLevel) -> None:
        """Advances the tournament to the next blind level.
        
        Args:
            next_blind_level: The new BlindLevel object to apply.
            
        Raises:
            ValueError: If the new level number is not strictly greater than the current level.
        """
        if next_blind_level.level <= self.current_level:
            raise ValueError(
                f"Next level ({next_blind_level.level}) must be greater than current level ({self.current_level})."
            )
            
        self.current_level = next_blind_level.level
        self.blind_level = next_blind_level

    def get_big_blinds(self, stack: int) -> float:
        """Calculates the depth of a given chip stack in terms of Big Blinds (BB).
        
        Args:
            stack: The amount of chips to evaluate.
            
        Returns:
            A float representing the number of big blinds the stack represents.
        """
        if self.blind_level.big_blind == 0:
            return 0.0
        return float(stack) / self.blind_level.big_blind

    def update_average_stack(self) -> None:
        """Recalculates the average stack size based on total chips and remaining players.
        Should be called whenever a player is eliminated or total chips change.
        """
        if self.players_count > 0:
            self.average_stack = float(self.total_chips) / self.players_count
        else:
            self.average_stack = 0.0

    def get_stage(self) -> TournamentStage:
        """Estimates the current macro-stage of the tournament based on field size.
        
        Returns:
            The TournamentStage enum (EARLY, MIDDLE, LATE, FINAL_TABLE).
        """
        if self.players_count <= 9:
            return TournamentStage.FINAL_TABLE
            
        if self.total_entries == 0:
            return TournamentStage.EARLY

        percentage_remaining = self.players_count / self.total_entries
        
        if percentage_remaining > 0.50:
            return TournamentStage.EARLY
        elif percentage_remaining > 0.15:
            return TournamentStage.MIDDLE
        else:
            return TournamentStage.LATE