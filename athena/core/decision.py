from __future__ import annotations
from enum import Enum, auto
from dataclasses import dataclass


class ActionType(Enum):
    """Enumeration of macro decision action types available to a player."""
    FOLD = auto()
    CHECK = auto()
    CALL = auto()
    BET = auto()
    RAISE = auto()
    ALL_IN = auto()


@dataclass(frozen=True, slots=True)
class DecisionContext:
    """Encapsulates the essential analytical context required to formulate a poker decision.
    
    Attributes:
        stack_bb: Effective stack depth measured in Big Blinds.
        pot_bb: Current total pot size in Big Blinds.
        position: Player's position string (e.g., 'BTN', 'UTG', 'BB').
        street: Current betting round ('PREFLOP', 'FLOP', 'TURN', 'RIVER').
        opponents: Number of active opponents remaining in the hand.
        current_bet_bb: Amount needed to match the current bet in Big Blinds (0 if checked to).
        hand_strength: Normalized hand equity/strength value between 0.0 (weakest) and 1.0 (nuts).
        tournament_stage: Macro tournament stage ('EARLY', 'MIDDLE', 'LATE', 'FINAL_TABLE').
    """
    stack_bb: float
    pot_bb: float
    position: str
    street: str
    opponents: int
    current_bet_bb: float
    hand_strength: float
    tournament_stage: str

    def __post_init__(self) -> None:
        """Validates decision context parameters."""
        if self.stack_bb < 0:
            raise ValueError(f"stack_bb cannot be negative. Got: {self.stack_bb}")
        if self.pot_bb < 0:
            raise ValueError(f"pot_bb cannot be negative. Got: {self.pot_bb}")
        if self.opponents < 0:
            raise ValueError(f"opponents cannot be negative. Got: {self.opponents}")
        if self.current_bet_bb < 0:
            raise ValueError(f"current_bet_bb cannot be negative. Got: {self.current_bet_bb}")
        if not (0.0 <= self.hand_strength <= 1.0):
            raise ValueError(f"hand_strength must be between 0.0 and 1.0. Got: {self.hand_strength}")


@dataclass(frozen=True, slots=True)
class DecisionResult:
    """Represents the output decision, confidence score, and clear reasoning explanation.
    
    Attributes:
        action: Recommended ActionType.
        confidence: Degree of certainty in decision (0.0 to 1.0).
        reasoning: Human-readable narrative explaining the underlying decision logic.
    """
    action: ActionType
    confidence: float
    reasoning: str

    def __post_init__(self) -> None:
        """Validates decision result attributes."""
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"confidence must be between 0.0 and 1.0. Got: {self.confidence}")


