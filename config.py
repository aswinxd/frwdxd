import os

API_ID = int(os.environ.get("API_ID","12799559"))
API_HASH = os.environ.get("API_HASH","QT2AAUK9RC6GX96E7D6S8YWJ")
BOT_TOKEN = os.environ.get("BOT_TOKEN","6765987978:AAHuqASdsQPFUV2O28nbx9nbM0QbTwHKL4U")
MONGO_DB_URI = os.environ.get("MONGO_DB_URI","mongodb+srv://mdalizadeh16:lavos@cluster0.u21tcwa.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = int(os.environ.get("LOG_GROUP","-1002055628777"))
ADMIN_USERS_ID = list(map(int, os.environ.get("ADMIN_USERS_ID","6854172577").split()))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL","-1002023444138"))
