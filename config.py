import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "16214694"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "7545825d90eb7adae543d59909c73121")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8154916973:AAEJP8r_R4nfNnHlCd-4yv5AD7IBheod7Kw")

OWNER_ID = int(os.environ.get("OWNER_ID", "5543709855"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "5543709855").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("mongodb+srv://sonalsangwan04:sonalsangwan04@cluster0.itcf42u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")##your mongo url eg: withmongodb+srv://xxxxxxx:xxxxxxx@clusterX.xxxx.mongodb.net/?retryWrites=true&w=majority
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002633929621"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002633929621")  # Optional here you'll get all logs
