from enum import IntEnum, auto
from dataclasses import dataclass


class Suit(IntEnum):
    """Enumeration representing the four suits in a standard deck of cards."""
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


class Rank(IntEnum):
    """Enumeration representing the ranks in a standard deck of cards, ordered by face value."""
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


@dataclass(frozen=True, slots=True)
class Card:
    """Represents an immutable playing card with a suit and rank, 
    designed for use in poker tournament engines.
    """
    suit: Suit
    rank: Rank

    def __post_init__(self) -> None:
        """Validates that the provided suit and rank are valid instances of their respective enums."""
        if not isinstance(self.suit, Suit):
            raise TypeError(f"Invalid suit type: {type(self.suit)}. Must be an instance of Suit.")
        if not isinstance(self.rank, Rank):
            raise TypeError(f"Invalid rank type: {type(self.rank)}. Must be an instance of Rank.")

    def __str__(self) -> str:
        """Returns standard poker notation for the card (e.g., 'AH' for Ace of Hearts)."""
        rank_symbols = {
            Rank.TWO: "2",
            Rank.THREE: "3",
            Rank.FOUR: "4",
            Rank.FIVE: "5",
            Rank.SIX: "6",
            Rank.SEVEN: "7",
            Rank.EIGHT: "8",
            Rank.NINE: "9",
            Rank.TEN: "T",
            Rank.JACK: "J",
            Rank.QUEEN: "Q",
            Rank.KING: "K",
            Rank.ACE: "A"
        }
        
        suit_symbols = {
            Suit.CLUBS: "c",
            Suit.DIAMONDS: "d",
            Suit.HEARTS: "h",
            Suit.SPADES: "s"
        }
        
        return f"{rank_symbols[self.rank]}{suit_symbols[self.suit]}"

    def __repr__(self) -> str:
        """Returns detailed unambiguous string representation for debugging."""
        return f"Card(Suit.{self.suit.name}, Rank.{self.rank.name})"