import os

def get_cogs():
    cogs = []

    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            cog = f"cogs.{file.replace('.py', '')}"
            cogs.append(cog)

    return cogs
