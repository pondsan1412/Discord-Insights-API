import discord
import discord.ext.commands as commands 
import requests as req

class check_connection(commands.Cog):
    def __init__(
            self,
            bot:commands.Bot
    ):
        self.bot = bot

    @commands.hybrid_command()
    async def check_connection(
        self,
        i:commands.Context,
        url:str
    ):
        """check connection between website"""
        if i:
            r = req.get(
                url=""
            )
