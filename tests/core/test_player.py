import pytest
from athena.core.player import Player, PlayerStatus
from athena.core.card import Card, Suit, Rank


def test_create_player() -> None:
    """Test that a valid player can be created with correct initial attributes."""
    player = Player(player_id="p1", name="Alice", stack=1500, position="BTN")
    
    assert player.player_id == "p1"
    assert player.name == "Alice"
    assert player.stack == 1500
    assert player.position == "BTN"
    assert player.hole_cards == ()
    assert player.status == PlayerStatus.ACTIVE


def test_player_validation() -> None:
    """Test validation rules for player creation."""
    # Test negative stack
    with pytest.raises(ValueError, match="stack cannot be negative"):
        Player(player_id="p2", name="Bob", stack=-500)
        
    # Test empty player_id
    with pytest.raises(ValueError, match="player_id is required"):
        Player(player_id="", name="Charlie", stack=1000)


def test_add_chips() -> None:
    """Test adding chips to a player's stack."""
    player = Player(player_id="p1", name="Alice", stack=1000)
    
    player.add_chips(500)
    assert player.stack == 1500
    
    # Test adding negative chips
    with pytest.raises(ValueError, match="negative amount"):
        player.add_chips(-100)


def test_remove_chips() -> None:
    """Test removing chips from a player's stack and handling all-in status."""
    player = Player(player_id="p1", name="Alice", stack=1000)
    
    # Normal removal
    player.remove_chips(300)
    assert player.stack == 700
    assert player.status == PlayerStatus.ACTIVE
    
    # Negative amount removal
    with pytest.raises(ValueError, match="negative amount"):
        player.remove_chips(-50)
        
    # Removing more than stack
    with pytest.raises(ValueError, match="Insufficient chips"):
        player.remove_chips(1000)
        
    # Exact stack removal (going all-in)
    player.remove_chips(700)
    assert player.stack == 0
    assert player.status == PlayerStatus.ALL_IN


def test_receive_cards() -> None:
    """Test assigning hole cards to a player."""
    player = Player(player_id="p1", name="Alice", stack=1000)
    cards = [Card(Suit.HEARTS, Rank.ACE), Card(Suit.SPADES, Rank.KING)]
    
    player.receive_cards(cards)
    assert len(player.hole_cards) == 2
    assert player.hole_cards[0].rank == Rank.ACE
    
    # Test incorrect number of cards
    with pytest.raises(ValueError, match="exactly 2 hole cards"):
        player.receive_cards([Card(Suit.HEARTS, Rank.ACE)])


def test_fold_status() -> None:
    """Test folding a hand updates status and clears hole cards."""
    player = Player(player_id="p1", name="Alice", stack=1000)
    cards = [Card(Suit.HEARTS, Rank.ACE), Card(Suit.SPADES, Rank.KING)]
    player.receive_cards(cards)
    
    player.fold()
    assert player.status == PlayerStatus.FOLDED
    assert player.hole_cards == ()


def test_reset_hand() -> None:
    """Test resetting a player's hand restores status correctly based on stack."""
    # Active player reset
    player1 = Player(player_id="p1", name="Alice", stack=1000)
    player1.fold()
    player1.reset_hand()
    assert player1.status == PlayerStatus.ACTIVE
    assert player1.hole_cards == ()
    
    # All-in player reset
    player2 = Player(player_id="p2", name="Bob", stack=0, status=PlayerStatus.FOLDED)
    player2.reset_hand()
    assert player2.status == PlayerStatus.ALL_IN
    assert player2.hole_cards == ()