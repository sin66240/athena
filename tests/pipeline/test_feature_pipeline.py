from athena.pipeline.feature_pipeline import FeaturePipeline


class MockExtractor:

    def extract(
        self,
        data
    ):

        return {
            "pot": data["pot"]
        }



class MockTransformer:

    def transform(
        self,
        features
    ):

        features["transformed"] = True

        return features



class MockStore:

    def __init__(
        self
    ):

        self.saved = None



    def save(
        self,
        features
    ):

        self.saved = features

        return features



def test_feature_pipeline():


    store = MockStore()


    pipeline = FeaturePipeline(
        extractor=MockExtractor(),
        transformer=MockTransformer(),
        store=store
    )


    result = pipeline.run(
        {
            "pot":100
        }
    )


    assert result["pot"] == 100

    assert result["transformed"] is True

    assert store.saved == result
