from os import environ
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv, set_key, unset_key

def reload_env():
    return load_dotenv('config.env', override=True)

reload_env()

session = environ.get('session', None)
api_id = environ.get('api_id', None)
api_hash = environ.get('api_hash', None)

with TelegramClient(StringSession(session), api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hi'))