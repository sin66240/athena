import pytest
from athena.service.decision_engine import DecisionResponse, DecisionEngine
from athena.ai.model import DummyModel
from athena.core.decision import DecisionContext


def test_decision_response_creation_and_validation() -> None:
    """Test creating valid DecisionResponse and validating confidence/action constraints."""
    response = DecisionResponse(
        action="BET",
        confidence=0.92,
        reasoning="Test model reasoning"
    )
    assert response.action == "BET"
    assert response.confidence == 0.92
    assert response.reasoning == "Test model reasoning"

    # Test confidence below 0.0
    with pytest.raises(ValueError, match="confidence must be between 0.0 and 1.0"):
        DecisionResponse(action="BET", confidence=-0.05, reasoning="")

    # Test confidence above 1.0
    with pytest.raises(ValueError, match="confidence must be between 0.0 and 1.0"):
        DecisionResponse(action="BET", confidence=1.05, reasoning="")

    # Test empty action handling
    with pytest.raises(ValueError, match="action must be a non-empty string"):
        DecisionResponse(action="", confidence=0.8, reasoning="")


def test_engine_initialization() -> None:
    """Test DecisionEngine initialization with a valid PokerModel."""
    model = DummyModel()
    engine = DecisionEngine(model)
    assert engine._model == model


def test_decision_generation() -> None:
    """Test full decision flow from game state to DecisionResponse using DummyModel."""
    model = DummyModel(model_version="v1.0.0", default_action="RAISE", default_confidence=0.85)
    engine = DecisionEngine(model)

    context = DecisionContext(
        stack_bb=30.0,
        pot_bb=6.0,
        position="CO",
        street="FLOP",
        opponents=2,
        current_bet_bb=2.0,
        hand_strength=0.78,
        tournament_stage="MIDDLE",
    )

    response = engine.decide(context)
    
    assert isinstance(response, DecisionResponse)
    assert response.action == "RAISE"
    assert response.confidence == 0.85
    assert "DummyModel" in response.reasoning