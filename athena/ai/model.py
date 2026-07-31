from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Sequence
import json
import os


class ModelType(Enum):
    """Enumeration representing the underlying AI model architecture type."""
    BASELINE = auto()
    MACHINE_LEARNING = auto()
    NEURAL_NETWORK = auto()


@dataclass(frozen=True, slots=True)
class PredictionResult:
    """Represents the structured prediction output from an AI model.
    
    Attributes:
        action: The recommended action (e.g., 'BET', 'FOLD', 'CALL').
        confidence: Degree of certainty in the prediction (0.0 to 1.0).
        model_name: Name/identifier of the model that generated the prediction.
        model_version: Version string of the model.
    """
    action: str
    confidence: float
    model_name: str
    model_version: str

    def __post_init__(self) -> None:
        """Validates prediction result attributes upon initialization."""
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"confidence must be between 0.0 and 1.0. Got: {self.confidence}")
        if not self.action or not str(self.action).strip():
            raise ValueError("action is required and cannot be empty.")
        if not self.model_name or not str(self.model_name).strip():
            raise ValueError("model_name is required and cannot be empty.")
        if not self.model_version or not str(self.model_version).strip():
            raise ValueError("model_version is required and cannot be empty.")


class PokerModel(ABC):
    """Abstract Base Class defining the standard contract for ATHENA AI poker models."""

    @abstractmethod
    def predict(self, features: Sequence[float] | dict[str, Any]) -> PredictionResult:
        """Generates a structured prediction based on input features."""
        pass

    @abstractmethod
    def train(self, dataset: list[Any]) -> None:
        """Trains or fine-tunes the model on a given dataset."""
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        """Saves model state and metadata to disk at the specified path."""
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        """Loads model state and metadata from disk from the specified path."""
        pass


class DummyModel(PokerModel):
    """A concrete baseline model implementation for testing and validation purposes."""

    def __init__(
        self,
        model_version: str = "v1.0.0",
        default_action: str = "CHECK",
        default_confidence: float = 0.85
    ) -> None:
        self.model_name: str = "DummyModel"
        self.model_version: str = model_version
        self.default_action: str = default_action
        self.default_confidence: float = default_confidence
        self._is_trained: bool = False

    def predict(self, features: Sequence[float] | dict[str, Any]) -> PredictionResult:
        """Returns a predictable dummy PredictionResult."""
        return PredictionResult(
            action=self.default_action,
            confidence=self.default_confidence,
            model_name=self.model_name,
            model_version=self.model_version,
        )

    def train(self, dataset: list[Any]) -> None:
        """Simulates model training."""
        if not dataset:
            raise ValueError("Dataset cannot be empty for training.")
        self._is_trained = True

    def save(self, path: str) -> None:
        """Saves model metadata to disk using standard library JSON serialization."""
        data = {
            "model_name": self.model_name,
            "model_version": self.model_version,
            "default_action": self.default_action,
            "default_confidence": self.default_confidence,
            "is_trained": self._is_trained,
        }
        
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def load(self, path: str) -> None:
        """Loads model metadata from disk using standard library JSON deserialization."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file not found at {path}")
            
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.model_name = data.get("model_name", self.model_name)
        self.model_version = data.get("model_version", self.model_version)
        self.default_action = data.get("default_action", self.default_action)
        self.default_confidence = data.get("default_confidence", self.default_confidence)
        self._is_trained = data.get("is_trained", False)