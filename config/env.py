import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')

host = '127.0.0.1'
api_key = os.getenv('API_KEY')
db_user = os.getenv('DB_USER')
db_name = os.getenv('DATABASE')
db_uri = f'postgresql://{db_user}@{host}/{db_name}'
