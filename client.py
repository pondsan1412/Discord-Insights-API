import discord.ext.commands as commands
import discord
import json
import asyncio
from dotenv import load_dotenv
import os
""" ประกาศ class ของ client
    ประกาศ ตัวแปร เก็บ Intents
 """
def intent():
    return discord.Intents(
        message_content=True,
        members=False,
        presences=False
    )

class client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned,
            description="Bot Fetch latest message in discord server",
            intents=intent()
        )

    #@client.event
    async def on_ready(self):
        print(f"Hello world! {self.user.name}")

load_dotenv()
DC_TOKEN = os.getenv("TOKEN")
bot = client()
bot.run(
    token=DC_TOKEN,
    reconnect=True
)