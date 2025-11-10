# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies for yt-dlp and ffmpeg
RUN apt-get update && apt-get install -y \
    ffmpeg \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all bot files
COPY . .

# Create downloads directory
RUN mkdir -p downloads

# Set environment variables (will be overridden by docker-compose or -e flags)
ENV PYTHONUNBUFFERED=1

# Run the bot
CMD ["python", "-u", "bot.py"]
