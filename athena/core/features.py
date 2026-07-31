from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping
from athena.core.decision import DecisionContext, DecisionEngine
from athena.core.game_state import Street
from athena.core.position import Position
from athena.core.tournament import TournamentStage


@dataclass(frozen=True, slots=True)
class FeatureVector:
    """ML-ready numerical feature representation of a poker decision context.
    
    Attributes:
        stack_bb: Stack depth in Big Blinds.
        pot_bb: Total pot size in Big Blinds.
        position_encoded: Integer categorical encoding of table position (0-5).
        street_encoded: Integer ordinal encoding of betting street (0-3).
        opponents: Count of active opponents remaining.
        hand_strength: Normalized hand strength/equity between 0.0 and 1.0.
        tournament_stage_encoded: Integer ordinal encoding of tournament phase (0-3).
        aggression_factor: Normalized ratio of active bet to total pot.
        risk_factor: Normalized context risk assessment score (0.0 to 1.0).
    """
    stack_bb: float
    pot_bb: float
    position_encoded: int
    street_encoded: int
    opponents: int
    hand_strength: float
    tournament_stage_encoded: int
    aggression_factor: float
    risk_factor: float

    def to_tuple(self) -> tuple[float, ...]:
        """Converts the feature vector into a flat tuple of floats for ML model input.
        
        Returns:
            Tuple of floats containing all numerical features in canonical order.
        """
        return (
            float(self.stack_bb),
            float(self.pot_bb),
            float(self.position_encoded),
            float(self.street_encoded),
            float(self.opponents),
            float(self.hand_strength),
            float(self.tournament_stage_encoded),
            float(self.aggression_factor),
            float(self.risk_factor),
        )

    def to_dict(self) -> dict[str, float]:
        """Converts the feature vector into a dictionary mapping feature names to numerical values.
        
        Returns:
            Dictionary with feature names as keys and floats as values.
        """
        return {
            "stack_bb": float(self.stack_bb),
            "pot_bb": float(self.pot_bb),
            "position_encoded": float(self.position_encoded),
            "street_encoded": float(self.street_encoded),
            "opponents": float(self.opponents),
            "hand_strength": float(self.hand_strength),
            "tournament_stage_encoded": float(self.tournament_stage_encoded),
            "aggression_factor": float(self.aggression_factor),
            "risk_factor": float(self.risk_factor),
        }


class FeatureEncoder:
    """Transforms raw poker domain objects and DecisionContext instances into 
    deterministic, ML-ready numerical FeatureVector representations.
    """

    _POSITION_MAP: Mapping[str, int] = {
        "UTG": 0,
        "UTG_PLUS_1": 0,
        "MP": 1,
        "LJ": 1,
        "HJ": 1,
        "CO": 2,
        "BTN": 3,
        "SB": 4,
        "BB": 5,
    }

    _STREET_MAP: Mapping[str, int] = {
        "PREFLOP": 0,
        "FLOP": 1,
        "TURN": 2,
        "RIVER": 3,
    }

    _STAGE_MAP: Mapping[str, int] = {
        "EARLY": 0,
        "MIDDLE": 1,
        "LATE": 2,
        "FINAL_TABLE": 3,
    }

    def __init__(self, decision_engine: DecisionEngine | None = None) -> None:
        """Initializes the FeatureEncoder with an optional DecisionEngine instance 
        for risk factor calculations.
        """
        self._decision_engine = decision_engine or DecisionEngine()

    @classmethod
    def encode_position(cls, position: Position | str) -> int:
        """Encodes a position enum or string into its discrete categorical integer index.
        
        UTG/UTG+1 -> 0
        MP/LJ/HJ   -> 1
        CO         -> 2
        BTN        -> 3
        SB         -> 4
        BB         -> 5

        Args:
            position: Position enum instance or position string (e.g., 'BTN', 'UTG').

        Returns:
            Integer encoding between 0 and 5.

        Raises:
            ValueError: If position is unmapped or invalid.
        """
        pos_str = position.name if isinstance(position, Position) else str(position).upper().strip()
        
        if pos_str in cls._POSITION_MAP:
            return cls._POSITION_MAP[pos_str]
        raise ValueError(f"Unknown position '{position}'. Expected one of {list(cls._POSITION_MAP.keys())}")

    @classmethod
    def encode_street(cls, street: Street | str) -> int:
        """Encodes a betting street enum or string into its discrete ordinal integer index.
        
        PREFLOP -> 0
        FLOP    -> 1
        TURN    -> 2
        RIVER   -> 3

        Args:
            street: Street enum instance or street string (e.g., 'PREFLOP', 'FLOP').

        Returns:
            Integer encoding between 0 and 3.

        Raises:
            ValueError: If street is unmapped or invalid.
        """
        street_str = street.name if isinstance(street, Street) else str(street).upper().strip()
        
        if street_str in cls._STREET_MAP:
            return cls._STREET_MAP[street_str]
        raise ValueError(f"Unknown street '{street}'. Expected one of {list(cls._STREET_MAP.keys())}")

    @classmethod
    def encode_stage(cls, stage: TournamentStage | str) -> int:
        """Encodes a tournament stage enum or string into its discrete ordinal integer index.
        
        EARLY       -> 0
        MIDDLE      -> 1
        LATE        -> 2
        FINAL_TABLE -> 3

        Args:
            stage: TournamentStage enum instance or stage string (e.g., 'EARLY', 'FINAL_TABLE').

        Returns:
            Integer encoding between 0 and 3.

        Raises:
            ValueError: If stage is unmapped or invalid.
        """
        stage_str = stage.name if isinstance(stage, TournamentStage) else str(stage).upper().strip()
        
        if stage_str in cls._STAGE_MAP:
            return cls._STAGE_MAP[stage_str]
        raise ValueError(f"Unknown stage '{stage}'. Expected one of {list(cls._STAGE_MAP.keys())}")

    def create_vector(self, context: DecisionContext) -> FeatureVector:
        """Transforms a DecisionContext into a deterministic FeatureVector instance.

        Args:
            context: DecisionContext containing the snapshot of the hand state.

        Returns:
            FeatureVector with all categorical and derived features properly encoded.
        """
        pos_encoded = self.encode_position(context.position)
        street_encoded = self.encode_street(context.street)
        stage_encoded = self.encode_stage(context.tournament_stage)

        # Derived Feature: Aggression Factor = facing bet relative to current pot size
        # Prevents division by zero when pot is 0.0
        tot_pot = max(0.001, context.pot_bb)
        aggression = min(5.0, context.current_bet_bb / tot_pot)

        # Derived Feature: Risk Factor calculated via DecisionEngine
        risk = self.decision_engine_risk(context)

        return FeatureVector(
            stack_bb=context.stack_bb,
            pot_bb=context.pot_bb,
            position_encoded=pos_encoded,
            street_encoded=street_encoded,
            opponents=context.opponents,
            hand_strength=context.hand_strength,
            tournament_stage_encoded=stage_encoded,
            aggression_factor=aggression,
            risk_factor=risk,
        )

    def decision_engine_risk(self, context: DecisionContext) -> float:
        """Computes risk factor for the context using the embedded DecisionEngine.

        Args:
            context: DecisionContext instance.

        Returns:
            Normalized risk score between 0.0 and 1.0.
        """
        return self._decision_engine.calculate_risk(context)