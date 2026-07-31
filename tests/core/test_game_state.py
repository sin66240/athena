import pytest
from athena.core.player import Player, PlayerStatus
from athena.core.game_state import GameState, Street


def test_create_game_state() -> None:
    """Test that a valid game state can be created with correct initial attributes."""
    gs = GameState(
        tournament_id="MTT-001",
        blinds=(10, 20),
        current_level=1
    )
    
    assert gs.tournament_id == "MTT-001"
    assert gs.blinds == (10, 20)
    assert gs.current_level == 1
    assert gs.players == []
    assert gs.pot == 0
    assert gs.street == Street.PREFLOP


def test_game_state_validation() -> None:
    """Test validation rules during GameState initialization."""
    # Test invalid tournament ID
    with pytest.raises(ValueError, match="tournament_id is required"):
        GameState(tournament_id="", blinds=(10, 20), current_level=1)

    # Test invalid level
    with pytest.raises(ValueError, match="current_level must be >= 1"):
        GameState(tournament_id="t1", blinds=(10, 20), current_level=0)

    # Test negative pot
    with pytest.raises(ValueError, match="pot cannot be negative"):
        GameState(tournament_id="t1", blinds=(10, 20), current_level=1, pot=-50)

    # Test invalid blinds format or negative values
    with pytest.raises(ValueError, match="blinds must be a tuple"):
        GameState(tournament_id="t1", blinds=(-10, 20), current_level=1)


def test_add_player() -> None:
    """Test adding players to the game state and duplicate ID prevention."""
    gs = GameState(tournament_id="t1", blinds=(10, 20), current_level=1)
    player1 = Player(player_id="p1", name="Alice", stack=1000)
    
    gs.add_player(player1)
    assert len(gs.players) == 1
    assert gs.players[0].name == "Alice"

    # Test adding duplicate player ID
    player2 = Player(player_id="p1", name="Alice Duplicate", stack=500)
    with pytest.raises(ValueError, match="already in the game"):
        gs.add_player(player2)


def test_remove_player() -> None:
    """Test removing players from the game state."""
    gs = GameState(tournament_id="t1", blinds=(10, 20), current_level=1)
    gs.add_player(Player(player_id="p1", name="Alice", stack=1000))
    gs.add_player(Player(player_id="p2", name="Bob", stack=1000))
    
    gs.remove_player("p1")
    assert len(gs.players) == 1
    assert gs.players[0].player_id == "p2"

    # Test removing non-existent player
    with pytest.raises(ValueError, match="not found in the game"):
        gs.remove_player("p99")


def test_pot_update() -> None:
    """Test adding chips to the main pot."""
    gs = GameState(tournament_id="t1", blinds=(10, 20), current_level=1)
    
    gs.update_pot(150)
    assert gs.pot == 150
    
    gs.update_pot(300)
    assert gs.pot == 450

    # Test adding negative amount
    with pytest.raises(ValueError, match="negative amount"):
        gs.update_pot(-50)


def test_street_transition() -> None:
    """Test the sequential progression of betting streets."""
    gs = GameState(tournament_id="t1", blinds=(10, 20), current_level=1)
    
    assert gs.street == Street.PREFLOP
    gs.advance_street()
    assert gs.street == Street.FLOP
    gs.advance_street()
    assert gs.street == Street.TURN
    gs.advance_street()
    assert gs.street == Street.RIVER
    gs.advance_street()
    assert gs.street == Street.SHOWDOWN

    # Test advancing past SHOWDOWN
    with pytest.raises(ValueError, match="Cannot advance street past SHOWDOWN"):
        gs.advance_street()


def test_active_player_filtering() -> None:
    """Test that get_active_players correctly filters out folded players."""
    gs = GameState(tournament_id="t1", blinds=(10, 20), current_level=1)
    
    player1 = Player(player_id="p1", name="Alice", stack=1000)
    player2 = Player(player_id="p2", name="Bob", stack=1000)
    player3 = Player(player_id="p3", name="Charlie", stack=0, status=PlayerStatus.ALL_IN)
    
    gs.add_player(player1)
    gs.add_player(player2)
    gs.add_player(player3)
    
    # Alice folds
    player1.fold()
    
    active_players = gs.get_active_players()
    
    assert len(active_players) == 2
    active_ids = [p.player_id for p in active_players]
    assert "p2" in active_ids  # Bob is ACTIVE
    assert "p3" in active_ids  # Charlie is ALL_IN (which counts as participating)
    assert "p1" not in active_ids  # Alice is FOLDED