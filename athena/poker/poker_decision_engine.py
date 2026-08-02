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

        # Premium hand

        if context.hand_strength >= 0.90:

            if context.stack_bb <= 15:

                return DecisionResult(
                    action=ActionType.ALL_IN,
                    confidence=0.95,
                    reasoning="Premium hand with short stack.",
                )

            return DecisionResult(
                action=ActionType.RAISE,
                confidence=0.90,
                reasoning="Premium hand with deep stack.",
            )

        # Strong hand

        if context.hand_strength >= 0.75:

            if context.position in ["CO", "BTN"]:

                return DecisionResult(
                    action=ActionType.RAISE,
                    confidence=0.85,
                    reasoning="Strong hand in late position.",
                )

            return DecisionResult(
                action=ActionType.CALL,
                confidence=0.70,
                reasoning="Strong hand in early position.",
            )

        # Playable hand

        if context.hand_strength >= 0.50:

            if context.stack_bb <= 10:

                return DecisionResult(
                    action=ActionType.ALL_IN,
                    confidence=0.75,
                    reasoning="Playable hand in push-fold zone.",
                )

            if context.position in ["CO", "BTN"]:

                return DecisionResult(
                    action=ActionType.CALL,
                    confidence=0.65,
                    reasoning="Playable hand in late position.",
                )

        # Weak hand

        return DecisionResult(
            action=ActionType.FOLD, confidence=0.90, reasoning="Weak hand."
        )
