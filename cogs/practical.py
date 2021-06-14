from os import name
import discord
from discord.ext import commands

from utils.utils import get_ip, delete_message

import asyncio


class Practical(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['ip', 'getip', 'ipaddress'], brief="Gets IP of Hamza's router (Admin only c:)")
    async def getIP(self, ctx):
        message = await ctx.send(f'De cuwwent ip addwess is **{get_ip()}**')
        await delete_message(message, ctx, 5)


        
    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(title="Help", colour=discord.Colour.magenta())

        helpEmbed.add_field(name="Fun", value="------------------------------------------------", inline=False)
        helpEmbed.add_field(name="gae", value="Refuses the gae\n\nAliases: gay")
        helpEmbed.add_field(name="dead", value="I'm not dead. unless...?")
        helpEmbed.add_field(name="shoot", value="gun go brrr")
        helpEmbed.add_field(name="suicide", value="Tries to stop suicide")
        helpEmbed.add_field(name="alive", value="Just checks if the bot is online.")


        helpEmbed.add_field(name="Admin", value="------------------------------------------------", inline=False)
        helpEmbed.add_field(name="getIP", value="Gets IP of Hamza's router (Admin only c:)\n\nAliases: ip, getip, ipaddress")
        helpEmbed.add_field(name="reload_all_cogs", value="Reloads all cog extensions.\n\nAliases: reloadAllCogs, reloadAll, reloadall, reloadallcogs, reload")


        await ctx.send(embed=helpEmbed)

def setup(bot):
    bot.add_cog(Practical(bot))