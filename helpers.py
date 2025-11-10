import time
import asyncio
import math
from typing import Optional
from pyrogram.errors import MessageNotModified, FloodWait

class Progress:
    """Enhanced progress tracker for downloads, uploads, and torrents"""
    
    def __init__(self, client, message):
        self.client = client
        self.message = message
        self.start_time = time.time()
        self.last_update = 0
        self.update_interval = 2  # Update every 2 seconds for faster feedback
        self.last_text = ""
        self.last_percentage = 0
        
    async def progress_callback(self, current, total, status="Processing"):
        """
        Enhanced progress callback for pyrogram
        Works with downloads, uploads, and torrents
        """
        now = time.time()
        
        # Skip if too soon (avoid flood)
        if now - self.last_update < self.update_interval:
            return
        
        try:
            elapsed = now - self.start_time
            
            if current == 0 or elapsed == 0 or total == 0:
                return
            
            # Calculate metrics
            speed = current / elapsed
            percentage = (current * 100) / total
            eta_seconds = (total - current) / speed if speed > 0 else 0
            
            # Only update if percentage changed significantly (1% threshold)
            if abs(percentage - self.last_percentage) < 1 and percentage < 99:
                return
            
            self.last_percentage = percentage
            
            # Create enhanced progress bar (20 blocks)
            filled = int(percentage / 5)
            progress_bar = "█" * filled + "░" * (20 - filled)
            
            # Format sizes
            current_formatted = humanbytes(current)
            total_formatted = humanbytes(total)
            speed_formatted = humanbytes(int(speed))
            
            # Build status text
            text = (
                f"**{status}**\n\n"
                f"{progress_bar} `{percentage:.1f}%`\n\n"
                f"📦 **Size:** {current_formatted} / {total_formatted}\n"
                f"⚡ **Speed:** {speed_formatted}/s\n"
                f"⏱️ **ETA:** {format_time(eta_seconds)}\n"
                f"🕐 **Elapsed:** {format_time(elapsed)}"
            )
            
            # Only update if text changed
            if text != self.last_text:
                await self.message.edit_text(text)
                self.last_text = text
                self.last_update = now
                
        except MessageNotModified:
            pass
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            # Silently ignore other errors
            pass

class TorrentProgress(Progress):
    """Specialized progress tracker for torrent downloads"""
    
    def __init__(self, client, message):
        super().__init__(client, message)
        self.update_interval = 3  # Slightly slower for torrents
        
    async def torrent_progress_callback(self, current, total, extra_info=""):
        """
        Progress callback specifically for torrents
        extra_info can include peer count, seeds, etc.
        """
        now = time.time()
        
        if now - self.last_update < self.update_interval:
            return
        
        try:
            elapsed = now - self.start_time
            
            if current == 0 or total == 0:
                # Show waiting state for torrents
                text = (
                    f"**📥 Downloading Torrent**\n\n"
                    f"⏳ Connecting to peers...\n"
                    f"{extra_info}"
                )
                await self.message.edit_text(text)
                self.last_update = now
                return
            
            # Calculate metrics
            speed = current / elapsed if elapsed > 0 else 0
            percentage = (current * 100) / total
            eta_seconds = (total - current) / speed if speed > 0 else 0
            
            # Progress bar
            filled = int(percentage / 5)
            progress_bar = "█" * filled + "░" * (20 - filled)
            
            # Format data
            current_formatted = humanbytes(current)
            total_formatted = humanbytes(total)
            speed_formatted = humanbytes(int(speed))
            
            text = (
                f"**📥 Downloading Torrent**\n\n"
                f"{progress_bar} `{percentage:.1f}%`\n\n"
                f"📦 **Size:** {current_formatted} / {total_formatted}\n"
                f"⚡ **Speed:** {speed_formatted}/s\n"
                f"⏱️ **ETA:** {format_time(eta_seconds)}\n"
                f"🕐 **Elapsed:** {format_time(elapsed)}\n"
                f"{extra_info}"
            )
            
            if text != self.last_text:
                await self.message.edit_text(text)
                self.last_text = text
                self.last_update = now
                
        except MessageNotModified:
            pass
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            pass

def format_time(seconds):
    """Format seconds to human readable time"""
    if seconds < 0:
        return "calculating..."
    
    if seconds < 60:
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
    
    power = 1024
    n = 0
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    
    while size >= power and n < len(units) - 1:
        size /= power
        n += 1
    
    return f"{size:.2f} {units[n]}"

