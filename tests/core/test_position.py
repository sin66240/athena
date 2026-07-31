import pytest
from athena.core.position import Position, PositionManager, TableSize


def test_six_max_positions() -> None:
    """Test that a 6-max table returns exactly 6 positions in correct order."""
    positions = PositionManager.get_positions(TableSize.SIX_MAX)
    
    assert len(positions) == 6
    assert positions == [
        Position.SB,
        Position.BB,
        Position.LJ,
        Position.HJ,
        Position.CO,
        Position.BTN,
    ]


def test_nine_max_positions() -> None:
    """Test that a 9-max table returns exactly 9 positions in correct order."""
    positions = PositionManager.get_positions(TableSize.NINE_MAX)
    
    assert len(positions) == 9
    assert positions == [
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


def test_dealer_position_mapping() -> None:
    """Test position mapping for button, small blind, and cutoff relative to dealer seat."""
    # 6-max table, Button is at seat 0
    btn_pos = PositionManager.get_position(seat=0, dealer_seat=0, table_size=TableSize.SIX_MAX)
    assert btn_pos == Position.BTN

    # Cutoff is 1 seat before Button (seat 5)
    co_pos = PositionManager.get_position(seat=5, dealer_seat=0, table_size=TableSize.SIX_MAX)
    assert co_pos == Position.CO

    # Test invalid seat index
    with pytest.raises(ValueError, match="Invalid seat index"):
        PositionManager.get_position(seat=6, dealer_seat=0, table_size=TableSize.SIX_MAX)


def test_small_blind_and_big_blind_assignment() -> None:
    """Test that SB and BB are correctly assigned immediately clockwise from dealer."""
    # 9-max table, Dealer is at seat 4
    sb_pos = PositionManager.get_position(seat=5, dealer_seat=4, table_size=TableSize.NINE_MAX)
    bb_pos = PositionManager.get_position(seat=6, dealer_seat=4, table_size=TableSize.NINE_MAX)

    assert sb_pos == Position.SB
    assert bb_pos == Position.BB

    # Test wrap-around across seat boundary: Dealer is at seat 8 (last seat)
    sb_wrap = PositionManager.get_position(seat=0, dealer_seat=8, table_size=TableSize.NINE_MAX)
    bb_wrap = PositionManager.get_position(seat=1, dealer_seat=8, table_size=TableSize.NINE_MAX)

    assert sb_wrap == Position.SB
    assert bb_wrap == Position.BB


def test_action_order_generation() -> None:
    """Test preflop action order generation starting after BB."""
    # 6-max table, Dealer is at seat 0
    # SB is seat 1, BB is seat 2 -> First to act (LJ) is seat 3
    order_6max = PositionManager.get_action_order(dealer_seat=0, table_size=TableSize.SIX_MAX)
    assert order_6max == [3, 4, 5, 0, 1, 2]

    # 9-max table with wrap-around, Dealer is at seat 7
    # SB is seat 8, BB is seat 0 -> First to act (UTG) is seat 1
    order_9max = PositionManager.get_action_order(dealer_seat=7, table_size=TableSize.NINE_MAX)
    assert order_9max == [1, 2, 3, 4, 5, 6, 7, 8, 0]