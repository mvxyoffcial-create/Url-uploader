
🔗 Telegram URL Uploader Bot

<div align="center"><img src="https://i.ibb.co/Z1GwLTwZ/376833becb99.jpg" width="400" alt="Telegram URL Uploader Bot"/>    

A powerful Telegram bot that can download files from any URL and upload them to Telegram with lightning speed! ⚡

🚀 Demo Bot • 📢 Updates • 🐛 Report Bug • 💡 Request Feature

</div>
---

✨ Features

🎯 Core Features

📥 Multi-Source Downloads: HTTP/HTTPS, YouTube, Instagram, TikTok, Facebook, Twitter

🧲 Torrent Support: Magnet links & .torrent files

🚀 Blazing Fast: Up to 500 MB/s download speed

💾 Large Files: Supports up to 4GB per upload

🎬 Original Quality: No compression — preserves full resolution and audio


🛠️ Advanced Features

📊 Real-time Progress: Live status with speed and ETA

🎨 Custom Thumbnails: Save personal thumbnails

✏️ Smart Renaming: Set custom file names dynamically

📝 Custom Captions: Create your own caption templates

⚙️ User Settings: Individualized preferences per user

📈 Statistics: User and bot-level analytics



---

🔗 Supported Platforms

Platform	Status	Features

YouTube	✅	4K, Playlists, Subtitles
Instagram	✅	Posts, Reels, Stories
TikTok	✅	Videos, No watermark
Facebook	✅	Videos, Reels
Twitter/X	✅	Videos, GIFs
Vimeo	✅	HD Video
Direct Links	✅	Resume support
Torrents	✅	Magnet & .torrent



---

🚀 Quick Start

🧰 Prerequisites

Python 3.13.7 or higher

Telegram Bot Token → from @BotFather

MongoDB Cloud Database → from MongoDB Atlas


🧩 Installation

git clone https://github.com/zero-creation690/Url-uploader.git
cd Url-uploader
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your credentials
python bot.py


---

⚙️ Configuration

Environment Variables

# Telegram API (Required)
APP_ID=20288994
API_HASH=d702614912f1ad370a0d18786002adbf
BOT_TOKEN=8062010233:AAExAW3Z-kpT17OTUXg0GQkCVsc7qnDUbXQ

# Database (Required)
DATABASE_URL=mongodb+srv://username:password@cluster.mongodb.net/

# Optional
LOG_CHANNEL=-1001234567890
OWNER_ID=8304706556
SESSION_STR=your_session_string

Get Telegram API Credentials

1. Go to my.telegram.org


2. Create a new app to get APP_ID & API_HASH


3. Talk to @BotFather to get BOT_TOKEN




---

📖 Usage

Command	Description

/start	Welcome message
/help	Full usage instructions
/about	Bot info
/settings	Personalize bot behavior
/status	Show your statistics
/rename	Rename downloaded files


How to Use 🤔

1. Go to /settings and configure preferences


2. Send a custom thumbnail image


3. Paste a link like:

https://youtube.com/watch?v=VIDEO_ID | NewName.mp4


4. Set a custom caption using /caption




---

🧱 Project Structure

Url-uploader/
├── bot.py              # Main bot logic
├── config.py           # Configuration handler
├── database.py         # MongoDB operations
├── downloader.py       # Download manager
├── helpers.py          # Utilities
├── requirements.txt    # Dependencies
└── .env                # Environment config


---

🧠 Technical Architecture

Framework: PyroBlack 2.7.4

Language: Python 3.13.7

Database: MongoDB Cloud

HTTP Client: aiohttp

Video Tools: yt-dlp, FFmpeg

Torrent Engine: libtorrent



---

🌍 Deployment Options

🖥️ Local Run

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python bot.py

🐳 Docker

FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]

💻 VPS (Screen)

screen -S url-bot
python bot.py
# Press Ctrl+A then D to detach


---

📊 Supported URL Formats

# Direct Links
"https://example.com/file.mp4"

# YouTube
"https://youtube.com/watch?v=..."
"https://youtu.be/..."

# Instagram
"https://instagram.com/p/..."
"https://instagram.com/reel/..."

# TikTok
"https://tiktok.com/@user/video/..."

# Torrent
"magnet:?xt=urn:btih:..."
"file.torrent"


---

🤝 Contributing

We love community contributions! ❤️

1. Fork the repo


2. Create a branch

git checkout -b feature/NewFeature


3. Commit your changes

git commit -m "Add NewFeature"


4. Push & open a pull request



Development Setup

pip install -r requirements-dev.txt
python -m pytest
black .


---

🐛 Troubleshooting

Common Issues

Bot not starting:

Check .env credentials

Verify MongoDB connection

Confirm Python 3.13.7+


Downloads failing:

URL inaccessible or unsupported

Network instability


Uploads failing:

File exceeds Telegram’s 4GB limit

Disk space issues

Telegram API timeout



---

📡 Getting Help

📢 Updates: @zerodevbro

👨‍💻 Developer: @Zeroboy216

🐛 Report Issues: GitHub Issues



---

📄 License

Licensed under the MIT License — see the LICENSE file for details.


---

🙏 Acknowledgments

Pyrogram Team – Telegram API framework

yt-dlp Developers – YouTube & media downloader

MongoDB Atlas – Cloud database hosting

Telegram – Platform for bot development



---

📞 Support & Links

💬 Telegram: @Zeroboy216
📢 Channel: @zerodevbro
💾 Repository: zero-creation690/Url-uploader


---

<div align="center">⭐ If you love this project, don’t forget to give it a star! ⭐

Made with ❤️ by Zero Boy

🚀 Try Bot • 📢 Join Channel • 💻 GitHub

</div>
