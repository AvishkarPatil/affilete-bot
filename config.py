from decouple import config
import sys
import logging

logger = logging.getLogger(__name__)

class Config:
    # Telegram API credentials
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    SESSION = config("SESSION")
    
    # Channel configuration
    FROM_CHANNELS = []
    TO_CHANNELS = []
    
    # Footer configuration
    FOOTER_TEXT = config("FOOTER_TEXT", default="")
    ADD_FOOTER = config("ADD_FOOTER", default=False, cast=bool)
    
    @classmethod
    def validate_and_load(cls):
        """Validate and load configuration"""
        required_vars = ['APP_ID', 'API_HASH', 'SESSION', 'FROM_CHANNEL', 'TO_CHANNEL']
        missing = []
        
        for var in required_vars:
            if not config(var, default=None):
                missing.append(var)
        
        if missing:
            logger.error(f"Missing required environment variables: {', '.join(missing)}")
            sys.exit(1)
        
        # Parse channels
        cls.FROM_CHANNELS = cls._parse_channels(config("FROM_CHANNEL"))
        cls.TO_CHANNELS = cls._parse_channels(config("TO_CHANNEL"))
        
        logger.info(f"Configured to forward from {len(cls.FROM_CHANNELS)} to {len(cls.TO_CHANNELS)} channels")
        
        if cls.ADD_FOOTER and cls.FOOTER_TEXT:
            logger.info(f"Footer enabled: {cls.FOOTER_TEXT}")
    
    @staticmethod
    def _parse_channels(channel_str):
        """Parse channel IDs from string"""
        try:
            return [int(ch.strip()) for ch in channel_str.split() if ch.strip()]
        except ValueError as e:
            logger.error(f"Invalid channel ID format: {e}")
            sys.exit(1)