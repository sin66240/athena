class PromotionPolicy:
    """
    Decide whether challenger should replace champion.
    """


    def __init__(
        self,
        minimum_gain=0.01
    ):

        self.minimum_gain = minimum_gain



    def should_promote(
        self,
        champion_score,
        challenger_score
    ):

        gain = (
            challenger_score - champion_score
        )


        return gain >= self.minimum_gain



    def evaluate(
        self,
        champion_score,
        challenger_score
    ):

        promote = self.should_promote(
            champion_score,
            challenger_score
        )


        return {
            "promote": promote,
            "gain": round(
                challenger_score - champion_score,
                10
            ),
            "minimum_gain": self.minimum_gain
        }