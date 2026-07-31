import pytest
from athena.core.tournament import BlindLevel, TournamentStage, TournamentState


def test_create_blind_level() -> None:
    """Test valid creation of a BlindLevel and validation rules."""
    level1 = BlindLevel(level=1, small_blind=50, big_blind=100, ante=10)
    assert level1.level == 1
    assert level1.small_blind == 50
    assert level1.big_blind == 100
    assert level1.ante == 10

    # Test invalid level number
    with pytest.raises(ValueError, match="Level must be 1 or greater"):
        BlindLevel(level=0, small_blind=50, big_blind=100)

    # Test negative blinds
    with pytest.raises(ValueError, match="Blinds and ante cannot be negative"):
        BlindLevel(level=1, small_blind=-50, big_blind=100)

    # Test small blind greater than big blind
    with pytest.raises(ValueError, match="Small blind .* cannot be greater than big blind"):
        BlindLevel(level=1, small_blind=200, big_blind=100)


def test_create_tournament_state() -> None:
    """Test creation of TournamentState and initial validation."""
    blind_level = BlindLevel(level=1, small_blind=25, big_blind=50)
    state = TournamentState(
        tournament_id="MTT-500",
        buy_in=100.0,
        players_count=100,
        current_level=1,
        blind_level=blind_level,
        total_chips=1000000,
        total_entries=100
    )

    assert state.tournament_id == "MTT-500"
    assert state.buy_in == 100.0
    assert state.players_count == 100
    assert state.average_stack == 10000.0

    # Test invalid tournament ID
    with pytest.raises(ValueError, match="tournament_id is required"):
        TournamentState(
            tournament_id="",
            buy_in=100.0,
            players_count=100,
            current_level=1,
            blind_level=blind_level,
            total_chips=1000000
        )


def test_advance_blind_level() -> None:
    """Test advancing the tournament to the next blind level."""
    level1 = BlindLevel(level=1, small_blind=25, big_blind=50)
    level2 = BlindLevel(level=2, small_blind=50, big_blind=100, ante=10)

    state = TournamentState(
        tournament_id="MTT-1",
        buy_in=50.0,
        players_count=50,
        current_level=1,
        blind_level=level1,
        total_chips=500000
    )

    state.advance_level(level2)
    assert state.current_level == 2
    assert state.blind_level == level2

    # Test advancing to a level that is not higher than the current level
    with pytest.raises(ValueError, match="must be greater than current level"):
        state.advance_level(level1)


def test_calculate_stack_in_bb() -> None:
    """Test converting a chip stack count into Big Blinds (BB)."""
    blind_level = BlindLevel(level=3, small_blind=100, big_blind=200, ante=25)
    state = TournamentState(
        tournament_id="MTT-1",
        buy_in=10.0,
        players_count=20,
        current_level=3,
        blind_level=blind_level,
        total_chips=200000
    )

    assert state.get_big_blinds(stack=5000) == 25.0
    assert state.get_big_blinds(stack=100) == 0.5
    assert state.get_big_blinds(stack=0) == 0.0


def test_update_average_stack() -> None:
    """Test updating the average stack as players are eliminated."""
    blind_level = BlindLevel(level=1, small_blind=10, big_blind=20)
    state = TournamentState(
        tournament_id="MTT-1",
        buy_in=100.0,
        players_count=100,
        current_level=1,
        blind_level=blind_level,
        total_chips=1000000
    )

    assert state.average_stack == 10000.0

    # Simulate player eliminations
    state.players_count = 50
    state.update_average_stack()
    assert state.average_stack == 20000.0

    # Test zero players remaining
    state.players_count = 0
    state.update_average_stack()
    assert state.average_stack == 0.0


def test_detect_tournament_stage() -> None:
    """Test detecting macro tournament stage based on remaining player count."""
    blind_level = BlindLevel(level=1, small_blind=10, big_blind=20)

    # Early Stage: > 50% remaining (e.g., 80/100)
    early_state = TournamentState(
        tournament_id="MTT-1",
        buy_in=100.0,
        players_count=80,
        current_level=1,
        blind_level=blind_level,
        total_chips=800000,
        total_entries=100
    )
    assert early_state.get_stage() == TournamentStage.EARLY

    # Middle Stage: > 15% and <= 50% remaining (e.g., 30/100)
    mid_state = TournamentState(
        tournament_id="MTT-1",
        buy_in=100.0,
        players_count=30,
        current_level=5,
        blind_level=blind_level,
        total_chips=800000,
        total_entries=100
    )
    assert mid_state.get_stage() == TournamentStage.MIDDLE

    # Late Stage: <= 15% remaining but > 9 players (e.g., 12/100)
    late_state = TournamentState(
        tournament_id="MTT-1",
        buy_in=100.0,
        players_count=12,
        current_level=10,
        blind_level=blind_level,
        total_chips=800000,
        total_entries=100
    )
    assert late_state.get_stage() == TournamentStage.LATE

    # Final Table Stage: <= 9 players remaining
    ft_state = TournamentState(
        tournament_id="MTT-1",
        buy_in=100.0,
        players_count=9,
        current_level=15,
        blind_level=blind_level,
        total_chips=800000,
        total_entries=100
    )
    assert ft_state.get_stage() == TournamentStage.FINAL_TABLE