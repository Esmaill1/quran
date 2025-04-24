# Quran FM Discord Bot

A simple Discord bot that streams Quran FM radio to your Discord voice channels. This bot allows users to listen to Quran recitations and Islamic content together in voice channels.

## Features

- Stream Quran FM radio to Discord voice channels
- Simple commands to control the bot
- Easy setup and deployment

## Requirements

- Python 3.8 or higher
- discord.py library
- FFmpeg installed on your system
- Discord Bot Token

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/quran-fm-discord-bot.git
   cd quran-fm-discord-bot
   ```

2. Install the required Python packages:
   ```
   pip install discord.py pynacl
   ```

3. Install FFmpeg:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add it to your PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` or equivalent for your distribution

4. Create a `.env` file in the project directory and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

## Setting Up Your Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Navigate to the "Bot" tab and click "Add Bot"
4. Under the "Privileged Gateway Intents" section, enable "Message Content Intent"
5. Copy your bot token and paste it in the `.env` file or directly in the code
6. Go to the "OAuth2" tab, select "bot" under "scopes" and select the following permissions:
   - View Channels
   - Send Messages
   - Connect
   - Speak
7. Use the generated URL to invite the bot to your server

## Usage

1. Start the bot:
   ```
   python bot.py
   ```

2. Use the following commands in your Discord server:
   - `!join` - Bot joins your current voice channel and starts playing Quran FM
   - `!leave` - Bot leaves the voice channel

## Customization

You can change the radio stream URL by modifying the `STREAM_URL` variable in the code:

```python
STREAM_URL = "https://stream.radiojar.com/0tpy1h0kxtzuv"  # Replace with your preferred Islamic radio stream
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py) - The Discord API wrapper for Python
- [Quran FM](https://quranfm.com/) - For providing the radio stream

## Disclaimer

This bot is intended for educational and personal use only. Always respect Discord's Terms of Service and Community Guidelines when using this bot.
