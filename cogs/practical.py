import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.utils.manage_commands import create_option, create_permission
from discord_slash.model import SlashCommandOptionType, SlashCommandPermissionType

from utils import get_ip, delete_message


class Practical(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['ip', 'getip', 'ipaddress'])

    async def getIP(self, ctx):
        message = await ctx.send(f'De cuwwent ip addwess is **{get_ip.get_ip()}**')
        await delete_message.delete_message(message, ctx, 5)

    # GET IP SLASH COMMAND
    # @cog_ext.cog_slash(
    #     name="getIP",
    #     guild_ids=[685842225875386369],
    #     description="Get the IP address of Hamza's router",
    #     options=[
    #         create_option(
    #             name="hidden",
    #             description="Whether or not to make the ip visible to only you",
    #             option_type=SlashCommandOptionType.BOOLEAN,
    #             required=False
    #         )
    #     ]
    # )
    # @cog_ext.permission(
    #     guild_id=685842225875386369,
    #     permissions=[
    #         create_permission(757592018661670932, SlashCommandPermissionType.ROLE, True),
    #         create_permission(685842225875386369, SlashCommandPermissionType.ROLE, False)
    #     ]
    # )
    # async def _getIP(self, ctx, hidden=False):
    #     message = f'De cuwwent ip addwess is **{get_ip.get_ip()}**'
    #     if hidden == True:
    #         await ctx.send(content=message, hidden=True)
    #     else:
    #         await ctx.send(content=message)

    @commands.command()
    async def help(self, ctx):
        helpEmbed = discord.Embed(title="Help", colour=discord.Colour.magenta())

        helpEmbed.add_field(name="Fun", value="------------------------------------------------", inline=False)
        helpEmbed.add_field(name="gae", value="Refuses the gae\n\nAliases: gay")
        helpEmbed.add_field(name="dead", value="I'm not dead. unless...?")
        helpEmbed.add_field(name="shoot", value="gun go brrr")
        helpEmbed.add_field(name="suicide", value="Tries to stop suicide")
        helpEmbed.add_field(name="alive", value="Just checks if the bot is online.")
        helpEmbed.add_field(name="avatar", value="Gets user avatar\n\nAliases: av, ava")


        helpEmbed.add_field(name="Admin", value="------------------------------------------------", inline=False)
        helpEmbed.add_field(name="getIP", value="Gets IP of Hamza's router (Admin only c:)\n\nAliases: ip, getip, ipaddress")
        helpEmbed.add_field(name="reload_all_cogs", value="Reloads all cog extensions.\n\nAliases: reloadAllCogs, reloadAll, reloadall, reloadallcogs, reload")


        await ctx.send(embed=helpEmbed)

def setup(bot):
    bot.add_cog(Practical(bot))