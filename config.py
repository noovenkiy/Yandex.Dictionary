import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")

API_BASE_URL = "https://dictionary.yandex.net/api/v1/dicservice.json"

DEFAULT_LANG = "ru-en"
