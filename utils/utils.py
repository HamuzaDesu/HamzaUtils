import os
import urllib.request
import json
import asyncio

def get_cogs():
    cogs = []

    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            cog = f"cogs.{file.replace('.py', '')}"
            cogs.append(cog)

    return cogs

def get_ip():
    return urllib.request.urlopen('https://ident.me/').read().decode('utf8')

def get_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config

async def delete_message(message, ctx, time):
    await asyncio.sleep(time)

    await ctx.message.delete()
    await message.delete()