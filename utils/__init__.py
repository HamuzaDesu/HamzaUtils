import asyncio,  os, requests, json

async def delete_message(message, ctx, time):
    await asyncio.sleep(time)

    await ctx.message.delete()
    await message.delete()

def get_cogs():
    cogs = []

    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            cog = f"cogs.{file.replace('.py', '')}"
            cogs.append(cog)

    return cogs

def get_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
        return config

def get_ip():
    res = requests.get('https://ident.me/')
    return str(res.content.decode('utf-8'))
