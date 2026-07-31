from __future__ import annotations
from enum import IntEnum, auto
from dataclasses import dataclass
from typing import List, Tuple, Optional
from athena.core.card import Card, Suit, Rank


class HandRank(IntEnum):
    """Enumeration representing standard poker hand classifications, 
    ordered from lowest (HIGH_CARD) to highest (STRAIGHT_FLUSH).
    """
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_KIND = 8
    STRAIGHT_FLUSH = 9


@dataclass(frozen=True, slots=True)
class HandEvaluationResult:
    """Represents the evaluated result of a 5-card poker hand, 
    providing both the hand category and a comparable numeric score 
    along with an explainable description.
    """
    hand_rank: HandRank
    score: int
    description: str


class HandEvaluator:
    """Evaluates a 5-card Texas Hold'em poker hand, determining 
    its hand rank, comparative score, and explainable details.
    """

    @staticmethod
    def evaluate(cards: List[Card]) -> HandEvaluationResult:
        """Evaluates exactly 5 cards and returns their HandEvaluationResult.
        
        Args:
            cards: A list containing exactly 5 Card objects.
            
        Raises:
            ValueError: If the input does not contain exactly 5 unique cards.
        """
        if len(cards) != 5:
            raise ValueError(f"Hand evaluation requires exactly 5 cards, got {len(cards)}.")
        
        if len(set(cards)) != 5:
            raise ValueError("Hand evaluation requires 5 unique cards (duplicate cards detected).")

        # Sort cards descending by rank value
        sorted_cards = sorted(cards, key=lambda c: c.rank.value, reverse=True)
        ranks = [c.rank.value for c in sorted_cards]
        suits = [c.suit for c in sorted_cards]

        is_flush = len(set(suits)) == 1
        
        # Check straight (handling regular and A-5 low wheel straight)
        straight_high = HandEvaluator._check_straight(ranks)
        is_straight = straight_high is not None

        # Count frequencies of each rank
        rank_counts: dict[int, int] = {}
        for r in ranks:
            rank_counts[r] = rank_counts.get(r, 0) + 1

        # Sort by frequency descending, then by rank value descending
        # Example: [(rank, count), ...]
        sorted_counts = sorted(rank_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)

        # Determine Hand Rank and construct score tuple for tie-breaking
        # Score format: Tuple of integers where position signifies precedence
        if is_straight and is_flush:
            hand_rank = HandRank.STRAIGHT_FLUSH
            # Tie breaker: high card of the straight
            score_tuple = (hand_rank.value, straight_high)
            desc = f"Straight Flush, {Rank(straight_high).name.upper()} High"
        elif sorted_counts[0][1] == 4:
            hand_rank = HandRank.FOUR_OF_KIND
            quad_rank = sorted_counts[0][0]
            kicker = sorted_counts[1][0]
            score_tuple = (hand_rank.value, quad_rank, kicker)
            desc = f"Four of a Kind, {Rank(quad_rank).name.upper()}S with {Rank(kicker).name.upper()} kicker"
        elif sorted_counts[0][1] == 3 and sorted_counts[1][1] == 2:
            hand_rank = HandRank.FULL_HOUSE
            trips_rank = sorted_counts[0][0]
            pair_rank = sorted_counts[1][0]
            score_tuple = (hand_rank.value, trips_rank, pair_rank)
            desc = f"Full House, {Rank(trips_rank).name.upper()}S full of {Rank(pair_rank).name.upper()}S"
        elif is_flush:
            hand_rank = HandRank.FLUSH
            score_tuple = (hand_rank.value, tuple(ranks))
            desc = f"Flush, {sorted_cards[0].rank.name.upper()} High"
        elif is_straight:
            hand_rank = HandRank.STRAIGHT
            score_tuple = (hand_rank.value, straight_high)
            desc = f"Straight, {Rank(straight_high).name.upper()} High"
        elif sorted_counts[0][1] == 3:
            hand_rank = HandRank.THREE_OF_KIND
            trips_rank = sorted_counts[0][0]
            kickers = tuple(r for r, count in sorted_counts[1:])
            score_tuple = (hand_rank.value, trips_rank, kickers)
            desc = f"Three of a Kind, {Rank(trips_rank).name.upper()}S"
        elif sorted_counts[0][1] == 2 and sorted_counts[1][1] == 2:
            hand_rank = HandRank.TWO_PAIR
            high_pair = sorted_counts[0][0]
            low_pair = sorted_counts[1][0]
            kicker = sorted_counts[2][0]
            score_tuple = (hand_rank.value, high_pair, low_pair, kicker)
            desc = f"Two Pair, {Rank(high_pair).name.upper()}s and {Rank(low_pair).name.upper()}s"
        elif sorted_counts[0][1] == 2:
            hand_rank = HandRank.ONE_PAIR
            pair_rank = sorted_counts[0][0]
            kickers = tuple(r for r, count in sorted_counts[1:])
            score_tuple = (hand_rank.value, pair_rank, kickers)
            desc = f"One Pair, {Rank(pair_rank).name.upper()}S"
        else:
            hand_rank = HandRank.HIGH_CARD
            score_tuple = (hand_rank.value, tuple(ranks))
            desc = f"High Card, {sorted_cards[0].rank.name.upper()}"

        # Convert score tuple into a single comparable integer score
        numeric_score = HandEvaluator._tuple_to_score(score_tuple)

        return HandEvaluationResult(
            hand_rank=hand_rank,
            score=numeric_score,
            description=desc
        )

    @staticmethod
    def _check_straight(ranks: List[int]) -> Optional[int]:
        """Checks if a sorted list of 5 unique ranks forms a straight.
        
        Handles both normal straights and the Ace-low wheel straight (A-2-3-4-5).
        Returns the high card value of the straight if valid, otherwise None.
        """
        # Check standard straight (descending order consecutive values)
        if ranks == [ranks[0], ranks[0]-1, ranks[0]-2, ranks[0]-3, ranks[0]-4]:
            return ranks[0]
        
        # Check Ace-low wheel straight (A-5-4-3-2 -> ranks: [14, 5, 4, 3, 2])
        if set(ranks) == {14, 5, 4, 3, 2}:
            return 5  # In a 5-high wheel, 5 is the highest card for straight comparison

        return None

    @staticmethod
    def _tuple_to_score(score_tuple: tuple) -> int:
        """Encodes a hierarchical score tuple into a single deterministic integer 
        for reliable comparison across hands.
        """
        # Base conversion encoding ensuring distinct positional weights
        score = 0
        multiplier = 1
        
        # Flatten tuple elements recursively if nested (e.g., handling kickers tuple)
        flattened = []
        for item in score_tuple:
            if isinstance(item, tuple):
                flattened.extend(item)
            else:
                flattened.append(item)

        for val in reversed(flattened):
            score += val * multiplier
            multiplier *= 100  # Each rank category fits within 0-15 range, base 100 is safe
            
        return score