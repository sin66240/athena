from athena.evaluation.model_manager import ModelManager


class AthenaApp:
    """
    Main application controller.
    """

    def __init__(self):

        self.model_manager = ModelManager()

    def load(self):
        """
        Load champion model from storage if available.
        """

        storage = getattr(
            self.model_manager,
            "storage",
            None
        )

        if storage is None:
            return None

        champion = storage.load()

        if champion is not None:
            self.model_manager.champion = champion

        return champion