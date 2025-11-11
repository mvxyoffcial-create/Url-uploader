🔗 Telegram URL Uploader Bot

<div align="center">

https://i.ibb.co/Z1GwLTwZ/376833becb99.jpg

https://img.shields.io/badge/Python-3.13.7-blue.svg
https://img.shields.io/badge/Pyrogram-2.7.4-green.svg
https://img.shields.io/badge/MongoDB-Cloud-brightgreen.svg
https://img.shields.io/badge/License-MIT-yellow.svg
https://img.shields.io/badge/Telegram-Bot-blue.svg

A powerful Telegram bot that can download files from any URL and upload them to Telegram with lightning speed! ⚡

🚀 Demo Bot • 📢 Updates • 🐛 Report Bug • 💡 Request Feature

</div>

✨ Features

🎯 Core Features

· 📥 Multi-Source Downloads: HTTP/HTTPS, YouTube, Instagram, TikTok, Facebook, Twitter
· 🧲 Torrent Support: Magnet links & .torrent files
· 🚀 Blazing Fast: 500 MB/s download speed
· 💾 Large Files: Support up to 4GB files
· 🎬 Original Quality: No compression, preserve original resolution & audio

🛠️ Advanced Features

· 📊 Real-time Progress: Live progress bar with speed and ETA
· 🎨 Custom Thumbnails: Set permanent custom thumbnails
· ✏️ Smart Renaming: Custom filenames with pattern support
· 📝 Custom Captions: Dynamic caption templates
· ⚙️ User Settings: Personalized bot behavior per user
· 📈 Statistics: Detailed user and bot analytics

🔗 Supported Platforms

Platform Status Features
YouTube ✅ 4K, Playlists, Subtitles
Instagram ✅ Posts, Reels, Stories
TikTok ✅ Videos, Watermark-free
Facebook ✅ Videos, Reels
Twitter/X ✅ Videos, GIFs
Vimeo ✅ HD Videos
Direct Links ✅ Resume support
Torrents ✅ Magnet & .torrent

🚀 Quick Start

Prerequisites

· Python 3.13.7 or higher
· Telegram Bot Token (Get from @BotFather)
· MongoDB Database (Free from MongoDB Atlas)

Installation

1. Clone the Repository

```bash
git clone https://github.com/zero-creation690/Url-uploader.git
cd Url-uploader
```

1. Install Dependencies

```bash
pip install -r requirements.txt
```

1. Configure Environment

```bash
cp .env.example .env
# Edit .env with your credentials
```

1. Run the Bot

```bash
python bot.py
```

⚙️ Configuration

Environment Variables

Create a .env file with:

```env
# Telegram API (Required)
APP_ID=20288994
API_HASH=d702614912f1ad370a0d18786002adbf
BOT_TOKEN=8062010233:AAExAW3Z-kpT17OTUXg0GQkCVsc7qnDUbXQ

# Database (Required)
DATABASE_URL=mongodb+srv://username:password@cluster.mongodb.net/

# Optional Settings
LOG_CHANNEL=-1001234567890
OWNER_ID=8304706556
SESSION_STR=your_session_string
```

Get Telegram API Credentials

1. Go to my.telegram.org
2. Create application to get APP_ID and API_HASH
3. Create bot with @BotFather to get BOT_TOKEN

📖 Usage

Basic Commands

Command Description
/start Start the bot and show welcome
/help Detailed help with usage guide
/about Bot information and specifications
/settings Configure bot behavior
/status Your download statistics
/rename Rename downloaded files

How to Use 🤔

1. Configure Settings
   ```
   First go to /settings and change the bot behavior as your choice
   ```
2. Set Custom Thumbnail
   ```
   Send me the custom thumbnail to save it permanently
   ```
3. Download Files
   ```
   Send url | New name.mkv
   ```
4. Set Captions
   ```
   Use /caption to set caption as Reply to media
   ```

Examples

Download YouTube Video:

```
https://youtube.com/watch?v=VIDEO_ID | MyVideo.mp4
```

Download with Custom Name:

```
https://example.com/file.zip | CustomName.zip
```

Set Permanent Thumbnail:
Just send any image to the bot

🏗️ Project Structure

```
Url-uploader/
├── bot.py                 # Main bot handler
├── config.py             # Configuration manager
├── database.py           # MongoDB operations
├── downloader.py         # Multi-source downloader
├── helpers.py            # Utility functions
├── requirements.txt      # Dependencies
└── .env                 # Environment variables
```

Technical Architecture

· Framework: PyroBlack 2.7.4
· Language: Python 3.13.7
· Database: MongoDB Cloud
· HTTP Client: aiohttp
· Video Processing: yt-dlp, FFmpeg
· Torrent: libtorrent

🚀 Deployment

Local Deployment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

Docker Deployment

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
```

VPS Deployment

```bash
# Using screen to keep bot running
screen -S url-bot
python bot.py
# Ctrl+A then D to detach
```

📊 API Reference

Supported URL Formats

```python
# Direct URLs
"https://example.com/file.mp4"

# YouTube
"https://youtube.com/watch?v=..."
"https://youtu.be/..."

# Instagram
"https://instagram.com/p/..."
"https://www.instagram.com/reel/..."

# TikTok
"https://tiktok.com/@user/video/..."

# Torrent
"magnet:?xt=urn:btih:..."
"*.torrent files"
```

🤝 Contributing

We love contributions! Here's how to help:

1. Fork the Repository
2. Create a Feature Branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit Your Changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the Branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest

# Code formatting
black .
```

🐛 Troubleshooting

Common Issues

Bot not starting:

· Check API credentials in .env
· Verify MongoDB connection string
· Ensure Python version is 3.13.7+

Downloads failing:

· Check internet connection
· Verify URL is accessible
· Some sites may block bot requests

Uploads failing:

· File size exceeds 4GB Telegram limit
· Check available disk space
· Verify Telegram API limits

Getting Help

· 📢 Updates Channel: @zerodevbro
· 👨‍💻 Developer: @Zeroboy216
· 🐛 Issues: GitHub Issues

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

· Pyrogram Team - Amazing Telegram MTProto framework
· yt-dlp Developers - Robust video downloader
· MongoDB - Reliable cloud database
· Telegram - Platform for innovation

📞 Support

If you need help or want to suggest features:

· 💬 Telegram: @Zeroboy216
· 📢 Channel: @zerodevbro
· 🐛 Issues: GitHub Issues
· 💾 Repository: zero-creation690/Url-uploader

---

<div align="center">

⭐ Don't forget to star this repository if you find it useful!

Made with ❤️ by Zero Boy

🚀 Try Bot • 📢 Join Channel • 💻 GitHub

</div>
