from athena.evaluation.model_manager import ModelManager



class MockModel:

    def __init__(self):

        self.name = "Champion"



class MockStorage:


    def load(self):

        return MockModel()



def test_load_champion():

    storage = MockStorage()


    manager = ModelManager(
        storage=storage
    )


    champion = manager.load_champion()


    assert champion.name == "Champion"

    assert manager.champion is champion