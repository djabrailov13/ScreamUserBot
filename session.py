# By t.me/djabrailov13
# ScreamUserBot
#

import sys
import subprocess

vers = 'Public 1.1v'

try:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
except:
    print('Please Wait: Installing Telethon...')
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'telethon'])
finally:
    print('ScreamUserBot ' + vers + '\n')

    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession

api_id = ''
api_hash = ''

while not api_id.isdigit() or len(api_id) < 5 or len(api_id) > 7:
    api_id = input('api_id: ')

while len(api_hash) != 32:
    api_hash = input('api_hash: ')

with TelegramClient(StringSession(), api_id, api_hash) as client:
    client.send_message('me', '**SESSION:** '+'```'+client.session.save()+'```')
    print('SESSION:\n'+client.session.save())

print('Session successfully generated! Please check your Telegram Saved Messages')