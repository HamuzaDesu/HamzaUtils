import asyncio
from os import name
import discord
from discord.ext import commands

from discord_slash import cog_ext
from discord_slash.utils import manage_commands
from discord_slash.utils.manage_commands import create_option
from discord_slash.model import SlashCommandOptionType
from requests.models import ContentDecodingError

from utils import get_yo_mama_joke

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['yomama', 'mama'])
    async def yoMama(self, ctx):
        await ctx.send(get_yo_mama_joke()['joke'])

    @cog_ext.cog_subcommand(
        base="yo",
        name='mama',
        description='Print out a yo mama joke'
    )
    async def _yoMama(self, ctx):
        await ctx.send(content=f'{get_yo_mama_joke()["joke"]}')

    @commands.command()
    async def timer(self, ctx, time : int):
        if time > 10 or time < 1:
            await ctx.send('Time must be within 1 and 10 seconds')
            return

        async with ctx.typing():
            await asyncio.sleep(time)
        await ctx.send(f'{ctx.message.author.mention}, your timer has finished!')


    @commands.command(aliases=['av', 'ava'])
    async def avatar(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.message.author
        avatarLink = member.avatar_url

        avatarEmbed = discord.Embed(colour=discord.Colour.blurple())

        avatarEmbed.set_image(url=avatarLink)
        avatarEmbed.set_author(name=member, icon_url=avatarLink)

        await ctx.send(embed=avatarEmbed)

    @cog_ext.cog_slash(
        name="avatar",
        description="Display a users avatar",
        options=[
            create_option(
                name="member",
                description="User to get avatar from",
                option_type=SlashCommandOptionType.USER,
                required=False
            )
        ]
    )
    async def _avatar(self, ctx, member=None):
        if member == None:
            member = ctx.author

        avatarLink = member.avatar_url

        avatarEmbed = discord.Embed(colour=discord.Colour.blurple())

        avatarEmbed.set_image(url=avatarLink)
        avatarEmbed.set_author(name=member, icon_url=avatarLink)

        await ctx.send(embed=avatarEmbed)


def setup(bot):
    bot.add_cog(Fun(bot))