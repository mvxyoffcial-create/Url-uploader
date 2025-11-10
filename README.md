# 🤖 Telegram URL Uploader Bot

A powerful Telegram bot that can download files from any URL and upload them to Telegram with progress tracking, custom thumbnails, and more!

## ✨ Features

- 📥 Download files from any HTTP/HTTPS URL
- 🎥 Download videos from YouTube, Instagram, TikTok, etc.
- 📤 Upload files up to 4GB to Telegram
- 📊 Real-time progress bar with speed and ETA
- 🎨 Custom thumbnails support
- ✏️ Custom filename and caption
- 🚀 Speed limiting (10 MB/s) to save bandwidth
- 💾 MongoDB integration for user data and logs
- 📈 Statistics tracking
- 📢 Broadcast messages to all users (owner only)

## 🛠️ Installation

### 1. Clone or Download

Create a new directory and save all the files:
- `bot.py`
- `config.py`
- `database.py`
- `downloader.py`
- `helpers.py`
- `requirements.txt`
- `.env`

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Edit the `.env` file with your credentials (already provided):

```env
API_HASH=your_api_hash
APP_ID=your_app_id
BOT_TOKEN=your_bot_token
DATABASE_URL=your_mongodb_url
LOG_CHANNEL=your_log_channel_id
OWNER_ID=your_telegram_user_id
```

### 4. Run the Bot

```bash
python bot.py
```

## 📝 Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/about` - About the bot
- `/settings` - View current settings
- `/setname <filename>` - Set custom filename
- `/setcaption <caption>` - Set custom caption
- `/clearsettings` - Clear all settings
- `/status` - Check your statistics
- `/total` - View bot statistics (owner only)
- `/broadcast` - Broadcast message (owner only)

## 🎯 Usage

### Download & Upload a File

Simply send any URL to the bot:

```
https://example.com/file.zip
```

### Download YouTube Video

```
https://www.youtube.com/watch?v=VIDEO_ID
```

### Set Custom Filename

```
/setname MyCustomFile.mp4
```

### Set Custom Caption

```
/setcaption This is my custom caption with emojis 🎉
```

### Set Thumbnail

Send any photo to the bot to set it as thumbnail for future uploads.

## 📂 Project Structure

```
telegram-bot/
├── bot.py              # Main bot file with command handlers
├── config.py           # Configuration loader
├── database.py         # MongoDB handler
├── downloader.py       # File downloader (aiohttp + yt-dlp)
├── helpers.py          # Utility functions
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
└── downloads/         # Temporary download directory (auto-created)
```

## 🔧 Technical Details

### Download Methods

1. **HTTP/HTTPS Files**: Uses `aiohttp` for async downloading with speed limiting
2. **Video Sites**: Uses `yt-dlp` for YouTube, Instagram, TikTok, etc.

### Speed Limiting

- Download speed: 10 MB/s (configurable in `config.py`)
- Upload speed: 10 MB/s (configurable in `config.py`)
- Chunk size: 512 KB

### Database Schema

**Users Collection:**
- `user_id`: Telegram user ID
- `username`: Telegram username
- `first_name`: User's first name
- `joined_date`: Date user started bot
- `last_used`: Last activity timestamp
- `total_downloads`: Total files downloaded
- `total_uploads`: Total files uploaded

**Logs Collection:**
- `user_id`: User who performed action
- `action`: Action type (start, download, upload, error)
- `details`: Action details
- `timestamp`: When action occurred

## 🚀 Deployment

### Deploy on VPS/Server

```bash
# Clone repository
git clone your-repo-url
cd telegram-bot

# Install dependencies
pip install -r requirements.txt

# Configure environment
nano .env

# Run with screen or tmux
screen -S bot
python bot.py
```

### Deploy on Heroku

1. Create `Procfile`:
```
worker: python bot.py
```

2. Push to Heroku:
```bash
heroku create your-app-name
git push heroku main
heroku ps:scale worker=1
```

### Deploy with Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "bot.py"]
```

## 🔐 Security Notes

- Never share your `.env` file or credentials
- Keep your `BOT_TOKEN` and `API_HASH` private
- Use strong MongoDB passwords
- Restrict `OWNER_ID` commands to trusted users only

## 📊 Performance

- Supports files up to 4GB (Telegram limit)
- Concurrent downloads/uploads
- Automatic cleanup of temporary files
- Speed limiting to prevent bandwidth exhaustion

## 🐛 Troubleshooting

### Bot not responding
- Check if bot token is correct
- Verify bot is running: `ps aux | grep bot.py`
- Check logs for errors

### Download fails
- Verify URL is accessible
- Check if website requires authentication
- Some sites may block bots

### Upload fails
- Check file size (max 4GB)
- Verify Telegram API credentials
- Check internet connection

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Contact: @YourUsername on Telegram

## 🙏 Credits

- [Pyrogram](https://docs.pyrogram.org/) - Telegram MTProto API framework
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Video downloader
- [aiohttp](https://docs.aiohttp.org/) - Async HTTP client
- [Motor](https://motor.readthedocs.io/) - Async MongoDB driver

---

Made with ❤️ for the Telegram community
