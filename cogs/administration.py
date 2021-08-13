import discord
from discord import colour
from discord.activity import create_activity
from discord.ext import commands

class Administration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["nuke"])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, qty: int = 1):
        #TODO: Verify if the user that called this command has enough permissions :)
        embed =  discord.Embed()
        author = ctx.message.author
        if qty <= 100:
            await ctx.channel.purge(limit=qty+1) 
            embed.description = "{1}, I just deleted {0} messages for you".format(qty, author.display_name)
            await ctx.send(embed=embed)
        else:
            embed.description = "{1}, I can't delete {0} messages, limit 100".format(qty, author.display_name)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Administration(bot))