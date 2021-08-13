import discord
from discord import colour
from discord.activity import create_activity
from discord.ext import commands
import json
from jsonUsers import JsonUsers

class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.profileJson = JsonUsers()        

    @commands.command(aliases=["p"])
    async def profile(self, ctx, member: discord.Member = None):
        user = member or ctx.author
        await self.profileJson.verify_user(user)   
        json_users = await self.profileJson.get_json_users()
        about_me = json_users[str(user.id)]["about_me"]
        coins =  json_users[str(user.id)]["coins"]

        em = discord.Embed(title = f"{ctx.author.name}'s profile", color= discord.Colour.from_rgb(r=255,g=183,b=197))
        em.set_thumbnail(url=f'''{user.avatar_url}''')
        em.add_field(name = ":coin: Coins", value=coins)
        em.add_field(name = "Description", value=about_me)
        await self.profileJson.set_json_users(json_users)
        await ctx.send(embed = em)
    
    @commands.command(aliases=["description"])
    async def set_description(self, ctx, content:str):
        user = ctx.author
        await self.profileJson.verify_user(ctx.author)
        json_users = await self.profileJson.get_json_users()
        json_users[str(user.id)]["about_me"] = content 

        await self.profileJson.set_json_users(json_users)
        await ctx.send("your description was changed successfully")
    

def setup(bot):
    bot.add_cog(Profile(bot))