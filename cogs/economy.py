import random
import discord
from discord import colour
from discord import message
from discord.activity import create_activity
from discord.ext import commands
import json
from jsonUsers import JsonUsers

class Economy(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.profileJson = JsonUsers()

    @commands.command(aliases=["dc", "daily", "claim"])
    async def daily_claim(self, ctx):
        user = ctx.author
        await self.profileJson.verify_user(user)   
        json_users = await self.profileJson.get_json_users()
        coins = random.randint(0,1000)
        json_users[str(user.id)]["coins"] += coins
        await self.profileJson.set_json_users(json_users)
        total_coins = json_users[str(user.id)]["coins"]
        msg = f' +{coins} :coin: added to your balance (total = {total_coins})'
        await ctx.send(msg)

    
    
    

    

def setup(bot):
    bot.add_cog(Economy(bot))