from athena.evaluation.model_manager import ModelManager



class MockModel:

    pass



def test_set_challenger():

    manager = ModelManager()


    model = MockModel()


    manager.set_challenger(
        model
    )


    assert manager.challenger is model



def test_promote_challenger():

    manager = ModelManager()


    model = MockModel()


    manager.set_challenger(
        model
    )


    champion = manager.promote()


    assert champion is model

    assert manager.challenger is None



def test_has_champion():

    manager = ModelManager()


    assert manager.has_champion() is False


    manager.promote if False else None