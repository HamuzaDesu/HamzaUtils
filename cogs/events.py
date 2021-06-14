import discord
from discord.ext import commands, tasks

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged on as {self.bot.user}')

        botActivity = discord.Game("It's not like I'm Hamza's slave or anything... b-baka")
        await self.bot.change_presence(status=discord.Status.online, activity=botActivity)

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user: return

        if message.content.startswith('uwu'):
            await message.channel.send('uwu my bwotha')

def setup(bot):
    bot.add_cog(Events(bot))