async def speed_limiter(chunk_size, speed_limit):
    """
    Limit download/upload speed
    Args:
        chunk_size: Size of current chunk in bytes
        speed_limit: Maximum speed in bytes per second
    """
    if speed_limit <= 0:
        return
    
    delay = chunk_size / speed_limit
    if delay > 0:
        await asyncio.sleep(delay)

def is_url(text):
    """
    Check if text is a valid URL or magnet link
    Supports:
    - HTTP/HTTPS URLs
    - FTP URLs
    - Magnet links
    - WWW URLs
    """
    if not text or not isinstance(text, str):
        return False
    
    text = text.strip().lower()
    
    # Check for various URL schemes
    valid_schemes = (
        'http://', 'https://', 
        'ftp://', 'ftps://',
        'www.',
        'magnet:?'
    )
    
    return text.startswith(valid_schemes)

def is_magnet_link(text):
    """Check if text is a magnet link"""
    if not text or not isinstance(text, str):
        return False
    return text.strip().lower().startswith('magnet:?')

def is_torrent_file(text):
    """Check if URL points to a torrent file"""
    if not text or not isinstance(text, str):
        return False
    return text.strip().lower().endswith('.torrent')

def sanitize_filename(filename, max_length=255):
    """
    Remove invalid characters from filename and limit length
    Args:
        filename: Original filename
        max_length: Maximum allowed length (default: 255)
    Returns:
        Sanitized filename
    """
    if not filename:
        return "download"
    
    # Invalid characters for most filesystems
    invalid_chars = '<>:"/\\|?*'
    
    # Replace invalid characters
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Remove control characters
    filename = ''.join(char for char in filename if ord(char) >= 32)
    
    # Limit length while preserving extension
    if len(filename) > max_length:
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        if ext:
            max_name_length = max_length - len(ext) - 1
            filename = name[:max_name_length] + '.' + ext
        else:
            filename = filename[:max_length]
    
    # Remove leading/trailing spaces and dots
    filename = filename.strip('. ')
    
    # Fallback if filename becomes empty
    if not filename:
        return "download"
    
    return filename

def get_file_extension(url_or_filename):
    """
    Extract file extension from URL or filename
    Returns extension with dot (e.g., '.mp4') or empty string
    """
    if not url_or_filename:
        return ""
    
    # Remove query parameters
    clean_url = url_or_filename.split('?')[0]
    
    # Get extension
    if '.' in clean_url:
        ext = clean_url.rsplit('.', 1)[-1].lower()
        # Validate extension (max 5 chars)
        if len(ext) <= 5 and ext.isalnum():
            return f".{ext}"
    
    return ""

def format_torrent_info(peers=0, seeds=0, download_rate=0, upload_rate=0):
    """
    Format torrent-specific information for display
    Args:
        peers: Number of connected peers
        seeds: Number of seeds
        download_rate: Download rate in bytes/s
        upload_rate: Upload rate in bytes/s
    Returns:
        Formatted string with torrent info
    """
    info_parts = []
    
    if peers >= 0:
        info_parts.append(f"👥 **Peers:** {peers}")
    
    if seeds >= 0:
        info_parts.append(f"🌱 **Seeds:** {seeds}")
    
    if download_rate > 0:
        info_parts.append(f"⬇️ **Down:** {humanbytes(int(download_rate))}/s")
    
    if upload_rate > 0:
        info_parts.append(f"⬆️ **Up:** {humanbytes(int(upload_rate))}/s")
    
    return "\n".join(info_parts) if info_parts else ""

def validate_file_size(size, max_size):
    """
    Validate if file size is within limits
    Args:
        size: File size in bytes
        max_size: Maximum allowed size in bytes
    Returns:
        Tuple of (is_valid: bool, message: str)
    """
    if size <= 0:
        return False, "Invalid file size"
    
    if size > max_size:
        size_formatted = humanbytes(size)
        max_formatted = humanbytes(max_size)
        return False, f"File size ({size_formatted}) exceeds limit ({max_formatted})"
    
    return True, "Valid"

async def retry_on_flood(func, max_retries=3):
    """
    Retry function on FloodWait error
    Args:
        func: Async function to execute
        max_retries: Maximum number of retries
    Returns:
        Function result or raises last exception
    """
    retries = 0
    
    while retries < max_retries:
        try:
            return await func()
        except FloodWait as e:
            retries += 1
            if retries >= max_retries:
                raise
            await asyncio.sleep(e.value)
        except Exception as e:
            raise
    
    return None
