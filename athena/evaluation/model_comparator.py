class ModelComparator:
    """
    Compare champion and challenger models.
    """


    def compare(
        self,
        champion_score,
        challenger_score
    ):

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