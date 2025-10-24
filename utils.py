import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

def format_channel_list(channels: List[int]) -> str:
    """Format channel list for logging"""
    return ", ".join([str(ch) for ch in channels])

def sanitize_text(text: Optional[str], max_length: int = 4096) -> Optional[str]:
    """Sanitize and truncate text to fit Telegram limits"""
    if not text:
        return text
    
    if len(text) > max_length:
        logger.warning(f"Text truncated from {len(text)} to {max_length} characters")
        return text[:max_length-3] + "..."
    
    return text

def get_channel_info(channel_id: int) -> str:
    """Get formatted channel info for logging"""
    return f"Channel {channel_id}"