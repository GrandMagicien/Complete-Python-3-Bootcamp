# Discord Training Load Bot 🏋️

A Discord bot that provides personalized training load suggestions based on your energy and sleep levels. The bot helps you optimize your workout intensity by recommending mechanical vs. metabolic load splits.

## Features

- **Smart Load Calculations**: Get personalized mechanical/metabolic load splits based on your current state
- **Slash Commands**: Easy-to-use Discord slash command interface
- **Empathetic Responses**: Friendly, motivational messages with actionable benefits
- **OpenAI Integration (Optional)**: Warm, personalized message rephrasing using OpenAI API
- **Simple Setup**: Easy configuration with environment variables

## How It Works

The bot analyzes your energy and sleep levels (both on a scale of 1-5) and suggests an appropriate training split:

### Load Split Rules

| Condition | Mechanical | Metabolic | Workout Type |
|-----------|-----------|-----------|--------------|
| Energy ≥ 4 AND Sleep ≥ 4 | 70% | 30% | Lift Weights |
| Energy ≥ 3 AND Sleep ≥ 3 | 60% | 40% | Technique Lift |
| Energy ≤ 2 OR Sleep ≤ 2 | 40% | 60% | Swim or Aqua |
| Other combinations | 50% | 50% | Balanced recovery |

Each suggestion includes:
- Recommended load split percentage
- Workout focus type
- 3 key benefits
- Motivational motto

## Prerequisites

- Python 3.8 or higher
- A Discord Bot Token (see setup instructions below)
- (Optional) OpenAI API Key for enhanced responses

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/GrandMagicien/Complete-Python-3-Bootcamp.git
cd Complete-Python-3-Bootcamp/discord-training-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install discord.py python-dotenv openai
```

### 3. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section and click "Add Bot"
4. Under the "Token" section, click "Copy" to copy your bot token
5. Enable the following Privileged Gateway Intents:
   - Message Content Intent (optional, not required for slash commands)
6. Go to the "OAuth2" → "URL Generator" section
7. Select the following scopes:
   - `bot`
   - `applications.commands`
8. Select the following bot permissions:
   - Send Messages
   - Use Slash Commands
9. Copy the generated URL and open it in your browser to invite the bot to your server

### 4. Configure Environment Variables

Create a `.env` file in the `discord-training-bot` directory:

```bash
cp .env.example .env
```

Edit the `.env` file and add your Discord bot token:

```env
DISCORD_TOKEN=your_actual_discord_bot_token_here
```

**Optional:** If you want to use OpenAI for warmer message rephrasing, add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the Bot

```bash
python bot.py
```

You should see a message like:
```
YourBotName#1234 has connected to Discord!
Bot is ready to accept /session commands
```

## Usage

Once the bot is running and added to your Discord server, you can use the `/session` command:

```
/session energy:4 sleep:5
```

**Parameters:**
- `energy` (required): Your current energy level (1-5, where 5 is highest)
- `sleep` (required): Your sleep quality last night (1-5, where 5 is best)

### Example Responses

**High Energy & Good Sleep:**
```
Training Load Suggestion 🏋️

Based on your inputs:
Energy Level: 5/5 ⚡
Sleep Quality: 5/5 😴

Suggested Mechanical/Metabolic Load Split: 70% / 30%
Recommended Focus: Lift Weights

Benefits:
• Build maximum strength and muscle mass
• Take advantage of your peak recovery state
• Create adaptive stress for long-term gains

Strong today, stronger tomorrow! 💪
```

**Low Energy or Poor Sleep:**
```
Training Load Suggestion 🏋️

Based on your inputs:
Energy Level: 2/5 ⚡
Sleep Quality: 2/5 😴

Suggested Mechanical/Metabolic Load Split: 40% / 60%
Recommended Focus: Swim or Aqua

Benefits:
• Promote blood flow without excessive strain
• Support recovery through gentle movement
• Maintain fitness while respecting fatigue

Recovery is training too - trust the process! 🌊
```

## Project Structure

```
discord-training-bot/
├── bot.py              # Main bot implementation
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variable template
└── README.md          # This file
```

## Key Functions

### `calculate_load_split(energy, sleep)`
Determines the appropriate mechanical/metabolic split based on input parameters.

### `format_message(...)`
Creates a well-formatted Discord message with all relevant information.

### `rephrase_with_openai(message)`
Optionally rephrases the message using OpenAI API for a warmer tone.

### `/session` command
Discord slash command that takes energy and sleep parameters and returns training suggestions.

## Troubleshooting

### Bot doesn't respond to commands
- Make sure the bot has been invited with the `applications.commands` scope
- Wait a few minutes after starting the bot for commands to sync
- Try running `await tree.sync()` manually if needed

### "DISCORD_TOKEN not found" error
- Ensure your `.env` file exists in the same directory as `bot.py`
- Check that `DISCORD_TOKEN` is properly set in your `.env` file
- Make sure there are no extra spaces or quotes around the token

### OpenAI integration not working
- This is optional - the bot works fine without it
- If you want to use it, ensure `OPENAI_API_KEY` is set in your `.env` file
- Check that you have the `openai` package installed

## Security Notes

- **Never commit your `.env` file** to version control
- Keep your Discord token and API keys secret
- Use environment variables for all sensitive data
- The `.env` file is already excluded via `.gitignore`

## Contributing

This bot is part of the Complete Python 3 Bootcamp course materials. Feel free to fork and customize it for your own use!

## License

Copyright(©) by Pierian Data Inc.

## Credits

Created as part of the Complete Python 3 Bootcamp course on Udemy.
