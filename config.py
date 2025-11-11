import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram API credentials
    APP_ID = int(os.environ.get("APP_ID", "20288994"))
    API_HASH = os.environ.get("API_HASH", "d702614912f1ad370a0d18786002adbf")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8062010233:AAExAW3Z-kpT17OTUXg0GQkCVsc7qnDUbXQ")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Urluploader_z_bot")
    
    # Database
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://moviedatabase:venura%408907@cluster0.hg0etvt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    # Logging
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002897456594"))
    
    # Owner
    OWNER_ID = int(os.environ.get("OWNER_ID", "8304706556"))
    
    # Session for user bot (if needed)
    SESSION_STR = os.environ.get("SESSION_STR", "")
    
    # Update channel
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "https://t.me/zerodevbro")
    DEVELOPER = "@Zeroboy216"
    
    # Download/Upload settings
    MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4 GB
    SPEED_LIMIT = 500 * 1024 * 1024  # 500 MB/s (SUPER FAST!)
    CHUNK_SIZE = 2 * 1024 * 1024  # 2 MB chunks for maximum speed
    
    # Download directory
    DOWNLOAD_DIR = "downloads"
    
    # Torrent settings
    TORRENT_DOWNLOAD_PATH = "downloads/torrents"
    TORRENT_SEED_TIME = 0  # Don't seed after download
    
    # Welcome message
    START_MESSAGE = """ʜᴇʏ {name}**, 
ɪ ᴀᴍ ᴛʜᴇ ᴍᴏsᴛ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🚀
ɪ ᴄᴀɴ ᴜᴘʟᴏᴀᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ ᴍᴏʀᴇ — ᴊᴜsᴛ ᴘᴀsᴛᴇ ᴀ ᴜʀʟ ᴏʀ ᴀ ᴍᴀɢɴᴇᴛ/ᴛᴏʀʀᴇɴᴛ ✨"""

    HELP_MESSAGE = """**📚 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅs**

**🔗 Sᴜᴘᴘᴏʀᴛᴇᴅ Lɪɴᴋs:**
• Dɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅs (HTTP/HTTPS)
• YᴏᴜTᴜʙᴇ ᴠɪᴅᴇᴏs (ᴜᴘ ᴛᴏ 4K)
• Iɴsᴛᴀɢʀᴀᴍ ᴘᴏsᴛs & ʀᴇᴇʟs
• TɪᴋTᴏᴋ ᴠɪᴅᴇᴏs
• Fᴀᴄᴇʙᴏᴏᴋ ᴠɪᴅᴇᴏs
• Tᴡɪᴛᴛᴇʀ/X ᴠɪᴅᴇᴏs
• Vɪᴍᴇᴏ, Dᴀɪʟʏᴍᴏᴛɪᴏɴ
• Tᴏʀʀᴇɴᴛ ғɪʟᴇs (.ᴛᴏʀʀᴇɴᴛ)
• Mᴀɢɴᴇᴛ ʟɪɴᴋs

**⚙️ Cᴏᴍᴍᴀɴᴅs:**
/sᴛᴀʀᴛ - Sᴛᴀʀᴛ ʙᴏᴛ & sʜᴏᴡ ᴍᴇɴᴜ
/ʜᴇʟᴘ - Sʜᴏᴡ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ
/ʀᴇɴᴀᴍᴇ - Rᴇɴᴀᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ғɪʟᴇ
/sᴇᴛᴛɪɴɢs - Bᴏᴛ sᴇᴛᴛɪɴɢs
/sᴛᴀᴛᴜs - Yᴏᴜʀ sᴛᴀᴛɪsᴛɪᴄs
/ᴀʙᴏᴜᴛ - Aʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ

**💡 Tɪᴘs:**
• Sᴇɴᴅ URL ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ
• Sᴇɴᴅ .ᴛᴏʀʀᴇɴᴛ ғɪʟᴇ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛᴏʀʀᴇɴᴛ
• Sᴇɴᴅ ᴍᴀɢɴᴇᴛ ʟɪɴᴋ ғᴏʀ ᴛᴏʀʀᴇɴᴛ ᴅᴏᴡɴʟᴏᴀᴅ
• Oʀɪɢɪɴᴀʟ ǫᴜᴀʟɪᴛʏ ᴘʀᴇsᴇʀᴠᴇᴅ (ɴᴏ ᴄᴏᴍᴘʀᴇssɪᴏɴ)
• Fᴀsᴛ 500 MB/s sᴘᴇᴇᴅ ⚡

**🎬 Vɪᴅᴇᴏ Qᴜᴀʟɪᴛʏ:**
✅ Oʀɪɢɪɴᴀʟ ʀᴇsᴏʟᴜᴛɪᴏɴ (720ᴘ, 1080ᴘ, 4K)
✅ Oʀɪɢɪɴᴀʟ ᴀᴜᴅɪᴏ (AAC 320ᴋʙᴘs)
✅ Oʀɪɢɪɴᴀʟ ғʀᴀᴍᴇ ʀᴀᴛᴇ (24ғᴘs, 30ғᴘs, 60ғᴘs)
✅ Sᴛʀᴇᴀᴍɪɴɢ sᴜᴘᴘᴏʀᴛ ᴇɴᴀʙʟᴇᴅ

**📞 Sᴜᴘᴘᴏʀᴛ:**
**Dᴇᴠᴇʟᴏᴘᴇʀ:** {dev}
**Uᴘᴅᴀᴛᴇs:** {channel}"""

    ABOUT_MESSAGE = """**ℹ️ Aʙᴏᴜᴛ URL Uᴘʟᴏᴀᴅᴇʀ Bᴏᴛ**

**📦 Vᴇʀsɪᴏɴ:** 3.0 Pʀᴏ
**⚡ Sᴘᴇᴇᴅ:** 500 MB/s
**💾 Mᴀx Sɪᴢᴇ:** 4 GB
**🎬 Qᴜᴀʟɪᴛʏ:** Oʀɪɢɪɴᴀʟ (Nᴏ ᴄᴏᴍᴘʀᴇssɪᴏɴ)

**✨ Fᴇᴀᴛᴜʀᴇs:**
✅ Dɪʀᴇᴄᴛ URL ᴅᴏᴡɴʟᴏᴀᴅs
✅ YᴏᴜTᴜʙᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅs (4K)
✅ Iɴsᴛᴀɢʀᴀᴍ, TɪᴋTᴏᴋ sᴜᴘᴘᴏʀᴛ
✅ Tᴏʀʀᴇɴᴛ & ᴍᴀɢɴᴇᴛ ʟɪɴᴋs
✅ Cᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟs & ᴄᴀᴘᴛɪᴏɴs
✅ Aᴜᴛᴏ ғɪʟᴇ ᴛʏᴘᴇ ᴅᴇᴛᴇᴄᴛɪᴏɴ
✅ Pʀᴏɢʀᴇss ᴛʀᴀᴄᴋɪɴɢ ᴡɪᴛʜ ETA
✅ Oʀɪɢɪɴᴀʟ ǫᴜᴀʟɪᴛʏ ᴘʀᴇsᴇʀᴠᴀᴛɪᴏɴ
✅ Sᴛʀᴇᴀᴍɪɴɢ sᴜᴘᴘᴏʀᴛ ғᴏʀ ᴠɪᴅᴇᴏs

**🛠️ Tᴇᴄʜɴᴏʟᴏɢʏ:**
• Pʏʀᴏɢʀᴀᴍ - Tᴇʟᴇɢʀᴀᴍ API
• ʏᴛ-ᴅʟᴘ - Vɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ
• ᴀɪᴏʜᴛᴛᴘ - HTTP ᴅᴏᴡɴʟᴏᴀᴅs
• ʟɪʙᴛᴏʀʀᴇɴᴛ - Tᴏʀʀᴇɴᴛ sᴜᴘᴘᴏʀᴛ
• FFᴍᴘᴇɢ - Vɪᴅᴇᴏ ᴘʀᴏᴄᴇssɪɴɢ
• MᴏɴɢᴏDB - Dᴀᴛᴀʙᴀsᴇ

**👨‍💻 Dᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ:** {dev}
**📢 Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ:** {channel}

**Mᴀᴅᴇ ᴡɪᴛʜ ❤️ ғᴏʀ Tᴇʟᴇɢʀᴀᴍ ᴜsᴇʀs!**"""
