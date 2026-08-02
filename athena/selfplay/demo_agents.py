class DemoAgent:


    def __init__(self, name):

        self.name = name



    def act(self, state=None):

        return "check"



    def __repr__(self):

        return self.name



def create_demo_agents(count=4):

    return [
        DemoAgent(
            f"agent_{i+1}"
        )
        for i in range(count)
    ]
