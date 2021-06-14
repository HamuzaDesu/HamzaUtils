import flask
from flask.helpers import flash
from flask.json import jsonify
import requests
from utils.utils import get_config


APPLICATION_ID = '816339520503939132'
GUILD_ID = 685842225875386369
# url = f"https://discord.com/api/v8/applications/{APPLICATION_ID}/commands"
url = f"https://discord.com/api/v8/applications/{APPLICATION_ID}/guilds/{GUILD_ID}/commands"

config = get_config()

json = {
    "name" : "shoot",
    "description" : "gun go brrr"
}

headers = {
    "Authorization": f"Bot {config['token']}"
}

res = requests.post(url, headers=headers, json=json)
# interaction = res.json()
# print(interaction)

# if res.status_code == 200:
#     url = f"https://discord.com/api/v8/interactions/{res['id']}/<interaction_token>/callback"
# print(res.status_code)
