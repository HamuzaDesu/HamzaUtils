import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):

    #     if isinstance(error, commands.CommandNotFound):
    #         await ctx.send('You dumb? Thats not a command.')
    #     elif isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send('Gimme dem deets')
    #     elif isinstance(error, commands.MissingPermissions):
    #         await ctx.send('Bitch ur too poor to use this command')
    #     elif isinstance(error, commands.NotOwner):
    #         await ctx.send(f"Uhh you can't use that command headass")
    #     # else:
        #     pass

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))