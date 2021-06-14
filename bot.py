import discord
from discord.ext import commands
import json
import os

from utils.utils import get_cogs, get_config

config = get_config()

TOKEN = config['token']
PREFIX = config['prefix']

client = commands.Bot(command_prefix=PREFIX, help_command=None)

for cog in get_cogs():
    try:
        client.load_extension(cog)
        print(f'{cog} loaded')
    except Exception as e:
        print(f'{cog} failed to load')
        raise e

client.run(TOKEN)
