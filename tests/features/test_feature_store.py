from athena.features.feature_store import FeatureStore


def test_feature_store():

    store = FeatureStore()


    store.save(
        {
            "pot":100
        }
    )


    assert len(
        store.all()
    ) == 1
