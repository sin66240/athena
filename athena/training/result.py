class TrainingResult:

    def __init__(self, data=None):

        self.metrics = {}

        self.data = data or {}


        if isinstance(data, dict):

            if "metrics" in data:

                self.metrics = data["metrics"]

            else:

                self.metrics = data



    def __getitem__(self,key):

        return self.data[key]
