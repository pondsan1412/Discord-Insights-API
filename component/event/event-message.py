import discord
import discord.ext.commands as commands
import json
import random

class event_messages(commands.Cog):
    def __init__(
            self,
            bot:commands.Bot
    ):
        self.bot = bot
        with open('config.json', 'r') as file:
            self.config = json.load(file)
        with open('respond-text.json', 'r', encoding='utf-8') as f:
            self.responses = json.load(f)

    @commands.Cog.listener()
    async def on_message(
        self,
        message:discord.Message
    ):
        """keep ignored self messages"""
        if message.author == self.bot.user:
            return
        
        if message.content.startswith("helloworld"):
            if message.author.id == self.config.get("author_owner"):
                await message.reply("hello world!")
        
        if any(word in message.content.lower() for word in ['ขอบคุณ', 'ขอบคุณครับ', 'ขอบใจ', 'thx']):
            if message.author.id == self.config.get('author_owner'):
                await message.reply(
                    content=f"{random.choice(self.responses['respond'])}"
                )

async def setup(bot):
    await bot.add_cog(event_messages(bot))