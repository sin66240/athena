class FeaturePipeline:
    """
    Orchestrates feature generation flow.
    """


    def __init__(
        self,
        extractor,
        transformer,
        store
    ):

        self.extractor = extractor

        self.transformer = transformer

        self.store = store



    def run(
        self,
        data
    ):


        features = self.extractor.extract(
            data
        )


        features = self.transformer.transform(
            features
        )


        self.store.save(
            features
        )


        return features
