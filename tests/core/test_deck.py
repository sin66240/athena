import pytest
from athena.core.deck import Deck
from athena.core.card import Card


def test_standard_deck_creation() -> None:
    """Test that a standard deck is created with exactly 52 cards."""
    deck = Deck.create_standard()
    assert deck.remaining() == 52


def test_all_cards_unique() -> None:
    """Test that all 52 cards in a newly created standard deck are unique."""
    deck = Deck.create_standard()
    unique_cards = set(deck.cards)
    assert len(unique_cards) == 52


def test_shuffle_changes_order() -> None:
    """Test that shuffling the deck changes the card arrangement (probabilistic)."""
    deck1 = Deck.create_standard()
    deck2 = Deck.create_standard()
    
    # Before shuffle, both decks should be identical
    assert deck1.cards == deck2.cards
    
    # Shuffle deck2
    deck2.shuffle()
    
    # After shuffle, they should (virtually always) be in a different order
    assert deck1.cards != deck2.cards
    assert deck2.remaining() == 52


def test_draw_removes_card() -> None:
    """Test that drawing a card reduces the deck count by 1 and returns a Card."""
    deck = Deck.create_standard()
    initial_count = deck.remaining()
    
    drawn_card = deck.draw()
    
    assert isinstance(drawn_card, Card)
    assert deck.remaining() == initial_count - 1


def test_remaining_count_correct() -> None:
    """Test that remaining() accurately tracks cards drawn sequentially."""
    deck = Deck.create_standard()
    
    for i in range(52):
        assert deck.remaining() == 52 - i
        deck.draw()
        
    assert deck.remaining() == 0
    assert deck.draw() is None


def test_reset_restores_deck() -> None:
    """Test that resetting the deck restores it to a full 52-card un-shuffled state."""
    deck = Deck.create_standard()
    deck.shuffle()
    deck.draw()
    deck.draw()
    
    assert deck.remaining() == 50
    
    deck.reset()
    
    assert deck.remaining() == 52
    fresh_deck = Deck.create_standard()
    assert deck.cards == fresh_deck.cards