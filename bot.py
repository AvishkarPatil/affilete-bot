from pyrogram import Client, filters
from config import Config
import logging
import asyncio
import sys

try:
    import uvloop
    uvloop.install()
except ImportError:
    pass

logging.basicConfig(
    format='[%(levelname)s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load and validate configuration
Config.validate_and_load()

try:
    client = Client(
        name="forwarder_bot",
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        session_string=Config.SESSION
    )
except Exception as e:
    logger.error(f"Failed to initialize client: {e}")
    sys.exit(1)

async def start_bot():
    """Start the bot and keep it running"""
    try:
        await client.start()
        user = await client.get_me()
        logger.info(f"Bot started successfully as: {user.first_name} (@{user.username})")
        await asyncio.Event().wait()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        sys.exit(1)

def add_footer_to_caption(original_caption):
    """Add custom footer to message caption"""
    if not Config.ADD_FOOTER or not Config.FOOTER_TEXT:
        return original_caption
    
    footer = f"\n\n{Config.FOOTER_TEXT}"
    if original_caption:
        return original_caption + footer
    return Config.FOOTER_TEXT

@client.on_message(filters.chat(Config.FROM_CHANNELS))
async def forward_message(client, message):
    """Forward messages from source to destination channels"""
    success_count = 0
    
    # Prepare caption with footer
    new_caption = add_footer_to_caption(message.caption)
    
    for to_channel in Config.TO_CHANNELS:
        try:
            await client.copy_message(
                chat_id=to_channel,
                from_chat_id=message.chat.id,
                message_id=message.id,
                caption=new_caption,
                caption_entities=message.caption_entities,
                reply_markup=message.reply_markup
            )
            success_count += 1
        except Exception as e:
            logger.error(f"Failed to forward to {to_channel}: {e}")
    
    if success_count > 0:
        logger.info(f"Forwarded message to {success_count}/{len(Config.TO_CHANNELS)} channels")

if __name__ == "__main__":
    logger.info("Starting Auto-Post Bot...")
    client.run(start_bot())
