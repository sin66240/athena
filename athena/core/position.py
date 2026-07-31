from __future__ import annotations
from enum import Enum
from dataclasses import dataclass


class TableSize(Enum):
    """Enumeration representing standard poker table capacity limits."""
    SIX_MAX = 6
    NINE_MAX = 9


class Position(Enum):
    """Enumeration of standard Texas Hold'em table positions."""
    UTG = "Under The Gun"
    UTG_PLUS_1 = "Under The Gun + 1"
    MP = "Middle Position"
    LJ = "Lojack"
    HJ = "Hijack"
    CO = "Cutoff"
    BTN = "Button"
    SB = "Small Blind"
    BB = "Big Blind"


class PositionManager:
    """Calculates table position assignments and action ordering for 6-max and 9-max 
    Tournament No Limit Hold'em tables relative to the dealer button.
    """

    # Canonical order of positions relative to the Button (seat offsets 1 through N)
    # Offset 1 = SB, Offset 2 = BB, Offset N = BTN
    _POSITIONS_6MAX: list[Position] = [
        Position.SB,
        Position.BB,
        Position.LJ,
        Position.HJ,
        Position.CO,
        Position.BTN,
    ]

    _POSITIONS_9MAX: list[Position] = [
        Position.SB,
        Position.BB,
        Position.UTG,
        Position.UTG_PLUS_1,
        Position.MP,
        Position.LJ,
        Position.HJ,
        Position.CO,
        Position.BTN,
    ]

    @classmethod
    def get_positions(cls, table_size: TableSize) -> list[Position]:
        """Returns the canonical list of active positions present at a full table.

        Args:
            table_size: TableSize enum specifying table capacity (SIX_MAX or NINE_MAX).

        Returns:
            A list of Position enums ordered clockwise starting from Small Blind.
        """
        if table_size == TableSize.SIX_MAX:
            return list(cls._POSITIONS_6MAX)
        elif table_size == TableSize.NINE_MAX:
            return list(cls._POSITIONS_9MAX)
        else:
            raise ValueError(f"Unsupported table size: {table_size}")

    @classmethod
    def get_position(cls, seat: int, dealer_seat: int, table_size: TableSize) -> Position:
        """Determines the specific Position enum for a given seat number relative to the dealer seat.

        Args:
            seat: Seat number of the player (0-indexed: 0 to table_size.value - 1).
            dealer_seat: Seat number holding the dealer button (0-indexed).
            table_size: TableSize enum specifying table capacity.

        Returns:
            The Position enum for the specified seat.

        Raises:
            ValueError: If seat numbers are out of bounds for the given table size.
        """
        max_seats = table_size.value

        if not (0 <= seat < max_seats):
            raise ValueError(f"Invalid seat index {seat} for {table_size.name} (must be 0..{max_seats - 1}).")
        if not (0 <= dealer_seat < max_seats):
            raise ValueError(f"Invalid dealer seat {dealer_seat} for {table_size.name} (must be 0..{max_seats - 1}).")

        # Calculate clockwise offset from the dealer seat (0 = BTN, 1 = SB, 2 = BB, etc.)
        offset = (seat - dealer_seat) % max_seats
        positions = cls.get_positions(table_size)

        # In our position array, SB is index 0 (offset 1), BB is index 1 (offset 2), BTN is last index (offset 0)
        return positions[offset - 1]

    @classmethod
    def get_action_order(cls, dealer_seat: int, table_size: TableSize) -> list[int]:
        """Calculates the preflop action ordering (seat indices) starting first-to-act after the Big Blind.

        Args:
            dealer_seat: Seat number holding the dealer button (0-indexed).
            table_size: TableSize enum specifying table capacity.

        Returns:
            A list of seat indices representing preflop action sequence clockwise.
        """
        max_seats = table_size.value
        if not (0 <= dealer_seat < max_seats):
            raise ValueError(f"Invalid dealer seat {dealer_seat} for {table_size.name}.")

        # First to act preflop is 3 seats clockwise from dealer button (UTG or LJ)
        first_act = (dealer_seat + 3) % max_seats

        return [(first_act + i) % max_seats for i in range(max_seats)]