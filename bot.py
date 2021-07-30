import discord
from discord.ext import commands
from discord_slash import SlashCommand

import utils

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

config = utils.get_config()

TOKEN = config['token']
PREFIX = config['prefix']

client = commands.Bot(command_prefix=PREFIX, help_command=None, inents=intents)
slash = SlashCommand(client, sync_commands=True)

for cog in utils.get_cogs():
    try:
        client.load_extension(cog)
        print(f'{cog} loaded')
    except Exception as e:
        print(f'{cog} failed to load')
        raise e

client.run(TOKEN)
