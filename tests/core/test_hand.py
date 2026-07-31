import pytest
from athena.core.card import Card, Suit, Rank
from athena.core.hand import HandEvaluator, HandRank


def test_evaluator_high_card() -> None:
    """Test evaluation of a High Card hand."""
    cards = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.HEARTS, Rank.JACK),
        Card(Suit.DIAMONDS, Rank.NINE),
        Card(Suit.CLUBS, Rank.SEVEN),
        Card(Suit.HEARTS, Rank.TWO)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.HIGH_CARD
    assert "High Card" in result.description


def test_evaluator_one_pair() -> None:
    """Test evaluation of a One Pair hand."""
    cards = [
        Card(Suit.SPADES, Rank.KING),
        Card(Suit.HEARTS, Rank.KING),
        Card(Suit.DIAMONDS, Rank.TEN),
        Card(Suit.CLUBS, Rank.SEVEN),
        Card(Suit.HEARTS, Rank.TWO)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.ONE_PAIR
    assert "One Pair, KINGS" in result.description


def test_evaluator_two_pair() -> None:
    """Test evaluation of a Two Pair hand."""
    cards = [
        Card(Suit.SPADES, Rank.QUEEN),
        Card(Suit.HEARTS, Rank.QUEEN),
        Card(Suit.DIAMONDS, Rank.JACK),
        Card(Suit.CLUBS, Rank.JACK),
        Card(Suit.HEARTS, Rank.FOUR)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.TWO_PAIR
    assert "Two Pair" in result.description


def test_evaluator_three_of_a_kind() -> None:
    """Test evaluation of a Three of a Kind hand."""
    cards = [
        Card(Suit.SPADES, Rank.JACK),
        Card(Suit.HEARTS, Rank.JACK),
        Card(Suit.DIAMONDS, Rank.JACK),
        Card(Suit.CLUBS, Rank.EIGHT),
        Card(Suit.HEARTS, Rank.THREE)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.THREE_OF_KIND
    assert "Three of a Kind, JACKS" in result.description


def test_evaluator_straight() -> None:
    """Test evaluation of a standard Straight hand (Ace high)."""
    cards = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.HEARTS, Rank.KING),
        Card(Suit.DIAMONDS, Rank.QUEEN),
        Card(Suit.CLUBS, Rank.JACK),
        Card(Suit.HEARTS, Rank.TEN)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.STRAIGHT
    assert "Straight, ACE High" in result.description


def test_evaluator_ace_low_straight() -> None:
    """Test evaluation of an Ace-low wheel straight (A-2-3-4-5)."""
    cards = [
        Card(Suit.SPADES, Rank.ACE),
        Card(Suit.HEARTS, Rank.TWO),
        Card(Suit.DIAMONDS, Rank.THREE),
        Card(Suit.CLUBS, Rank.FOUR),
        Card(Suit.HEARTS, Rank.FIVE)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.STRAIGHT
    assert "Straight, FIVE High" in result.description


def test_evaluator_flush() -> None:
    """Test evaluation of a Flush hand."""
    cards = [
        Card(Suit.HEARTS, Rank.ACE),
        Card(Suit.HEARTS, Rank.TEN),
        Card(Suit.HEARTS, Rank.SEVEN),
        Card(Suit.HEARTS, Rank.FOUR),
        Card(Suit.HEARTS, Rank.TWO)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.FLUSH
    assert "Flush, ACE High" in result.description


def test_evaluator_full_house() -> None:
    """Test evaluation of a Full House hand."""
    cards = [
        Card(Suit.SPADES, Rank.TEN),
        Card(Suit.HEARTS, Rank.TEN),
        Card(Suit.DIAMONDS, Rank.TEN),
        Card(Suit.CLUBS, Rank.FOUR),
        Card(Suit.HEARTS, Rank.FOUR)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.FULL_HOUSE
    assert "Full House, TENS" in result.description


def test_evaluator_four_of_a_kind() -> None:
    """Test evaluation of a Four of a Kind hand."""
    cards = [
        Card(Suit.SPADES, Rank.NINE),
        Card(Suit.HEARTS, Rank.NINE),
        Card(Suit.DIAMONDS, Rank.NINE),
        Card(Suit.CLUBS, Rank.NINE),
        Card(Suit.HEARTS, Rank.KING)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.FOUR_OF_KIND
    assert "Four of a Kind, NINES" in result.description


def test_evaluator_straight_flush() -> None:
    """Test evaluation of a Straight Flush hand."""
    cards = [
        Card(Suit.SPADES, Rank.JACK),
        Card(Suit.SPADES, Rank.TEN),
        Card(Suit.SPADES, Rank.NINE),
        Card(Suit.SPADES, Rank.EIGHT),
        Card(Suit.SPADES, Rank.SEVEN)
    ]
    result = HandEvaluator.evaluate(cards)
    assert result.hand_rank == HandRank.STRAIGHT_FLUSH
    assert "Straight Flush" in result.description


def test_evaluator_invalid_card_count() -> None:
    """Test that passing incorrect number of cards raises ValueError."""
    # Too few cards
    with pytest.raises(ValueError):
        HandEvaluator.evaluate([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING)
        ])

    # Too many cards
    with pytest.raises(ValueError):
        HandEvaluator.evaluate([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.KING),
            Card(Suit.HEARTS, Rank.QUEEN),
            Card(Suit.HEARTS, Rank.JACK),
            Card(Suit.HEARTS, Rank.TEN),
            Card(Suit.HEARTS, Rank.NINE)
        ])


def test_evaluator_duplicate_cards() -> None:
    """Test that passing duplicate cards raises ValueError."""
    with pytest.raises(ValueError):
        HandEvaluator.evaluate([
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.HEARTS, Rank.ACE),
            Card(Suit.DIAMONDS, Rank.KING),
            Card(Suit.CLUBS, Rank.QUEEN),
            Card(Suit.SPADES, Rank.JACK)
        ])