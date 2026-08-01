class PromotionService:
    """
    Handle challenger evaluation and promotion flow.
    """


    def __init__(
        self,
        evaluator,
        comparator,
        policy,
        manager
    ):

        self.evaluator = evaluator
        self.comparator = comparator
        self.policy = policy
        self.manager = manager



    def evaluate_and_promote(
        self,
        challenger
    ):

        champion = self.manager.champion



        # First model becomes champion
        if champion is None:

            self.manager.set_challenger(
                challenger
            )


            self.manager.promote()


            return {
                "promoted": True,
                "reason": "No champion"
            }



        champion_score = self.evaluator.evaluate(
            champion
        )


        challenger_score = self.evaluator.evaluate(
            challenger
        )



        comparison = self.comparator.compare(
            champion_score,
            challenger_score
        )



        decision = self.policy.evaluate(
            champion_score,
            challenger_score
        )



        if decision["promote"]:

            self.manager.set_challenger(
                challenger
            )


            self.manager.promote()


            return {
                "promoted": True,
                "reason": "Higher score",
                "comparison": comparison,
                "decision": decision
            }



        return {
            "promoted": False,
            "reason": "Insufficient improvement",
            "comparison": comparison,
            "decision": decision
        }
