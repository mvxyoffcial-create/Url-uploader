import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API credentials
    APP_ID = int(os.environ.get("APP_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Urluploader_z_bot")
    
    # Database
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
    # Logging & Owner
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    
    # Settings
    SESSION_STR = os.environ.get("SESSION_STR", "")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/zerodevbro")
    DEVELOPER = "@Zeroboy216"
    
    # Download/Upload settings
    MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024 
    SPEED_LIMIT = 500 * 1024 * 1024 
    CHUNK_SIZE = 2 * 1024 * 1024 
    DOWNLOAD_DIR = "downloads"
    TORRENT_DOWNLOAD_PATH = "downloads/torrents"
    TORRENT_SEED_TIME = 0 
    
    # Messages
    START_MESSAGE = """ʜᴇʏ {name}**, 
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🚀"""

    HELP_MESSAGE = """**Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ** 🤔
𖣔 Send url | New name.mkv"""

    ABOUT_MESSAGE = """╭───────────⍟
├📛 **Mʏ Nᴀᴍᴇ** : URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ
├📢 **Framework** : PyroBlack
├🧬 **Build Status** : v1.4 [ Stable ]
╰───────────────⍟"""
