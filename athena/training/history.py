class TrainingHistory:
    """
    Stores training metrics over time.
    """


    def __init__(self):

        self.records = []



    def add(
        self,
        epoch,
        metrics
    ):

        self.records.append(
            {
                "epoch": epoch,
                "metrics": metrics
            }
        )



    def latest(self):

        if not self.records:
            return None

        return self.records[-1]
