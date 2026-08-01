class DatasetValidator:
    """
    Validate dataset quality.
    """


    def validate(
        self,
        data
    ):

        if data is None:

            return False


        if len(data) == 0:

            return False


        return True
