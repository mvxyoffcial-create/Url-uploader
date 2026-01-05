import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API credentials
    APP_ID = int(os.environ.get("APP_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    
    # Database
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
    # Logging
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    
    # Owner
    OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
    
    # Session for user bot
    SESSION_STR = os.environ.get("SESSION_STR", "")
    
    # Update channel
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/zerodevbro")
    DEVELOPER = "@Zeroboy216"
    
    # Download/Upload settings
    MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4 GB
    SPEED_LIMIT = 500 * 1024 * 1024  # 500 MB/s
    CHUNK_SIZE = 2 * 1024 * 1024  # 2 MB chunks
    DOWNLOAD_DIR = "downloads"
    TORRENT_DOWNLOAD_PATH = "downloads/torrents"
    TORRENT_SEED_TIME = 0 
    
    # Messages
    START_MESSAGE = """ʜᴇʏ {name}**, 
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🚀
ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ ᴍᴏʀᴇ — ᴊᴜsᴛ ᴘᴀsᴛᴇ ᴀ ᴜʀʟ ᴏʀ ᴀ ᴍᴀɢɴᴇᴛ/ᴛᴏʀʀᴇɴᴛ ✨"""

    HELP_MESSAGE = """
**Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ** 🤔
   
𖣔 Fɪʀsᴛ ɢᴏ ᴛᴏ ᴛʜᴇ /settings ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙᴏᴛ ʙᴇʜᴀᴠɪᴏʀ ᴀs ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.

𖣔 Sᴇɴᴅ ᴍᴇ ᴛʜᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴀᴠᴇ ɪᴛ ᴘᴇʀᴍᴀɴᴇɴᴛʟʏ.

𖣔 **Sᴇɴᴅ ᴜʀʟ | Nᴇᴡ ɴᴀᴍᴇ.ᴍᴋᴠ**

𖣔 Sᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇsɪʀᴇᴅ ᴏᴘᴛɪᴏɴ.

𖣔 Usᴇ `/caption` ᴛᴏ sᴇᴛ ᴄᴀᴘᴛɪᴏɴ ᴀs Rᴇᴘʟʏ ᴛᴏ ᴍᴇᴅɪᴀ
"""

    ABOUT_MESSAGE = """
╭───────────⍟
├📛 **Mʏ Nᴀᴍᴇ** : URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ
├📢 **Fʀᴀᴍᴇᴡᴏʀᴋ** : <a href="https://docs.pyrogram.org/">PʏʀᴏBʟᴀᴄᴋ 2.7.4</a>
├💮 **Lᴀɴɢᴜᴀɢᴇ** : <a href="https://www.python.org">Pʏᴛʜᴏɴ 3.13.7</a>
├💾 **Dᴀᴛᴀʙᴀsᴇ** : <a href="https://cloud.mongodb.com">MᴏɴɢᴏDB</a>
├🚨 **Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ** : <a href="https://t.me/zerodevsupport"> Zᴇʀᴏ Sᴜᴘᴘᴏʀᴛ</a>
├🥏 **Cʜᴀɴɴᴇʟ** : <a href="https://t.me/zerodevbro"> Zᴇʀᴏ Dᴇᴠ </a>
├👨‍💻 **Cʀᴇᴀᴛᴇʀ** :  @Zeroboy216
├🧬 **Bᴜɪʟᴅ Sᴛᴀᴛᴜs** :  ᴠ1.4 [ ꜱᴛᴀʙʟᴇ ]
╰───────────────⍟
"""
