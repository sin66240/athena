from athena.features.version import FeatureVersion


def test_feature_version():

    version = FeatureVersion(
        "v1"
    )


    assert version.name == "v1"


    assert str(version) == "v1"
