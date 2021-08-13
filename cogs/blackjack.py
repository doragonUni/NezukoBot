import discord
from discord import colour
from discord import embeds
from discord.activity import create_activity
from discord.embeds import Embed
from discord.ext import commands
import json
from jsonUsers import JsonUsers


class BlackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.profileJson = JsonUsers()
    
    @commands.command()
    async def gamble(self, ctx, qty:int):
        user = ctx.author
        await self.profileJson.verify_user(user)   
        json_users = await self.profileJson.get_json_users()
        current_coins =  json_users[str(user.id)]["coins"]
        if current_coins < qty:
            await ctx.send(f"Insufficient funds, you have {current_coins} in your wallet ")
        else:            
            json_users[str(user.id)]["coins"] -= qty
            em = discord.Embed(title='Coin flip')
            em.add_field(name = ":coin: :coin: :coin: :coin: :coin:", value="👛")
            msg = await ctx.send(embed= em)
            await msg.add_reaction("🅰")
            await msg.add_reaction("🅱")
        await self.profileJson.set_json_users(json_users)


    

def setup(bot):
    bot.add_cog(BlackJack(bot))
    
    
