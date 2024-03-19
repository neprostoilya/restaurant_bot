import os
from dotenv import load_dotenv


load_dotenv()

# Telegram Token
TOKEN = os.getenv('TOKEN')
# URL
URL = os.getenv('URL')
# CLICK PAYMENT
CLICK = os.getenv('CLICK')
# PAYME PAYMENT
PAYME = os.getenv('PAYME')
# GROUP_ID
GROUP_ID = os.getenv('GROUP_ID')