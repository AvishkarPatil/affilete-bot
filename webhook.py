from flask import Flask, request
from config import Config
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle webhook updates"""
    try:
        update = request.get_json()
        logger.info(f"Received webhook update: {update}")
        return "OK", 200
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return "Error", 500

if __name__ == "__main__":
    Config.validate_and_load()
    app.run(host="0.0.0.0", port=Config.PORT, debug=False)