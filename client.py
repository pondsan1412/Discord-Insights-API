import discord.ext.commands as commands
import discord
import json
import asyncio
from dotenv import load_dotenv
import os
import logging
""" ประกาศ class ของ client
    ประกาศ ตัวแปร เก็บ Intents
 """
def intent():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    return intents


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

    async def setup_hook(self):
        # ลบคำสั่ง help แบบดั้งเดิม
        self.remove_command('help')

        # โหลด cogs จากโฟลเดอร์ component/Context
        context_folder = "component/Context"
        for filename in os.listdir(context_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = f"{context_folder.replace('/', '.')}.{filename[:-3]}"
                try:
                    await self.load_extension(module_name)
                    print(f"Loaded extension: {module_name}")
                except Exception as e:
                    print(f"Failed to load extension {module_name}: {e}")

        # โหลด cogs จากโฟลเดอร์ component/event
        event_folder = "component/event"
        for filename in os.listdir(event_folder):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = f"{event_folder.replace('/', '.')}.{filename[:-3]}"
                try:
                    await self.load_extension(module_name)
                    print(f"Loaded extension: {module_name}")
                except Exception as e:
                    print(f"Failed to load extension {module_name}: {e}")
load_dotenv()
DC_TOKEN = os.getenv("TOKEN")
bot = client()
bot.run(
    token=DC_TOKEN,
    reconnect=True
)