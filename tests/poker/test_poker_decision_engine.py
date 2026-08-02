from athena.poker.poker_decision_engine import PokerDecisionEngine

from athena.core.decision import (
    DecisionContext,
    ActionType,
)


def test_premium_deep_stack():

    engine = PokerDecisionEngine()

    context = DecisionContext(

        stack_bb=50,
        pot_bb=5,
        position="BTN",
        street="PREFLOP",
        opponents=3,
        current_bet_bb=2,
        hand_strength=0.95,
        tournament_stage="MIDDLE",

    )

    result = engine.evaluate(context)

    assert result.action == ActionType.RAISE


def test_strong_hand_late_position():

    engine = PokerDecisionEngine()

    context = DecisionContext(

        stack_bb=30,
        pot_bb=5,
        position="CO",
        street="PREFLOP",
        opponents=4,
        current_bet_bb=2,
        hand_strength=0.80,
        tournament_stage="MIDDLE",

    )

    result = engine.evaluate(context)

    assert result.action == ActionType.RAISE


def test_weak_hand():

    engine = PokerDecisionEngine()

    context = DecisionContext(

        stack_bb=40,
        pot_bb=5,
        position="UTG",
        street="PREFLOP",
        opponents=5,
        current_bet_bb=2,
        hand_strength=0.20,
        tournament_stage="MIDDLE",

    )

    result = engine.evaluate(context)

    assert result.action == ActionType.FOLD
