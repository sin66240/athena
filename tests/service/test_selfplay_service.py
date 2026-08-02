from athena.service.selfplay_service import SelfPlayService


def test_record_match():

    service = SelfPlayService()

    service.record_match(
        "model_a",
        "model_b"
    )

    assert service.get_total_matches() == 1



def test_champion():

    service = SelfPlayService()

    service.record_match(
        "model_a",
        "model_b"
    )

    service.record_match(
        "model_a",
        "model_c"
    )


    assert service.get_champion() == "model_a"



def test_dashboard_data():

    service = SelfPlayService()

    service.record_generation(1)


    data = service.get_dashboard_data()


    assert data["generations"] == 1
