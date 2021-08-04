import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_permission
from discord_slash.model import SlashCommandOptionType, SlashCommandPermissionType

import utils

class Practical(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['ip', 'getip', 'ipaddress'])
    async def getIP(self, ctx):
        message = await ctx.send(f'De cuwwent ip addwess is **{utils.get_ip()}**')
        await utils.delete_message(message, ctx, 5)

    # GET IP SLASH COMMAND
    @cog_ext.cog_slash(
        name="getIP",
        description="Get the IP address of Hamza's router",
        options=[
            create_option(
                name="hidden",
                description="Whether or not to make the ip visible to only you",
                option_type=SlashCommandOptionType.BOOLEAN,
                required=False
            )
        ]
    )
    @cog_ext.permission(
        guild_id=685842225875386369,
        permissions=[
            create_permission(757592018661670932, SlashCommandPermissionType.ROLE, True),
            create_permission(685842225875386369, SlashCommandPermissionType.ROLE, False)
        ]
    )
    async def _getIP(self, ctx, hidden=False):
        message = f'De cuwwent ip addwess is **{utils.get_ip()}**'
        if hidden == True:
            await ctx.send(content=message, hidden=True)
        else:
            await ctx.send(content=message)

    # Custom Help
    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(title="Help", colour=discord.Colour.magenta())

        helpEmbed.add_field(name="alive", value="Just checks if the bot is online.")
        helpEmbed.add_field(name="avatar", value="Gets user avatar\n\nAliases: av, ava")

        helpEmbed.add_field(name="Admin", value="------------------------------------------------", inline=False)
        helpEmbed.add_field(name="getIP", value="Gets IP of Hamza's router (Admin only c:)\n\nAliases: ip, getip, ipaddress")
        helpEmbed.add_field(name="reload_all_cogs", value="Reloads all cog extensions.\n\nAliases: reloadAllCogs, reloadAll, reloadall, reloadallcogs, reload")


        await ctx.send(embed=helpEmbed)

def setup(bot):
    bot.add_cog(Practical(bot))