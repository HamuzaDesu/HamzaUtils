import asyncio
import discord
from discord.ext import commands

from discord_slash import cog_ext
from discord_slash.utils import manage_commands
from discord_slash.utils.manage_commands import create_option
from discord_slash.model import SlashCommandOptionType


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gay'], brief='Refuses the gae')
    async def gae(self, ctx):
        await ctx.send("I'm not gay!")
    
    @commands.command(brief="I'm not dead. unless...?")
    async def dead(self, ctx):
        await ctx.send("I'm not dead")
    
    @commands.command(brief='gun go brrr')
    async def shoot(self, ctx):
        await ctx.send('Shoot yourself you pussy')
    
    @commands.command(brief='Tries to stop suicide')
    async def suicide(self, ctx):
        await ctx.send("Do it.")

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
        guild_ids=[685842225875386369],
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