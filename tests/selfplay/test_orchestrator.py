from athena.selfplay.orchestrator import (
    SelfPlayOrchestrator
)



class Dummy:

    pass



def test_create_cycle():

    manager = SelfPlayOrchestrator(
        Dummy(),
        Dummy(),
        Dummy(),
        Dummy()
    )


    cycle = manager.create_cycle(
        1
    )


    assert cycle.generation == 1
    assert cycle.status == "created"



def test_cycle_flow():

    manager = SelfPlayOrchestrator(
        Dummy(),
        Dummy(),
        Dummy(),
        Dummy()
    )


    cycle = manager.create_cycle(
        5
    )


    manager.run_cycle(cycle)


    assert cycle.status == "running"



    manager.complete_cycle(cycle)


    assert cycle.status == "completed"



def test_latest_cycle():

    manager = SelfPlayOrchestrator(
        Dummy(),
        Dummy(),
        Dummy(),
        Dummy()
    )


    manager.create_cycle(10)


    assert manager.latest_cycle().generation == 10
