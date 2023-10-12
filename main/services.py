import requests
from config import settings


def send_message_tg(user_id, text):
    try:
        requests.post(f'https://api.telegram.org/bot{settings.BOT_API_KEY}/sendMessage?chat_id={user_id}&text={text}')
    except Exception as _err:
        print(_err)
