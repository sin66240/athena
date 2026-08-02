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



        # Support both old and new evaluator
        try:

            evaluation = self.evaluator.evaluate(
                champion,
                challenger
            )


        except TypeError:

            champion_score = self.evaluator.evaluate(
                champion
            )


            challenger_score = self.evaluator.evaluate(
                challenger
            )


            evaluation = {

                "champion_score": champion_score,

                "challenger_score": challenger_score

            }



        # Compare result
        comparison = self.comparator.compare(
            evaluation
        )



        # Support both old and new policy
        if "games" in evaluation:

            decision = self.policy.evaluate_match_result(
                evaluation
            )


        else:

            decision = self.policy.evaluate(
                evaluation["champion_score"],
                evaluation["challenger_score"]
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