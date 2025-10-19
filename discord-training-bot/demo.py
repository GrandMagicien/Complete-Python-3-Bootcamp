#!/usr/bin/env python3
"""
Demo script to test the Discord Training Load Bot logic without connecting to Discord.

This script simulates the /session command by directly calling the bot's functions.
"""

from bot import calculate_load_split, format_message


def demo_session(energy: int, sleep: int):
    """
    Demonstrate a session command with given energy and sleep values.
    
    Args:
        energy: Energy level (1-5)
        sleep: Sleep level (1-5)
    """
    print(f"\n{'='*60}")
    print(f"Simulating: /session energy:{energy} sleep:{sleep}")
    print('='*60)
    
    # Validate inputs
    if not (1 <= energy <= 5):
        print("⚠️ Energy level must be between 1 and 5!")
        return
    
    if not (1 <= sleep <= 5):
        print("⚠️ Sleep quality must be between 1 and 5!")
        return
    
    # Calculate load split
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(energy, sleep)
    
    # Format message
    message = format_message(energy, sleep, mechanical, metabolic, workout_type, benefits, motto)
    
    # Display the message
    print(message)
    print('='*60)


def main():
    """Run demo scenarios."""
    print("\n🏋️ Discord Training Load Bot - Demo Mode 🏋️\n")
    print("This demo shows how the bot responds to different energy/sleep combinations.\n")
    
    # Demo scenario 1: High energy and great sleep
    demo_session(5, 5)
    
    # Demo scenario 2: Moderate energy and sleep
    demo_session(3, 3)
    
    # Demo scenario 3: Low energy
    demo_session(2, 3)
    
    # Demo scenario 4: Mixed conditions
    demo_session(4, 3)
    
    print("\n" + "="*60)
    print("Demo complete!")
    print("="*60 + "\n")
    print("To run the actual bot with Discord:")
    print("1. Create a .env file with your DISCORD_TOKEN")
    print("2. Run: python bot.py")
    print("3. Use /session command in your Discord server\n")


if __name__ == "__main__":
    main()
