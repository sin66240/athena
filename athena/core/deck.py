from __future__ import annotations
import random
from dataclasses import dataclass, field
from typing import List, Optional
from athena.core.card import Card, Suit, Rank


@dataclass
class Deck:
    """Represents a standard deck of 52 playing cards, managing state 
    such as shuffling, drawing, resetting, and tracking remaining cards 
    for poker simulation and training engines.
    """
    cards: List[Card] = field(default_factory=list)

    @classmethod
    def create_standard(cls) -> Deck:
        """Creates and returns a standard 52-card deck containing all 
        combinations of suits and ranks, in initial un-shuffled order.
        """
        standard_cards = [
            Card(suit, rank)
            for suit in Suit
            for rank in Rank
        ]
        return cls(cards=standard_cards)

    def shuffle(self) -> None:
        """Shuffles the remaining cards in the deck in-place 
        using a cryptographically secure or pseudo-random algorithm.
        """
        random.shuffle(self.cards)

    def draw(self) -> Optional[Card]:
        """Draws and removes the top card from the deck.
        
        Returns:
            The drawn Card object, or None if the deck is empty.
        """
        if not self.cards:
            return None
        return self.cards.pop()

    def reset(self) -> None:
        """Resets the deck back to a full standard 52-card state 
        in un-shuffled order.
        """
        self.cards = [
            Card(suit, rank)
            for suit in Suit
            for rank in Rank
        ]

    def remaining(self) -> int:
        """Returns the number of cards currently remaining in the deck."""
        return len(self.cards)