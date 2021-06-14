import asyncio
from discord import Webhook, RequestsWebhookAdapter
import requests
from discord.ext import commands

from utils.utils import get_ip

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
        async with ctx.typing():
            await asyncio.sleep(time)
        await ctx.send(f'{ctx.message.author.mention}, your timer has finished!')

def setup(bot):
    bot.add_cog(Fun(bot))