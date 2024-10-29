import os
from dotenv import load_dotenv
import subprocess
import discord
import discord.ext.commands as commands
import json
import random
import requests

load_dotenv()

class event_messages(commands.Cog):
    def __init__(
            self,
            bot: commands.Bot
    ):
        self.bot = bot
        with open('config.json', 'r') as file:
            self.config = json.load(file)
        with open('respond-text.json', 'r', encoding='utf-8') as f:
            self.responses = json.load(f)
        self.api_url = "http://localhost:5000/api/last_message"
        self.api_token = os.getenv("API_TOKEN", "your_secret_token")

    @commands.Cog.listener()
    async def on_message(
        self,
        message: discord.Message
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

        # ฟังชั่นสำหรับรับค่าต่างๆและ POST ไปยัง Flask server
        try:
            headers = {
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json"
            }
            attachments = []
            if message.attachments:
                for attachment in message.attachments:
                    attachments.append({
                        "filename": attachment.filename,
                        "url": attachment.url,
                        "content_type": attachment.content_type,
                        "size": attachment.size
                    })

            payload = {
                "LastMessage": message.content,
                "datetime": str(message.created_at),
                "profilepicture": str(message.author.display_avatar.url),
                "message_id": str(message.id),
                "message_content": message.content,
                "is_admin": message.author.guild_permissions.administrator if message.guild else False,
                "server_id": str(message.guild.id) if message.guild else None,
                "server_name": message.guild.name if message.guild else None,
                "server_profile_picture": str(message.guild.icon.url) if message.guild else None,
                "attachments": attachments
            }

            response = requests.post(self.api_url, headers=headers, json=payload)
            if response.status_code != 200:
                print(f"Failed to POST to API. Status code: {response.status_code}, Response: {response.text}")

        except Exception as e:
            print(f"Error during POST request: {e}")

async def setup(bot):
    await bot.add_cog(event_messages(bot))


def run_flask():
    subprocess.Popen(["python", "modules/api.py"])


def run_bot():
    subprocess.Popen(["python", "client.py"])


if __name__ == "__main__":
    # เปิด Flask Server และ Discord Bot แยกกันในสอง process
    run_flask()
    run_bot()
