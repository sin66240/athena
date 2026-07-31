import pytest
from athena.core.decision import DecisionContext
from athena.core.features import FeatureEncoder, FeatureVector
from athena.core.game_state import Street
from athena.core.position import Position
from athena.core.tournament import TournamentStage


def test_position_encoding() -> None:
    """Test encoding of table position strings and enums."""
    assert FeatureEncoder.encode_position("UTG") == 0
    assert FeatureEncoder.encode_position(Position.BTN) == 3
    assert FeatureEncoder.encode_position("BB") == 5

    with pytest.raises(ValueError, match="Unknown position"):
        FeatureEncoder.encode_position("INVALID_POS")


def test_street_encoding() -> None:
    """Test encoding of betting street strings and enums."""
    assert FeatureEncoder.encode_street("PREFLOP") == 0
    assert FeatureEncoder.encode_street(Street.RIVER) == 3
    assert FeatureEncoder.encode_street("FLOP") == 1

    with pytest.raises(ValueError, match="Unknown street"):
        FeatureEncoder.encode_street("INVALID_STREET")


def test_tournament_stage_encoding() -> None:
    """Test encoding of tournament stage strings and enums."""
    assert FeatureEncoder.encode_stage("EARLY") == 0
    assert FeatureEncoder.encode_stage(TournamentStage.FINAL_TABLE) == 3
    assert FeatureEncoder.encode_stage("MIDDLE") == 1

    with pytest.raises(ValueError, match="Unknown stage"):
        FeatureEncoder.encode_stage("INVALID_STAGE")


def test_feature_vector_creation() -> None:
    """Test creating a FeatureVector from a DecisionContext and checking serialization methods."""
    context = DecisionContext(
        stack_bb=40.0,
        pot_bb=8.0,
        position="BTN",
        street="FLOP",
        opponents=2,
        current_bet_bb=4.0,
        hand_strength=0.75,
        tournament_stage="MIDDLE",
    )
    
    encoder = FeatureEncoder()
    vector = encoder.create_vector(context)

    assert isinstance(vector, FeatureVector)
    assert vector.stack_bb == 40.0
    assert vector.pot_bb == 8.0
    assert vector.position_encoded == 3  # BTN
    assert vector.street_encoded == 1   # FLOP
    assert vector.opponents == 2
    assert vector.hand_strength == 0.75
    assert vector.tournament_stage_encoded == 1  # MIDDLE
    
    # Test tuple conversion (ML format)
    tup = vector.to_tuple()
    assert isinstance(tup, tuple)
    assert len(tup) == 9
    assert tup[0] == 40.0
    assert tup[2] == 3.0

    # Test dictionary conversion
    d = vector.to_dict()
    assert isinstance(d, dict)
    assert "stack_bb" in d
    assert "risk_factor" in d
    assert d["position_encoded"] == 3.0


def test_feature_values_range() -> None:
    """Test that derived feature values (aggression and risk factors) stay within valid ranges."""
    context = DecisionContext(
        stack_bb=20.0,
        pot_bb=10.0,
        position="SB",
        street="RIVER",
        opponents=5,
        current_bet_bb=10.0,
        hand_strength=0.30,
        tournament_stage="FINAL_TABLE",
    )

    encoder = FeatureEncoder()
    vector = encoder.create_vector(context)

    # Aggression factor = current_bet_bb / pot_bb = 10.0 / 10.0 = 1.0
    assert 0.0 <= vector.aggression_factor <= 5.0
    assert vector.aggression_factor == 1.0

    # Risk factor should be properly bounded between 0.0 and 1.0
    assert 0.0 <= vector.risk_factor <= 1.0