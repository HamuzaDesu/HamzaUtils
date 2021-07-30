from os import name
import discord
from discord import message
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils import manage_commands

import utils

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = utils.get_config()

    config = utils.get_config()

    @commands.command()
    async def alive(self, ctx):
        await ctx.send("I am awive")
    
    @cog_ext.cog_slash(
        name="alive",
        description="Checks whether the bot is alive or not",
        guild_ids=config["guild_ids"]
    )
    async def _alive(self, ctx):
        await ctx.send("I am awive")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def removeSlash(self, ctx):
        commands = await manage_commands.remove_all_commands(self.config["bot_id"], self.config["TOKEN"], self.config["guild_ids"])
        await ctx.send(commands)

    # @commands.is_owner()
    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['reloadAllCogs', 'reloadAll', 'reloadall', 'reloadallcogs', 'reload'], brief='Reloads all cog extensions.')
    async def reload_all_cogs(self, ctx):
        for cog in utils.get_cogs():
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        message = await ctx.send(f"Rewoaded all cogs")

        await utils.delete_message(message, ctx, 5)


    config = utils.get_config()
    @cog_ext.cog_slash(
        name="reload",
        description="Reload all cogs",
        guild_ids=config['guild_ids']
    )
    async def _reloadAllCogs(self, ctx):
        for cog in utils.get_cogs():
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        await ctx.send(content="Rewoaded all cogs", hidden=True)


def setup(bot):
    bot.add_cog(Admin(bot))