import pytest
from athena.core.betting import Action, BettingAction, BettingEngine


def test_create_betting_action() -> None:
    """Test creating valid betting actions."""
    action_fold = BettingAction(player_id="p1", action=Action.FOLD)
    assert action_fold.player_id == "p1"
    assert action_fold.action == Action.FOLD
    assert action_fold.amount == 0

    action_bet = BettingAction(player_id="p2", action=Action.BET, amount=100)
    assert action_bet.action == Action.BET
    assert action_bet.amount == 100


def test_betting_action_validation() -> None:
    """Test validation rules for BettingAction."""
    # Test empty player_id
    with pytest.raises(ValueError, match="player_id is required"):
        BettingAction(player_id="", action=Action.FOLD)

    # Test negative amount
    with pytest.raises(ValueError, match="cannot be negative"):
        BettingAction(player_id="p1", action=Action.BET, amount=-50)

    # Test FOLD with amount > 0
    with pytest.raises(ValueError, match="must have an amount of 0"):
        BettingAction(player_id="p1", action=Action.FOLD, amount=10)

    # Test CHECK with amount > 0
    with pytest.raises(ValueError, match="must have an amount of 0"):
        BettingAction(player_id="p1", action=Action.CHECK, amount=20)


def test_fold_action() -> None:
    """Test that folding does not alter the pot or bets."""
    engine = BettingEngine(pot=100, current_bet=50, minimum_raise=50)
    engine.contributions["p1"] = 50

    action = BettingAction(player_id="p2", action=Action.FOLD)
    engine.apply_action(action)

    # Ensure state remains unchanged
    assert engine.pot == 100
    assert engine.current_bet == 50
    assert engine.get_player_contribution("p2") == 0


def test_call_calculation_and_action() -> None:
    """Test calculating call amounts and applying CALL actions."""
    engine = BettingEngine(minimum_raise=20)
    
    # Player 1 Bets 50
    engine.apply_action(BettingAction(player_id="p1", action=Action.BET, amount=50))
    
    # Player 2 needs to call 50
    assert engine.calculate_call_amount("p2") == 50
    
    # Player 2 Calls 50
    engine.apply_action(BettingAction(player_id="p2", action=Action.CALL, amount=50))
    
    assert engine.pot == 100
    assert engine.get_player_contribution("p2") == 50

    # Test calling incorrect amount
    with pytest.raises(ValueError, match="CALL amount must exactly match"):
        engine.apply_action(BettingAction(player_id="p3", action=Action.CALL, amount=30))


def test_raise_handling() -> None:
    """Test betting and raising mechanics, including minimum raise calculations."""
    engine = BettingEngine(minimum_raise=20) # Big Blind size
    
    # Valid BET
    engine.apply_action(BettingAction(player_id="p1", action=Action.BET, amount=20))
    assert engine.current_bet == 20
    assert engine.minimum_raise == 20
    
    # Invalid RAISE (less than min raise)
    with pytest.raises(ValueError, match="must total at least 40"):
        # p2 wants to raise, but only adds 30 total (current_bet 20 + min_raise 20 = 40 needed)
        engine.apply_action(BettingAction(player_id="p2", action=Action.RAISE, amount=30))

    # Valid RAISE
    engine.apply_action(BettingAction(player_id="p2", action=Action.RAISE, amount=60))
    assert engine.current_bet == 60
    assert engine.minimum_raise == 40  # Raised by 40 (60 - 20)
    
    # Player 1 Re-raises
    # Needs to total at least current_bet (60) + min_raise (40) = 100.
    # Player 1 already has 20 in, so they need to add 80.
    engine.apply_action(BettingAction(player_id="p1", action=Action.RAISE, amount=80))
    assert engine.current_bet == 100
    assert engine.pot == 160


def test_all_in_handling() -> None:
    """Test ALL_IN actions, specifically handling partial raises."""
    engine = BettingEngine(minimum_raise=50)
    
    # P1 Bets 100
    engine.apply_action(BettingAction(player_id="p1", action=Action.BET, amount=100))
    
    # P2 goes ALL_IN for 120 (adds 120)
    # This is a raise of 20, which is less than the min raise of 100
    engine.apply_action(BettingAction(player_id="p2", action=Action.ALL_IN, amount=120))
    
    assert engine.current_bet == 120
    assert engine.minimum_raise == 100  # Min raise doesn't change because it was a "short" all-in
    assert engine.pot == 220

    # P3 goes ALL_IN for 300
    engine.apply_action(BettingAction(player_id="p3", action=Action.ALL_IN, amount=300))
    
    assert engine.current_bet == 300
    assert engine.minimum_raise == 180  # Full raise (300 - 120), so min raise updates
    assert engine.pot == 520


def test_pot_calculation_and_contributions() -> None:
    """Test that pot and player contributions are accurately tracked."""
    engine = BettingEngine(minimum_raise=10)
    
    engine.apply_action(BettingAction(player_id="p1", action=Action.BET, amount=100))
    engine.apply_action(BettingAction(player_id="p2", action=Action.CALL, amount=100))
    
    assert engine.get_player_contribution("p1") == 100
    assert engine.get_player_contribution("p2") == 100
    assert engine.get_player_contribution("p3") == 0  # No contribution yet
    assert engine.pot == 200


def test_reset_round() -> None:
    """Test resetting the betting round for the next street."""
    engine = BettingEngine(pot=500, current_bet=100, minimum_raise=50)
    engine.contributions = {"p1": 100, "p2": 100}

    # Reset for the Flop, Big Blind is 20
    engine.reset_round(initial_minimum_raise=20)

    # Pot should remain
    assert engine.pot == 500
    
    # Bets and contributions should clear
    assert engine.current_bet == 0
    assert engine.minimum_raise == 20
    assert len(engine.contributions) == 0
    assert engine.get_player_contribution("p1") == 0