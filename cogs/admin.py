import discord
from discord.ext import commands

import os
from utils.utils import get_cogs, delete_message



class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Just checks if the bot is online.')
    async def alive(self, ctx):
        await ctx.send("I am awive")
    
    # @commands.is_owner()
    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['reloadAllCogs', 'reloadAll', 'reloadall', 'reloadallcogs', 'reload'], brief='Reloads all cog extensions.')
    async def reload_all_cogs(self, ctx):
        for cog in get_cogs():
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        message = await ctx.send(f"Rewoaded all cogs")

        await delete_message(message, ctx, 5)
def setup(bot):
    bot.add_cog(Admin(bot))