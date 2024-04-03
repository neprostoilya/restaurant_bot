import os
from dotenv import load_dotenv


load_dotenv()

# Telegram Token for client
TOKEN_BOT_1 = os.getenv('TOKEN_BOT_1')
# Telegram Token for bot 2
TOKEN_BOT_2 = os.getenv('TOKEN_BOT_2')
# URL
URL = os.getenv('URL')
# CLICK PAYMENT
CLICK = os.getenv('CLICK')
# PAYME PAYMENT
PAYME = os.getenv('PAYME')
# GROUP_ID
GROUP_ID = os.getenv('GROUP_ID')