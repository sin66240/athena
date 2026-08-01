from athena.app.main import AthenaApp


def test_create_app():

    app = AthenaApp()

    assert app is not None


def test_app_has_manager():

    app = AthenaApp()

    assert app.model_manager is not None