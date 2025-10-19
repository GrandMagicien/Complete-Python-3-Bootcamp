"""
Discord Training Load Bot

A bot that suggests mechanical/metabolic training load splits based on energy and sleep levels.
"""

import os
import discord
from discord import app_commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot token
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', None)

# Initialize the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def calculate_load_split(energy: int, sleep: int) -> tuple[int, int, str, list[str], str]:
    """
    Calculate the mechanical/metabolic load split based on energy and sleep levels.
    
    Args:
        energy: Energy level (1-5)
        sleep: Sleep level (1-5)
    
    Returns:
        Tuple of (mechanical_pct, metabolic_pct, workout_type, benefits, motto)
    """
    if energy >= 4 and sleep >= 4:
        # High energy and good sleep - go heavy
        mechanical, metabolic = 70, 30
        workout_type = "Lift Weights"
        benefits = [
            "Build maximum strength and muscle mass",
            "Take advantage of your peak recovery state",
            "Create adaptive stress for long-term gains"
        ]
        motto = "Strong today, stronger tomorrow! 💪"
    elif energy >= 3 and sleep >= 3:
        # Moderate energy and sleep - technical work
        mechanical, metabolic = 60, 40
        workout_type = "Technique Lift"
        benefits = [
            "Refine movement patterns with focused practice",
            "Build strength while managing fatigue wisely",
            "Develop skill and power simultaneously"
        ]
        motto = "Quality over quantity - perfect your craft! 🎯"
    elif energy <= 2 or sleep <= 2:
        # Low energy or poor sleep - active recovery
        mechanical, metabolic = 40, 60
        workout_type = "Swim or Aqua"
        benefits = [
            "Promote blood flow without excessive strain",
            "Support recovery through gentle movement",
            "Maintain fitness while respecting fatigue"
        ]
        motto = "Recovery is training too - trust the process! 🌊"
    else:
        # Balanced approach for mixed conditions
        mechanical, metabolic = 50, 50
        workout_type = "Balanced recovery"
        benefits = [
            "Maintain equilibrium between systems",
            "Adapt to your body's current needs",
            "Build resilience through varied stimulus"
        ]
        motto = "Balance is the key to consistency! ⚖️"
    
    return mechanical, metabolic, workout_type, benefits, motto


def format_message(energy: int, sleep: int, mechanical: int, metabolic: int, 
                   workout_type: str, benefits: list[str], motto: str) -> str:
    """
    Format the response message.
    
    Args:
        energy: Energy level
        sleep: Sleep level
        mechanical: Mechanical load percentage
        metabolic: Metabolic load percentage
        workout_type: Type of workout
        benefits: List of benefits
        motto: Motivational motto
    
    Returns:
        Formatted message string
    """
    benefits_text = "\n".join([f"• {benefit}" for benefit in benefits])
    
    message = f"""**Training Load Suggestion** 🏋️

Based on your inputs:
Energy Level: {energy}/5 ⚡
Sleep Quality: {sleep}/5 😴

**Suggested Mechanical/Metabolic Load Split: {mechanical}% / {metabolic}%**
Recommended Focus: **{workout_type}**

**Benefits:**
{benefits_text}

_{motto}_"""
    
    return message


async def rephrase_with_openai(message: str) -> str:
    """
    Optionally rephrase the message using OpenAI API to make it warmer.
    
    Args:
        message: Original message
    
    Returns:
        Rephrased message or original if API is not available
    """
    if not OPENAI_API_KEY:
        return message
    
    try:
        from openai import OpenAI
        
        openai_client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a warm, empathetic fitness coach. Rephrase the following training advice to be more encouraging and personal while keeping all the key information intact."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            max_tokens=400,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI rephrasing failed: {e}")
        return message


@tree.command(name="session", description="Get training load suggestions based on your energy and sleep levels")
@app_commands.describe(
    energy="Your current energy level (1-5, where 5 is highest)",
    sleep="Your sleep quality last night (1-5, where 5 is best)"
)
async def session(interaction: discord.Interaction, energy: int, sleep: int):
    """
    Slash command to get training load suggestions.
    
    Args:
        interaction: Discord interaction
        energy: Energy level (1-5)
        sleep: Sleep level (1-5)
    """
    # Validate inputs
    if not (1 <= energy <= 5):
        await interaction.response.send_message(
            "⚠️ Energy level must be between 1 and 5!", 
            ephemeral=True
        )
        return
    
    if not (1 <= sleep <= 5):
        await interaction.response.send_message(
            "⚠️ Sleep quality must be between 1 and 5!", 
            ephemeral=True
        )
        return
    
    # Calculate load split
    mechanical, metabolic, workout_type, benefits, motto = calculate_load_split(energy, sleep)
    
    # Format message
    message = format_message(energy, sleep, mechanical, metabolic, workout_type, benefits, motto)
    
    # Optionally rephrase with OpenAI
    if OPENAI_API_KEY:
        await interaction.response.defer()
        message = await rephrase_with_openai(message)
        await interaction.followup.send(message)
    else:
        await interaction.response.send_message(message)


@client.event
async def on_ready():
    """Event handler for when the bot is ready."""
    await tree.sync()
    print(f'{client.user} has connected to Discord!')
    print(f'Bot is ready to accept /session commands')


def main():
    """Main entry point for the bot."""
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN not found in environment variables. Please check your .env file.")
    
    client.run(TOKEN)


if __name__ == "__main__":
    main()
