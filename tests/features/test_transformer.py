from athena.features.transformer import FeatureTransformer


def test_feature_transformer():

    transformer = FeatureTransformer()

    result = transformer.transform(
        {
            "pot":100
        }
    )

    assert result["pot"] == 100
