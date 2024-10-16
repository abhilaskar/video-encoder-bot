import os
from pyrogram import Client
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

api_id = int(os.environ.get("API_ID", "24872345"))
api_hash = os.environ.get("API_HASH", "e4d28d51a26681f692a24d3ae7cb8d0c")
bot_token = os.environ.get("BOT_TOKEN", "7882058840:AAGIJivkzXOBWv-2o0aBD-dSJEU-NxNb49k")
download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))

app = Client(":memory:", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
