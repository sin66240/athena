class ModelComparator:
    """
    Compare champion and challenger models.
    """


    def compare(
        self,
        champion_score,
        challenger_score=None
    ):

        # รองรับ evaluation dict จาก ModelEvaluator รุ่นใหม่
        if (
            challenger_score is None
            and isinstance(champion_score, dict)
        ):

            evaluation = champion_score

            if "champion_score" in evaluation:

                champion_score = evaluation["champion_score"]
                challenger_score = evaluation["challenger_score"]

            else:

                games = evaluation["games"]

                champion_score = (
                    evaluation["champion_wins"] / games
                )

                challenger_score = (
                    evaluation["challenger_wins"] / games
                )


        if challenger_score > champion_score:

            return {
                "winner": "challenger",
                "promote": True,
                "difference": round(
                    challenger_score - champion_score,
                    10
                )
            }


        return {
            "winner": "champion",
            "promote": False,
            "difference": round(
                champion_score - challenger_score,
                10
            )
        }