class DecisionEngine:
    """Baseline rule-based Decision Intelligence Engine for ATHENA.
    Serves as the deterministic foundation for future AI and strategic model integrations.
    """

    def evaluate(self, context: DecisionContext) -> DecisionResult:
        """Evaluates a decision context using baseline heuristic rules and returns a DecisionResult.
        
        Args:
            context: DecisionContext object describing the state of the hand.
            
        Returns:
            DecisionResult object containing recommended action, confidence, and explanation.
        """
        risk_score = self.calculate_risk(context)
        is_facing_bet = context.current_bet_bb > 0

        # Rule 1: Short Stack Push/Fold or Jam territory (stack <= 15 BB)
        if context.stack_bb <= 15.0:
            if context.hand_strength >= 0.65:
                return DecisionResult(
                    action=ActionType.ALL_IN,
                    confidence=0.90,
                    reasoning=f"Short stack ({context.stack_bb:.1f} BB) with strong hand (strength: {context.hand_strength:.2f}). Pushing for maximum value/fold equity."
                )
            elif not is_facing_bet and context.hand_strength >= 0.45:
                return DecisionResult(
                    action=ActionType.ALL_IN if context.stack_bb <= 10.0 else ActionType.BET,
                    confidence=0.75,
                    reasoning=f"Short stack ({context.stack_bb:.1f} BB) taking aggressive initiative with moderate hand strength ({context.hand_strength:.2f})."
                )
            elif is_facing_bet and context.hand_strength < 0.50:
                return DecisionResult(
                    action=ActionType.FOLD,
                    confidence=0.85,
                    reasoning=f"Short stack ({context.stack_bb:.1f} BB) facing bet of {context.current_bet_bb:.1f} BB with insufficient hand strength ({context.hand_strength:.2f})."
                )

        # Rule 2: Premium / Monster hands (hand_strength >= 0.80)
        if context.hand_strength >= 0.80:
            if is_facing_bet:
                action = ActionType.ALL_IN if context.current_bet_bb >= context.stack_bb * 0.5 else ActionType.RAISE
                return DecisionResult(
                    action=action,
                    confidence=0.95,
                    reasoning=f"Monster hand (strength: {context.hand_strength:.2f}). Raising/shoving against incoming bet of {context.current_bet_bb:.1f} BB."
                )
            else:
                return DecisionResult(
                    action=ActionType.BET,
                    confidence=0.90,
                    reasoning=f"Very strong hand (strength: {context.hand_strength:.2f}). Betting for value against {context.opponents} opponent(s)."
                )

        # Rule 3: Medium / Speculative hands (0.45 <= hand_strength < 0.80)
        if 0.45 <= context.hand_strength < 0.80:
            if is_facing_bet:
                # Calculate pot odds vs hand strength
                pot_odds = context.current_bet_bb / (context.pot_bb + context.current_bet_bb) if (context.pot_bb + context.current_bet_bb) > 0 else 1.0
                if context.hand_strength >= pot_odds * 1.2:
                    return DecisionResult(
                        action=ActionType.CALL,
                        confidence=0.70,
                        reasoning=f"Hand strength ({context.hand_strength:.2f}) justifies call against bet of {context.current_bet_bb:.1f} BB with pot odds {pot_odds:.2f}."
                    )
                else:
                    return DecisionResult(
                        action=ActionType.FOLD,
                        confidence=0.65,
                        reasoning=f"Hand strength ({context.hand_strength:.2f}) insufficient for price offered by bet ({context.current_bet_bb:.1f} BB)."
                    )
            else:
                if context.position in ("BTN", "CO", "HJ") and context.hand_strength >= 0.55:
                    return DecisionResult(
                        action=ActionType.BET,
                        confidence=0.75,
                        reasoning=f"In position ({context.position}) with moderate strength ({context.hand_strength:.2f}). Betting for positional leverage."
                    )
                return DecisionResult(
                    action=ActionType.CHECK,
                    confidence=0.80,
                    reasoning=f"Checking moderate hand (strength: {context.hand_strength:.2f}) to realize equity risk-free."
                )

        # Rule 4: Weak hands (hand_strength < 0.45)
        if is_facing_bet:
            return DecisionResult(
                action=ActionType.FOLD,
                confidence=0.90,
                reasoning=f"Weak hand (strength: {context.hand_strength:.2f}) facing bet of {context.current_bet_bb:.1f} BB. Folding."
            )
        else:
            return DecisionResult(
                action=ActionType.CHECK,
                confidence=0.85,
                reasoning=f"Weak hand (strength: {context.hand_strength:.2f}) checked to. Checking back."
            )

    def calculate_risk(self, context: DecisionContext) -> float:
        """Calculates a normalized risk profile score between 0.0 (minimal risk) and 1.0 (extreme risk).
        
        Args:
            context: DecisionContext object describing the state.
            
        Returns:
            Float representing the normalized risk level.
        """
        # Risk increases with larger bets relative to stack, higher opponents count, and lower hand strength
        stack_commitment = min(1.0, context.current_bet_bb / max(1.0, context.stack_bb))
        opponent_risk = min(1.0, context.opponents / 8.0)
        equity_vulnerability = 1.0 - context.hand_strength

        # Stage multiplier: Late / Final Table stage elevates tournament life risk
        stage_weights = {
            "EARLY": 0.8,
            "MIDDLE": 1.0,
            "LATE": 1.2,
            "FINAL_TABLE": 1.4,
        }
        stage_mult = stage_weights.get(context.tournament_stage, 1.0)

        raw_risk = (stack_commitment * 0.5 + opponent_risk * 0.2 + equity_vulnerability * 0.3) * stage_mult
        return min(1.0, max(0.0, raw_risk))

    def explain_decision(self, context: DecisionContext) -> str:
        """Generates a detailed narrative text breakdown of the decision context and resulting evaluation.
        
        Args:
            context: DecisionContext object describing the state.
            
        Returns:
            Formatted explanatory string summarizing stack, position, hand strength, risk, and action.
        """
        result = self.evaluate(context)
        risk_score = self.calculate_risk(context)

        return (
            f"[ATHENA Decision Summary]\n"
            f"• Stage: {context.tournament_stage} | Street: {context.street} | Pos: {context.position}\n"
            f"• Stack: {context.stack_bb:.1f} BB | Pot: {context.pot_bb:.1f} BB | Facing Bet: {context.current_bet_bb:.1f} BB\n"
            f"• Hand Strength: {context.hand_strength:.2f} | Opponents: {context.opponents} | Calculated Risk: {risk_score:.2f}\n"
            f"• Recommended Action: {result.action.name} (Confidence: {result.confidence * 100:.0f}%)\n"
            f"• Rationale: {result.reasoning}"
        )