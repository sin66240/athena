from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class TrainingSample:
    """Represents a single training sample containing numerical features, a label, and metadata.
    
    Attributes:
        features: List of numerical features (int or float).
        label: The classification or target label string.
        metadata: Additional contextual dictionary information.
    """
    features: list[float]
    label: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validates that features are numeric and label is non-empty."""
        if not isinstance(self.features, list):
            raise TypeError("features must be a list.")
        if not all(isinstance(x, (int, float)) for x in self.features):
            raise ValueError("All elements in features must be numbers (int or float).")
        if not self.label or not str(self.label).strip():
            raise ValueError("label cannot be empty or blank.")


@dataclass(slots=True)
class PokerDataset:
    """Manages a collection of TrainingSample instances for AI model training and evaluation."""
    samples: list[TrainingSample] = field(default_factory=list)

    def add_sample(self, sample: TrainingSample) -> None:
        """Adds a TrainingSample to the dataset.
        
        Args:
            sample: The TrainingSample instance to add.
            
        Raises:
            TypeError: If the object is not a TrainingSample.
        """
        if not isinstance(sample, TrainingSample):
            raise TypeError("Can only add TrainingSample instances to PokerDataset.")
        self.samples.append(sample)

    def size(self) -> int:
        """Returns the total number of samples stored in the dataset."""
        return len(self.samples)

    def get_features(self) -> list[list[float]]:
        """Extracts and returns all feature vectors from the dataset.
        
        Returns:
            A list of feature lists.
        """
        return [sample.features for sample in self.samples]

    def get_labels(self) -> list[str]:
        """Extracts and returns all target labels from the dataset.
        
        Returns:
            A list of label strings.
        """
        return [sample.label for sample in self.samples]