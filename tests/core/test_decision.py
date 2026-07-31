import pytest
from athena.core.decision import (
    ActionType,
    DecisionContext,
    DecisionEngine,
    DecisionResult,
)


def test_create_decision_context() -> None:
    """Test valid creation of a DecisionContext and attribute validation."""
    context = DecisionContext(
        stack_bb=50.0,
        pot_bb=10.0,
        position="BTN",
        street="FLOP",
        opponents=2,
        current_bet_bb=0.0,
        hand_strength=0.75,
        tournament_stage="MIDDLE",
    )

    assert context.stack_bb == 50.0
    assert context.position == "BTN"
    assert context.hand_strength == 0.75

    # Test invalid hand strength out of bounds (0.0 to 1.0)
    with pytest.raises(ValueError, match="hand_strength must be between 0.0 and 1.0"):
        DecisionContext(
            stack_bb=50.0,
            pot_bb=10.0,
            position="BTN",
            street="FLOP",
            opponents=2,
            current_bet_bb=0.0,
            hand_strength=1.5,
            tournament_stage="MIDDLE",
        )


def test_strong_hand_decision() -> None:
    """Test that strong hands result in aggressive actions (BET/RAISE)."""
    engine = DecisionEngine()
    
    # Strong hand, checked to on BTN -> Should Bet
    context = DecisionContext(
        stack_bb=40.0,
        pot_bb=6.0,
        position="BTN",
        street="FLOP",
        opponents=1,
        current_bet_bb=0.0,
        hand_strength=0.85,
        tournament_stage="EARLY",
    )
    result = engine.evaluate(context)

    assert result.action == ActionType.BET
    assert result.confidence >= 0.85
    assert "Monster hand" in result.reasoning or "Very strong hand" in result.reasoning


def test_weak_hand_decision() -> None:
    """Test that weak hands result in passive or defensive actions (FOLD/CHECK)."""
    engine = DecisionEngine()

    # Weak hand facing a bet -> Should Fold
    facing_bet_context = DecisionContext(
        stack_bb=30.0,
        pot_bb=12.0,
        position="BB",
        street="TURN",
        opponents=1,
        current_bet_bb=6.0,
        hand_strength=0.20,
        tournament_stage="MIDDLE",
    )
    result_fold = engine.evaluate(facing_bet_context)

    assert result_fold.action == ActionType.FOLD
    assert "Weak hand" in result_fold.reasoning

    # Weak hand checked to -> Should Check
    checked_to_context = DecisionContext(
        stack_bb=30.0,
        pot_bb=12.0,
        position="BB",
        street="TURN",
        opponents=1,
        current_bet_bb=0.0,
        hand_strength=0.20,
        tournament_stage="MIDDLE",
    )
    result_check = engine.evaluate(checked_to_context)

    assert result_check.action == ActionType.CHECK


def test_short_stack_behavior() -> None:
    """Test that short stacks show increased aggression (ALL_IN preference)."""
    engine = DecisionEngine()

    # Short stack (10 BB) with good hand strength (0.70) -> Should ALL_IN
    short_stack_context = DecisionContext(
        stack_bb=10.0,
        pot_bb=3.0,
        position="CO",
        street="PREFLOP",
        opponents=3,
        current_bet_bb=0.0,
        hand_strength=0.70,
        tournament_stage="LATE",
    )
    result = engine.evaluate(short_stack_context)

    assert result.action == ActionType.ALL_IN
    assert "Short stack" in result.reasoning


def test_decision_confidence_range() -> None:
    """Test that evaluated decisions produce confidence scores bounded between 0.0 and 1.0."""
    engine = DecisionEngine()
    context = DecisionContext(
        stack_bb=25.0,
        pot_bb=8.0,
        position="HJ",
        street="RIVER",
        opponents=1,
        current_bet_bb=4.0,
        hand_strength=0.55,
        tournament_stage="MIDDLE",
    )
    result = engine.evaluate(context)

    assert isinstance(result, DecisionResult)
    assert 0.0 <= result.confidence <= 1.0


def test_explanation_output() -> None:
    """Test that explain_decision generates a comprehensive narrative text output."""
    engine = DecisionEngine()
    context = DecisionContext(
        stack_bb=12.0,
        pot_bb=5.0,
        position="SB",
        street="PREFLOP",
        opponents=1,
        current_bet_bb=0.0,
        hand_strength=0.88,
        tournament_stage="FINAL_TABLE",
    )
    explanation = engine.explain_decision(context)

    assert isinstance(explanation, str)
    assert "[ATHENA Decision Summary]" in explanation
    assert "FINAL_TABLE" in explanation
    assert "Recommended Action:" in explanation
    assert "Rationale:" in explanation