from athena.features.schema import FeatureSchema


def test_feature_schema():

    schema = FeatureSchema()


    assert schema.version == "v1"


    assert "pot" in schema.features

    assert "player_count" in schema.features
