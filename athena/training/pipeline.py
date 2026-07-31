from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING
from athena.data.dataset import PokerDataset

if TYPE_CHECKING:
    from athena.ai.model import PokerModel


@dataclass(frozen=True, slots=True)
class TrainingMetrics:
    """Encapsulates evaluation metrics resulting from a training pipeline run.
    
    Attributes:
        accuracy: Model accuracy score between 0.0 and 1.0.
        loss: Model loss value (must be >= 0.0).
        samples: Total number of evaluated samples.
    """
    accuracy: float
    loss: float
    samples: int

    def __post_init__(self) -> None:
        """Validates metric value ranges."""
        if not (0.0 <= self.accuracy <= 1.0):
            raise ValueError(f"accuracy must be between 0.0 and 1.0. Got: {self.accuracy}")
        if self.loss < 0.0:
            raise ValueError(f"loss cannot be negative. Got: {self.loss}")
        if self.samples < 0:
            raise ValueError(f"samples cannot be negative. Got: {self.samples}")


@dataclass(slots=True)
class TrainingPipeline:
    """Manages the preparation, training, and evaluation lifecycle of ATHENA AI models."""
    _dataset: PokerDataset | None = None
    _is_prepared: bool = False

    def prepare(self, dataset: PokerDataset) -> None:
        """Prepares the training pipeline with a target PokerDataset.
        
        Args:
            dataset: The PokerDataset instance to use for training/evaluation.
            
        Raises:
            ValueError: If the dataset is empty.
        """
        if not isinstance(dataset, PokerDataset):
            raise TypeError("dataset must be an instance of PokerDataset.")
        if dataset.size() == 0:
            raise ValueError("Cannot prepare pipeline with an empty dataset.")
        
        self._dataset = dataset
        self._is_prepared = True

    def train(self, model: PokerModel) -> None:
        """Trains a given PokerModel using the prepared dataset features.
        
        Args:
            model: A concrete implementation of PokerModel from athena.ai.model.
            
        Raises:
            RuntimeError: If the pipeline has not been prepared with a dataset.
        """
        if not self._is_prepared or self._dataset is None:
            raise RuntimeError("Pipeline must be prepared with a dataset before training.")
        
        features = self._dataset.get_features()
        model.train(features)

    def evaluate(self, dataset: PokerDataset | None = None) -> TrainingMetrics:
        """Evaluates model/pipeline state against a dataset and returns structured TrainingMetrics.
        
        Args:
            dataset: Optional alternative PokerDataset to evaluate. Defaults to the prepared dataset.
            
        Returns:
            TrainingMetrics containing accuracy, loss, and sample count.
        """
        target_dataset = dataset if dataset is not None else self._dataset
        if target_dataset is None or target_dataset.size() == 0:
            raise ValueError("No valid dataset available for evaluation.")
        
        sample_count = target_dataset.size()
        # Baseline foundational mock evaluation metrics
        return TrainingMetrics(
            accuracy=0.88,
            loss=0.21,
            samples=sample_count,
        )