from athena.selfplay.demo_agents import create_demo_agents
from athena.selfplay.runner_service import SelfPlayRunnerService
from athena.selfplay.manager import SelfPlayManager


class SelfPlayGeneration:


    def __init__(
        self,
        runner=None,
        manager=None
    ):

        if runner is None:

            runner = SelfPlayRunnerService()


        self.runner = runner


        if manager is None:

            manager = SelfPlayManager(
                runner
            )


        self.manager = manager



    def run(
        self,
        agent_count=4
    ):

        agents = create_demo_agents(
            agent_count
        )


        results = self.runner.run_series(
            agents,
            rounds=1
        )


        return {
            "agents": agents,
            "matches": len(results),
            "results": results
        }