# Telegram Auto-Forward Bot

A reliable Telegram bot that automatically forwards messages from source channels to destination channels with improved error handling and logging.

## Features
- Forward messages from multiple source channels to multiple destination channels
- Preserves message formatting, captions, and reply markup
- Comprehensive error handling and logging
- Configuration validation
- Support for both single and multiple channel forwarding

## Setup

### 1. Get Telegram API Credentials
- Visit [my.telegram.org](https://my.telegram.org)
- Create a new application to get `APP_ID` and `API_HASH`

### 2. Generate Session String
- Use this [Colab notebook](https://colab.research.google.com/drive/1wjYvtwUo5zDsUvukyafAR9Of-2NYkKsu) to generate your session string

### 3. Configure Environment Variables
Edit `config.env` file:
```
APP_ID=your_app_id
API_HASH=your_api_hash
SESSION=your_session_string
FROM_CHANNEL=-1001234567890 -1001234567891
TO_CHANNEL=-1001234567892 -1001234567893
ADD_FOOTER=True
FOOTER_TEXT=📢 Forwarded by MyBot
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Bot
```bash
python bot.py
```

## Configuration
- `FROM_CHANNEL`: Source channel IDs separated by spaces
- `TO_CHANNEL`: Destination channel IDs separated by spaces
- `ADD_FOOTER`: Enable/disable custom footer (True/False)
- `FOOTER_TEXT`: Custom text added to forwarded messages
- Both channels support single or multiple IDs

## Getting Channel IDs
1. Forward a message from the channel to [@userinfobot](https://t.me/userinfobot)
2. The bot will show the channel ID
3. Use the ID with the minus sign (e.g., -1001234567890)

## Deployment
The bot includes configuration for:
- Heroku (Procfile)
- Render (render.yml)
- Local development

## Credits
- Original concept by [LmaoDED](https://github.com/LimbuSoda)
- Enhanced with improved error handling and multi-channel support
