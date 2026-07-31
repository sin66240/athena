import pytest
import os
from athena.ai.model import (
    ModelType,
    PredictionResult,
    DummyModel,
)


def test_model_type_enum() -> None:
    """Test that all ModelType enum members exist correctly."""
    assert ModelType.BASELINE is not None
    assert ModelType.MACHINE_LEARNING is not None
    assert ModelType.NEURAL_NETWORK is not None


def test_prediction_result_creation_and_validation() -> None:
    """Test creating valid PredictionResult and validating confidence boundaries."""
    result = PredictionResult(
        action="BET",
        confidence=0.95,
        model_name="TestModel",
        model_version="1.0.0",
    )
    assert result.action == "BET"
    assert result.confidence == 0.95
    assert result.model_name == "TestModel"
    assert result.model_version == "1.0.0"

    # Test invalid confidence bounds (< 0.0)
    with pytest.raises(ValueError, match="confidence must be between 0.0 and 1.0"):
        PredictionResult(
            action="BET",
            confidence=-0.1,
            model_name="TestModel",
            model_version="1.0.0",
        )

    # Test invalid confidence bounds (> 1.0)
    with pytest.raises(ValueError, match="confidence must be between 0.0 and 1.0"):
        PredictionResult(
            action="BET",
            confidence=1.05,
            model_name="TestModel",
            model_version="1.0.0",
        )

    # Test empty action validation
    with pytest.raises(ValueError, match="action is required"):
        PredictionResult(
            action="",
            confidence=0.5,
            model_name="TestModel",
            model_version="1.0.0",
        )


def test_dummy_model_prediction() -> None:
    """Test that DummyModel returns a valid PredictionResult with confidence between 0 and 1."""
    model = DummyModel(model_version="v1.2.3", default_action="RAISE", default_confidence=0.88)
    features = [40.0, 8.0, 3.0, 1.0, 2.0, 0.75, 1.0, 0.5, 0.2]
    
    prediction = model.predict(features)
    
    assert isinstance(prediction, PredictionResult)
    assert prediction.action == "RAISE"
    assert 0.0 <= prediction.confidence <= 1.0
    assert prediction.confidence == 0.88
    assert prediction.model_name == "DummyModel"
    assert prediction.model_version == "v1.2.3"


def test_dummy_model_train() -> None:
    """Test training method behavior for DummyModel."""
    model = DummyModel()
    with pytest.raises(ValueError, match="Dataset cannot be empty"):
        model.train([])
        
    model.train([[1.0, 2.0], [3.0, 4.0]])
    assert model._is_trained is True


def test_save_and_load_model(tmp_path) -> None:
    """Test saving and loading model state using standard library files."""
    model_path = tmp_path / "dummy_model.json"
    
    model = DummyModel(model_version="v2.0.0", default_action="CALL", default_confidence=0.75)
    model.save(str(model_path))
    
    assert os.path.exists(model_path)
    
    # Load state into a new model instance
    loaded_model = DummyModel(model_version="v0.0.1", default_action="CHECK", default_confidence=0.5)
    loaded_model.load(str(model_path))
    
    assert loaded_model.model_version == "v2.0.0"
    assert loaded_model.default_action == "CALL"
    assert loaded_model.default_confidence == 0.75
    assert loaded_model._is_trained is False

    # Test loading non-existent file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        loaded_model.load(str(tmp_path / "non_existent.json"))