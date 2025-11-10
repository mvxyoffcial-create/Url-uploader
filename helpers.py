import time
import asyncio
import math
from typing import Optional

class Progress:
    """Progress tracker for downloads and uploads with enhanced UI"""
    
    def __init__(self, client, message):
        self.client = client
        self.message = message
        self.start_time = time.time()
        self.last_update = 0
        self.update_interval = 2  # Update every 2 seconds
        
    async def progress_callback(self, current, total, status="Downloading"):
        """Progress callback for pyrogram with beautiful formatting"""
        now = time.time()
        
        # Update only every N seconds to avoid flood
        if now - self.last_update < self.update_interval:
            return
            
        self.last_update = now
        elapsed = now - self.start_time
        
        if current == 0 or elapsed == 0:
            return
            
        speed = current / elapsed
        percentage = current * 100 / total
        eta_seconds = (total - current) / speed if speed > 0 else 0
        
        # Format data
        current_mb = current / (1024 * 1024)
        total_mb = total / (1024 * 1024)
        speed_mb = speed / (1024 * 1024)
        
        # Create advanced progress bar (20 blocks)
        filled = int(percentage / 5)
        empty = 20 - filled
        
        # Use different characters for better visual
        if filled > 0:
            progress_bar = "█" * filled + "░" * empty
        else:
            progress_bar = "░" * 20
        
        # Status emoji
        status_emoji = "⬇️" if "Download" in status else "⬆️" if "Upload" in status else "🔄"
        
        # Create beautiful progress message
        text = (
            f"{status_emoji} **{status}**\n\n"
            f"`{progress_bar}` {percentage:.1f}%\n\n"
            f"📦 **Size:** {current_mb:.2f} MB / {total_mb:.2f} MB\n"
            f"🚀 **Speed:** {speed_mb:.2f} MB/s\n"
            f"⏱️ **ETA:** {format_time(eta_seconds)}\n"
            f"⏰ **Elapsed:** {format_time(elapsed)}"
        )
        
        try:
            await self.message.edit_text(text)
        except Exception:
            pass

def format_time(seconds):
    """Format seconds to human readable time"""
    if seconds < 0:
        return "0s"
    elif seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        secs = int(seconds % 60)
        return f"{minutes}m {secs}s"
    else:
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        return f"{hours}h {minutes}m"

def humanbytes(size):
    """Convert bytes to human readable format"""
    if not size or size < 0:
        return "0 B"
    
    power = 2**10
    n = 0
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    
    while size > power and n < len(units) - 1:
        size /= power
        n += 1
    
    return f"{size:.2f} {units[n]}"

async def speed_limiter(chunk_size, speed_limit):
    """Limit download/upload speed"""
    delay = chunk_size / speed_limit
    await asyncio.sleep(delay)

def is_url(text):
    """Check if text is a valid URL"""
    if not text:
        return False
    
    url_indicators = [
        'http://', 'https://', 'www.',
        'ftp://', 'ftps://'
    ]
    
    return any(text.lower().startswith(indicator) for indicator in url_indicators)

def is_magnet(text):
    """Check if text is a magnet link"""
    if not text:
        return False
    return text.lower().startswith('magnet:?')

def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    if not filename:
        return "file"
    
    # Invalid characters for filenames
    invalid_chars = '<>:"/\\|?*'
    
    # Replace invalid characters with underscore
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    
    # If filename is empty after sanitization
    if not filename:
        filename = "file"
    
    return filename

def get_file_extension(filename):
    """Get file extension from filename"""
    if not filename or '.' not in filename:
        return ''
    return filename.rsplit('.', 1)[-1].lower()

def is_video_file(filename):
    """Check if file is a video based on extension"""
    video_extensions = [
        'mp4', 'mkv', 'avi', 'mov', 'flv', 'wmv', 
        'webm', 'm4v', 'mpg', 'mpeg', '3gp', 'ts'
    ]
    
    ext = get_file_extension(filename)
    return ext in video_extensions

def is_audio_file(filename):
    """Check if file is an audio file"""
    audio_extensions = [
        'mp3', 'wav', 'flac', 'aac', 'ogg', 
        'wma', 'm4a', 'opus', 'ape'
    ]
    
    ext = get_file_extension(filename)
    return ext in audio_extensions

def is_document_file(filename):
    """Check if file is a document"""
    doc_extensions = [
        'pdf', 'doc', 'docx', 'xls', 'xlsx', 
        'ppt', 'pptx', 'txt', 'zip', 'rar', '7z'
    ]
    
    ext = get_file_extension(filename)
    return ext in doc_extensions

def format_duration(seconds):
    """Format duration in seconds to HH:MM:SS"""
    if not seconds or seconds < 0:
        return "00:00"
    
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

async def run_command(command):
    """Run shell command asynchronously"""
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    
    return process.returncode, stdout.decode(), stderr.decode()

def truncate_text(text, max_length=100):
    """Truncate text to max length"""
    if not text:
        return ""
    
    if len(text) <= max_length:
        return text
    
    return text[:max_length - 3] + "..."

def create_progress_bar(percentage, length=20):
    """Create a progress bar string"""
    filled = int(percentage / 100 * length)
    empty = length - filled
    
    return "█" * filled + "░" * empty

def parse_torrent_info(info_dict):
    """Parse torrent info dictionary"""
    if not info_dict:
        return {}
    
    return {
        'name': info_dict.get('name', 'Unknown'),
        'size': info_dict.get('total_size', 0),
        'files': info_dict.get('num_files', 1),
        'pieces': info_dict.get('num_pieces', 0)
    }

def validate_url(url):
    """Validate if URL is properly formatted"""
    if not url:
        return False
    
    # Basic URL validation
    try:
        from urllib.parse import urlparse
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def get_readable_message(current, total, status="Processing"):
    """Get a readable progress message"""
    percentage = (current / total) * 100 if total > 0 else 0
    current_readable = humanbytes(current)
    total_readable = humanbytes(total)
    
    return f"{status}: {percentage:.1f}% ({current_readable}/{total_readable})"

def estimate_completion_time(current, total, start_time):
    """Estimate completion time based on current progress"""
    if current == 0:
        return "Calculating..."
    
    elapsed = time.time() - start_time
    rate = current / elapsed
    remaining = total - current
    eta = remaining / rate if rate > 0 else 0
    
    return format_time(eta)
