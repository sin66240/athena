import pytest
from athena.data.dataset import TrainingSample, PokerDataset
from athena.training.pipeline import TrainingMetrics, TrainingPipeline
from athena.ai.model import DummyModel


def test_training_sample_creation_and_validation() -> None:
    """Test creating valid TrainingSample instances and enforcing validation rules."""
    sample = TrainingSample(
        features=[1.5, 2.0, 3.1],
        label="RAISE",
        metadata={"street": "RIVER"}
    )
    assert sample.features == [1.5, 2.0, 3.1]
    assert sample.label == "RAISE"
    assert sample.metadata["street"] == "RIVER"

    # Test features not being a list
    with pytest.raises(TypeError, match="features must be a list"):
        TrainingSample(features="not-a-list", label="FOLD")  # type: ignore

    # Test features containing non-numeric elements
    with pytest.raises(ValueError, match="All elements in features must be numbers"):
        TrainingSample(features=[1.0, "invalid"], label="FOLD")  # type: ignore

    # Test empty label validation
    with pytest.raises(ValueError, match="label cannot be empty or blank"):
        TrainingSample(features=[1.0, 2.0], label="")


def test_poker_dataset_operations() -> None:
    """Test adding samples, size checking, and feature/label extraction methods."""
    dataset = PokerDataset()
    assert dataset.size() == 0

    sample1 = TrainingSample(features=[0.1, 0.2], label="CHECK")
    sample2 = TrainingSample(features=[0.3, 0.4], label="BET")

    dataset.add_sample(sample1)
    dataset.add_sample(sample2)

    assert dataset.size() == 2
    assert dataset.get_features() == [[0.1, 0.2], [0.3, 0.4]]
    assert dataset.get_labels() == ["CHECK", "BET"]

    # Test adding invalid type
    with pytest.raises(TypeError, match="Can only add TrainingSample instances"):
        dataset.add_sample("not-a-sample")  # type: ignore


def test_training_metrics_validation() -> None:
    """Test TrainingMetrics validation rules for accuracy and loss boundaries."""
    metrics = TrainingMetrics(accuracy=0.92, loss=0.12, samples=50)
    assert metrics.accuracy == 0.92
    assert metrics.loss == 0.12
    assert metrics.samples == 50

    # Invalid accuracy > 1.0
    with pytest.raises(ValueError, match="accuracy must be between 0.0 and 1.0"):
        TrainingMetrics(accuracy=1.05, loss=0.1, samples=10)

    # Invalid negative loss
    with pytest.raises(ValueError, match="loss cannot be negative"):
        TrainingMetrics(accuracy=0.85, loss=-0.01, samples=10)


def test_pipeline_prepare() -> None:
    """Test pipeline preparation phase with valid and empty datasets."""
    pipeline = TrainingPipeline()
    dataset = PokerDataset()
    dataset.add_sample(TrainingSample(features=[1.0, 2.0], label="CALL"))

    pipeline.prepare(dataset)
    assert pipeline._is_prepared is True

    # Preparing with an empty dataset should raise ValueError
    empty_dataset = PokerDataset()
    with pytest.raises(ValueError, match="Cannot prepare pipeline with an empty dataset"):
        pipeline.prepare(empty_dataset)


def test_pipeline_train() -> None:
    """Test training phase integration with a concrete DummyModel."""
    dataset = PokerDataset()
    dataset.add_sample(TrainingSample(features=[10.0, 20.0], label="BET"))

    pipeline = TrainingPipeline()
    pipeline.prepare(dataset)

    model = DummyModel()
    pipeline.train(model)
    assert model._is_trained is True

    # Training without calling prepare first should raise RuntimeError
    unprepared_pipeline = TrainingPipeline()
    with pytest.raises(RuntimeError, match="Pipeline must be prepared"):
        unprepared_pipeline.train(model)


def test_pipeline_evaluate() -> None:
    """Test evaluation phase returning structured TrainingMetrics."""
    dataset = PokerDataset()
    dataset.add_sample(TrainingSample(features=[5.0, 6.0], label="CHECK"))
    dataset.add_sample(TrainingSample(features=[7.0, 8.0], label="RAISE"))

    pipeline = TrainingPipeline()
    pipeline.prepare(dataset)

    metrics = pipeline.evaluate()
    assert isinstance(metrics, TrainingMetrics)
    assert metrics.samples == 2
    assert 0.0 <= metrics.accuracy <= 1.0
    assert metrics.loss >= 0.0