from athena.core.decision import (
    ActionType,
    DecisionContext,
    DecisionResult,
)


class PokerDecisionEngine:

    def evaluate(
        self,
        context: DecisionContext,
    ) -> DecisionResult:

        if context.hand_strength >= 0.90:

            return DecisionResult(

                action=ActionType.ALL_IN,

                confidence=0.95,

                reasoning="Premium hand."

            )

        if context.hand_strength >= 0.75:

            return DecisionResult(

                action=ActionType.RAISE,

                confidence=0.80,

                reasoning="Strong hand."

            )

        if context.hand_strength >= 0.50:

            return DecisionResult(

                action=ActionType.CALL,

                confidence=0.65,

                reasoning="Playable hand."

            )

        return DecisionResult(

            action=ActionType.FOLD,

            confidence=0.90,

            reasoning="Weak hand."

        )
