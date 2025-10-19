"""
Unit tests for the Discord Training Load Bot

Tests the core logic for calculating load splits and formatting messages.
"""

import sys
import os

# Add the bot directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bot import calculate_load_split, format_message


def test_high_energy_high_sleep():
    """Test the load split for high energy and good sleep."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(4, 4)
    assert mechanical == 70
    assert metabolic == 30
    assert workout_type == "Lift Weights"
    assert len(benefits) == 3
    assert "💪" in motto
    print("✓ Test passed: High energy, high sleep")


def test_high_energy_high_sleep_edge():
    """Test the edge case for high energy and good sleep."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(5, 5)
    assert mechanical == 70
    assert metabolic == 30
    assert workout_type == "Lift Weights"
    print("✓ Test passed: Maximum energy and sleep")


def test_moderate_energy_moderate_sleep():
    """Test the load split for moderate energy and sleep."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(3, 3)
    assert mechanical == 60
    assert metabolic == 40
    assert workout_type == "Technique Lift"
    assert len(benefits) == 3
    assert "🎯" in motto
    print("✓ Test passed: Moderate energy, moderate sleep")


def test_low_energy():
    """Test the load split for low energy."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(2, 3)
    assert mechanical == 40
    assert metabolic == 60
    assert workout_type == "Swim or Aqua"
    assert len(benefits) == 3
    assert "🌊" in motto
    print("✓ Test passed: Low energy")


def test_low_sleep():
    """Test the load split for poor sleep."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(3, 2)
    assert mechanical == 40
    assert metabolic == 60
    assert workout_type == "Swim or Aqua"
    print("✓ Test passed: Low sleep")


def test_very_low_energy_and_sleep():
    """Test the load split for very low energy and poor sleep."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(1, 1)
    assert mechanical == 40
    assert metabolic == 60
    assert workout_type == "Swim or Aqua"
    print("✓ Test passed: Very low energy and sleep")


def test_balanced_recovery():
    """Test the balanced recovery case."""
    # energy=3, sleep=4 should trigger Technique Lift (energy >= 3 and sleep >= 3)
    # We need a case that doesn't match any of the first 3 rules
    # This doesn't actually exist in our logic since we cover all cases
    # So let's test a case that would be balanced: energy=2, sleep=4
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(2, 4)
    # This should trigger low energy rule (energy <= 2)
    assert mechanical == 40
    assert metabolic == 60
    assert workout_type == "Swim or Aqua"
    print("✓ Test passed: Low energy case (energy=2, sleep=4)")


def test_format_message():
    """Test that the message formatting works correctly."""
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(4, 4)
    message = format_message(4, 4, mechanical, metabolic, workout_type, benefits, motto)
    
    # Check that all key elements are in the message
    assert "Training Load Suggestion" in message
    assert "Energy Level: 4/5" in message
    assert "Sleep Quality: 4/5" in message
    assert "70% / 30%" in message
    assert "Lift Weights" in message
    assert "Benefits:" in message
    assert motto in message
    
    print("✓ Test passed: Message formatting")


def test_load_split_boundaries():
    """Test various boundary conditions for load splits."""
    # Test energy=4, sleep=3 (should be technique lift - energy >= 3 and sleep >= 3)
    mechanical, metabolic, workout_type, _, _ = calculate_load_split(4, 3)
    assert mechanical == 60 and metabolic == 40
    assert workout_type == "Technique Lift"
    
    # Test energy=3, sleep=4 (should be technique lift - energy >= 3 and sleep >= 3)
    mechanical, metabolic, workout_type, _, _ = calculate_load_split(3, 4)
    assert mechanical == 60 and metabolic == 40
    assert workout_type == "Technique Lift"
    
    # Test energy=2, sleep=4 (low energy should trigger swim/aqua)
    mechanical, metabolic, workout_type, _, _ = calculate_load_split(2, 4)
    assert mechanical == 40 and metabolic == 60
    assert workout_type == "Swim or Aqua"
    
    # Test energy=4, sleep=2 (low sleep should trigger swim/aqua)
    mechanical, metabolic, workout_type, _, _ = calculate_load_split(4, 2)
    assert mechanical == 40 and metabolic == 60
    assert workout_type == "Swim or Aqua"
    
    print("✓ Test passed: Load split boundaries")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*50)
    print("Running Discord Training Load Bot Tests")
    print("="*50 + "\n")
    
    try:
        test_high_energy_high_sleep()
        test_high_energy_high_sleep_edge()
        test_moderate_energy_moderate_sleep()
        test_low_energy()
        test_low_sleep()
        test_very_low_energy_and_sleep()
        test_balanced_recovery()
        test_format_message()
        test_load_split_boundaries()
        
        print("\n" + "="*50)
        print("All tests passed! ✓")
        print("="*50 + "\n")
        return True
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
