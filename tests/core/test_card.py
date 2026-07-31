import pytest
from athena.core.card import Card, Suit, Rank


def test_create_valid_card() -> None:
    """Test that a valid card can be created with correct attributes."""
    card = Card(Suit.HEARTS, Rank.ACE)
    assert card.suit == Suit.HEARTS
    assert card.rank == Rank.ACE


def test_suit_validation() -> None:
    """Test that providing an invalid suit raises a TypeError."""
    with pytest.raises(TypeError):
        # Passing an invalid type instead of Suit enum
        Card("HEARTS", Rank.ACE)  # type: ignore


def test_rank_validation() -> None:
    """Test that providing an invalid rank raises a TypeError."""
    with pytest.raises(TypeError):
        # Passing an invalid type instead of Rank enum
        Card(Suit.HEARTS, 14)  # type: ignore


def test_string_representation() -> None:
    """Test standard poker notation string representation for various cards."""
    card_ah = Card(Suit.HEARTS, Rank.ACE)
    card_tc = Card(Suit.CLUBS, Rank.TEN)
    card_2s = Card(Suit.SPADES, Rank.TWO)
    
    assert str(card_ah) == "Ah"
    assert str(card_tc) == "Tc"
    assert str(card_2s) == "2s"


def test_equality_comparison() -> None:
    """Test that cards with the same suit and rank are equal, and support immutability."""
    card1 = Card(Suit.DIAMONDS, Rank.KING)
    card2 = Card(Suit.DIAMONDS, Rank.KING)
    card3 = Card(Suit.HEARTS, Rank.KING)
    
    assert card1 == card2
    assert card1 != card3
    assert hash(card1) == hash(card2)


def test_immutability() -> None:
    """Test that the Card dataclass is frozen and cannot be modified after creation."""
    card = Card(Suit.SPADES, Rank.QUEEN)
    with pytest.raises(AttributeError):
        card.rank = Rank.JACK  # type: ignore


def test_invalid_input_handling() -> None:
    """Test that passing None or random objects raises appropriate exceptions."""
    with pytest.raises(TypeError):
        Card(None, Rank.ACE)  # type: ignore

    with pytest.raises(TypeError):
        Card(Suit.CLUBS, None)  # type: ignore