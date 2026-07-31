from __future__ import annotations
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    """Represents structured evaluation metrics for model predictions.
    
    Attributes:
        accuracy: Overall classification accuracy (0.0 to 1.0).
        precision: Macro-averaged precision score (0.0 to 1.0).
        recall: Macro-averaged recall score (0.0 to 1.0).
        f1_score: Macro-averaged F1 score (0.0 to 1.0).
        samples: Total number of evaluated samples.
    """
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    samples: int

    def __post_init__(self) -> None:
        """Validates evaluation metric boundaries."""
        if not (0.0 <= self.accuracy <= 1.0):
            raise ValueError(f"accuracy must be between 0.0 and 1.0. Got: {self.accuracy}")
        if not (0.0 <= self.precision <= 1.0):
            raise ValueError(f"precision must be between 0.0 and 1.0. Got: {self.precision}")
        if not (0.0 <= self.recall <= 1.0):
            raise ValueError(f"recall must be between 0.0 and 1.0. Got: {self.recall}")
        if not (0.0 <= self.f1_score <= 1.0):
            raise ValueError(f"f1_score must be between 0.0 and 1.0. Got: {self.f1_score}")
        if self.samples < 0:
            raise ValueError(f"samples cannot be negative. Got: {self.samples}")


class ModelEvaluator:
    """Evaluates model prediction performance against ground-truth labels 
    using pure Python without external dependencies. Supports binary and multiclass string labels.
    """

    def evaluate(self, predictions: Sequence[str], labels: Sequence[str]) -> EvaluationResult:
        """Evaluates predictions against true labels and returns an EvaluationResult.
        
        Args:
            predictions: List or sequence of predicted label strings.
            labels: List or sequence of true ground-truth label strings.
            
        Returns:
            EvaluationResult containing accuracy, precision, recall, f1_score, and samples.
            
        Raises:
            TypeError: If inputs are not valid sequences.
            ValueError: If datasets are empty or lengths do not match.
        """
        if not isinstance(predictions, (list, tuple)) or not isinstance(labels, (list, tuple)):
            raise TypeError("predictions and labels must be lists or sequences.")
        
        if len(predictions) != len(labels):
            raise ValueError(f"Length mismatch: predictions ({len(predictions)}) and labels ({len(labels)}) must have equal length.")
        
        samples = len(predictions)
        if samples == 0:
            raise ValueError("Cannot evaluate empty datasets.")
        
        # Convert to lists of strings and normalize
        preds = [str(p).strip().upper() for p in predictions]
        trues = [str(l).strip().upper() for l in labels]

        # Calculate Accuracy
        correct = sum(1 for p, t in zip(preds, trues) if p == t)
        accuracy = float(correct) / float(samples)

        # Identify all unique classes present
        unique_classes = sorted(list(set(trues) | set(preds)))
        num_classes = len(unique_classes)

        if num_classes == 0:
            return EvaluationResult(accuracy=accuracy, precision=0.0, recall=0.0, f1_score=0.0, samples=samples)

        precisions = []
        recalls = []
        f1s = []

        for cls in unique_classes:
            tp = sum(1 for p, t in zip(preds, trues) if p == cls and t == cls)
            fp = sum(1 for p, t in zip(preds, trues) if p == cls and t != cls)
            fn = sum(1 for p, t in zip(preds, trues) if p != cls and t == cls)

            # Avoid division by zero
            p_cls = float(tp) / float(tp + fp) if (tp + fp) > 0 else 0.0
            r_cls = float(tp) / float(tp + fn) if (tp + fn) > 0 else 0.0
            
            if (p_cls + r_cls) > 0:
                f1_cls = 2.0 * (p_cls * r_cls) / (p_cls + r_cls)
            else:
                f1_cls = 0.0

            precisions.append(p_cls)
            recalls.append(r_cls)
            f1s.append(f1_cls)

        # Macro-averaging across classes
        macro_precision = sum(precisions) / float(num_classes)
        macro_recall = sum(recalls) / float(num_classes)
        macro_f1 = sum(f1s) / float(num_classes)

        return EvaluationResult(
            accuracy=accuracy,
            precision=macro_precision,
            recall=macro_recall,
            f1_score=macro_f1,
            samples=samples,
        )