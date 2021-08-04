from os import name
import discord
from discord import message
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_permission, remove_all_commands

from discord_slash.model import SlashCommandPermissionType

import utils
#  sdf
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
        description="Checks whether the bot is alive or not"
    )
    async def _alive(self, ctx):
        await ctx.send("I am awive")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def removeSlash(self, ctx):
        await remove_all_commands(self.config["bot_id"], self.config["token"], self.config["guild_ids"])
        await ctx.send("Removed all slash commands")

    config = utils.get_config()
    @cog_ext.cog_subcommand(
        base="remove",
        name="slash",
        description="Remove all slash commands from bot",
    )
    @cog_ext.permission(
        guild_id=685842225875386369,
        permissions=[
            create_permission(757592018661670932, SlashCommandPermissionType.ROLE, True),
            create_permission(685842225875386369, SlashCommandPermissionType.ROLE, False)
        ]
    )
    async def _removeSlash(self, ctx):
        await remove_all_commands(self.config["bot_id"], self.config["token"], self.config["guild_ids"])
        await ctx.send(content='Removed all slash commands', hidden=True)
    # async def test(self, ctx):
    #     await ctx.send('The test worked')
    

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
    )
    async def _reloadAllCogs(self, ctx):
        for cog in utils.get_cogs():
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        await ctx.send(content="Rewoaded all cogs", hidden=True)


def setup(bot):
    bot.add_cog(Admin(bot))