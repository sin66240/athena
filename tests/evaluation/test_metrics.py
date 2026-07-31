import pytest
from athena.evaluation.metrics import EvaluationResult, ModelEvaluator


def test_evaluation_result_creation_and_validation() -> None:
    """Test valid creation of EvaluationResult and field boundary validations."""
    res = EvaluationResult(
        accuracy=0.9,
        precision=0.85,
        recall=0.88,
        f1_score=0.86,
        samples=100
    )
    assert res.accuracy == 0.9
    assert res.precision == 0.85
    assert res.recall == 0.88
    assert res.f1_score == 0.86
    assert res.samples == 100

    # Invalid accuracy > 1.0
    with pytest.raises(ValueError, match="accuracy must be between 0.0 and 1.0"):
        EvaluationResult(accuracy=1.05, precision=0.5, recall=0.5, f1_score=0.5, samples=10)

    # Invalid negative samples
    with pytest.raises(ValueError, match="samples cannot be negative"):
        EvaluationResult(accuracy=0.5, precision=0.5, recall=0.5, f1_score=0.5, samples=-5)


def test_accuracy_calculation() -> None:
    """Test correct accuracy calculation."""
    evaluator = ModelEvaluator()
    preds = ["FOLD", "BET", "CALL", "CHECK"]
    labels = ["FOLD", "BET", "FOLD", "CHECK"]  # 3 correct out of 4 -> 0.75

    result = evaluator.evaluate(preds, labels)
    assert result.samples == 4
    assert result.accuracy == 0.75


def test_precision_calculation() -> None:
    """Test precision computation logic."""
    evaluator = ModelEvaluator()
    preds = ["BET", "BET", "FOLD", "CHECK"]
    labels = ["BET", "FOLD", "FOLD", "CHECK"]

    result = evaluator.evaluate(preds, labels)
    assert 0.0 <= result.precision <= 1.0
    assert result.samples == 4


def test_recall_calculation() -> None:
    """Test recall computation logic."""
    evaluator = ModelEvaluator()
    preds = ["CALL", "CHECK", "FOLD", "BET"]
    labels = ["CALL", "CHECK", "BET", "BET"]

    result = evaluator.evaluate(preds, labels)
    assert 0.0 <= result.recall <= 1.0
    assert result.samples == 4


def test_f1_calculation() -> None:
    """Test F1 score computation logic."""
    evaluator = ModelEvaluator()
    preds = ["RAISE", "FOLD", "CHECK"]
    labels = ["RAISE", "FOLD", "CHECK"]

    result = evaluator.evaluate(preds, labels)
    assert result.f1_score == 1.0  # Perfect match


def test_empty_dataset_and_validation() -> None:
    """Test handling of empty datasets and invalid inputs."""
    evaluator = ModelEvaluator()

    # Empty lists
    with pytest.raises(ValueError, match="Cannot evaluate empty datasets"):
        evaluator.evaluate([], [])

    # Length mismatch
    with pytest.raises(ValueError, match="Length mismatch"):
        evaluator.evaluate(["BET"], ["BET", "FOLD"])

    # Invalid type input
    with pytest.raises(TypeError, match="predictions and labels must be lists or sequences"):
        evaluator.evaluate("not-a-list", ["BET"])  # type: ignore