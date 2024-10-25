import discord
import discord.ext.commands as commands 
import requests as req
import json
import asyncio
class check_connection(commands.Cog):
    def __init__(
            self,
            bot:commands.Bot
    ):
        self.bot = bot
        self.bot_thinking = './public/assets/bot-thinking.gif' #images

    @commands.hybrid_command()
    async def get(
        self,
        i:commands.Context,
        url:str
    ):
        """check connection between website"""
        
        if i:
            try:
                images = await i.send(file=discord.File(self.bot_thinking))
                r = req.get(url=url)

                # แปลงข้อมูล JSON เป็นสตริง
                formatted_json = json.dumps(r.json(), indent=4)
                
                await asyncio.sleep(2)
                await images.delete()
                if len(formatted_json) > 2000:
                    first_message = await i.send(f"Error: มันยาวกว่า 2000 ตัวอักษรครับ คุณ {i.author.name} \n เดี๋ยวจะส่งเป็นไฟล์ให้แทนนะครับ")
                    await asyncio.sleep(2)
                    images = await i.send(file=discord.File(self.bot_thinking))
                    await asyncio.sleep(1)
                    await images.delete()
                    with open("output.json", "W") as file:
                        file.write(formatted_json)
                    await i.send(file=discord.File("output.json"))
                    
                else:
                    await i.send(f"```json\n{formatted_json}\n```")

            except discord.HTTPException as e:
                await i.send(f"เกิดข้อผิดพลาด ```{e}``` \nขอแนะนำให้คุณ {i.author.name} ลองหา URL อื่นๆ ที่ output ไม่ยาวกว่า 4000 TOKEN ครับ")


async def setup(bot):
    await bot.add_cog(check_connection(bot))