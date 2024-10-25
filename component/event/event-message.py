import discord
import discord.ext.commands as commands

class event_messages(commands.Cog):
    def __init__(
            self,
            bot:commands.Bot
    ):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(
        self,
        message:discord.Message
    ):
        """keep ignored self messages"""
        if message.author == self.bot.user:
            return
        

async def setup(bot):
    await bot.add_cog(event_messages)