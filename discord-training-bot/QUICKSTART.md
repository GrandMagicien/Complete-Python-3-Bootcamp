# Quick Start Guide

## Installation (5 minutes)

```bash
# 1. Navigate to the bot directory
cd discord-training-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
cp .env.example .env
# Edit .env and add your DISCORD_TOKEN

# 4. Run the bot
python bot.py
```

## Testing Without Discord

```bash
# Run the demo to see how it works
python demo.py

# Run unit tests
python test_bot.py
```

## Using in Discord

Once the bot is running and invited to your server:

```
/session energy:5 sleep:5
```

## Load Split Quick Reference

| Your State | Energy | Sleep | Mechanical | Metabolic | Workout |
|------------|--------|-------|-----------|-----------|---------|
| 🔥 Peak Performance | 4-5 | 4-5 | 70% | 30% | Lift Weights |
| ⚙️ Good & Ready | 3 | 3-5 | 60% | 40% | Technique Lift |
| 🌊 Need Recovery | 1-2 | any | 40% | 60% | Swim or Aqua |
| 😴 Poor Sleep | any | 1-2 | 40% | 60% | Swim or Aqua |

## Troubleshooting

**Bot not responding?**
- Check DISCORD_TOKEN in .env
- Ensure bot has proper permissions
- Wait a few minutes for commands to sync

**Want OpenAI warmth?**
- Add OPENAI_API_KEY to .env
- This is optional - bot works without it!

## Files

- `bot.py` - Main bot code
- `demo.py` - Test without Discord
- `test_bot.py` - Unit tests
- `README.md` - Full documentation
- `.env.example` - Configuration template

Need help? Check README.md for detailed instructions!
