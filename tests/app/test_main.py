from athena.app.main import AthenaApp


def test_create_app():

    app = AthenaApp()

    assert app is not None


def test_app_has_manager():

    app = AthenaApp()

    assert app.model_manager is not None


class MockChampion:
    pass


class MockStorage:

    def load(self):
        return MockChampion()


def test_app_loads_champion():

    app = AthenaApp()

    app.model_manager.storage = MockStorage()

    champion = app.load()

    assert champion is not None
    assert app.model_manager.has_champion()