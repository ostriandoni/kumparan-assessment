import os
from models.news import news
from models.topic import topic
from dotenv import load_dotenv

load_dotenv()

MONGO_HOST = os.getenv('DB_HOST')
MONGO_PORT = int(os.getenv('DB_PORT'))
MONGO_DBNAME = os.getenv('DB_NAME')
MONGO_USERNAME = os.getenv('DB_USERNAME')
MONGO_PASSWORD = os.getenv('DB_PASSWORD')
EXTENDED_MEDIA_INFO = ['content_type', 'name', 'length']
RETURN_MEDIA_AS_BASE64_STRING = False
RETURN_MEDIA_AS_URL = True
IF_MATCH = False
DOMAIN = {
    'news': news,
    'topic': topic
}
