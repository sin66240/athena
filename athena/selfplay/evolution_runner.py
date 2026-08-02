class EvolutionRunner:

    def __init__(self):
        self.history = []

    def run_generation(self, generation):

        result = {
            "generation": generation,
            "status": "completed"
        }

        self.history.append(result)

        return result

    def get_history(self):

        return self.history
