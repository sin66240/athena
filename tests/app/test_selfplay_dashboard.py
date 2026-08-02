from athena.app.selfplay_dashboard import SelfPlayDashboard


def test_dashboard_overview():

    dashboard = SelfPlayDashboard()

    result = dashboard.overview()

    assert result["title"] == "ATHENA SelfPlay Dashboard"



def test_match_count():

    dashboard = SelfPlayDashboard()

    assert dashboard.match_count() == 0



def test_champion_status():

    dashboard = SelfPlayDashboard()

    result = dashboard.champion_status()

    assert "champion" in result
