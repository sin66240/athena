from athena.cli.selfplay_cli import SelfPlayCLI


def test_status():

    cli = SelfPlayCLI()

    result = cli.status()

    assert "title" in result



def test_champion():

    cli = SelfPlayCLI()

    result = cli.champion()

    assert "champion" in result



def test_matches():

    cli = SelfPlayCLI()

    result = cli.matches()

    assert result["matches"] == 0
