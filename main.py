import discord
from discord.enums import AuditLogAction
from discord.ext import commands
import builtins
from discord.ext.commands.core import guild_only
from discord.activity import create_activity
import datetime

bot = commands.Bot(command_prefix='?')
builtins.bot = bot #This allow me to encapsulate diferent .py files for diferent functionality

cogs = ['cogs.administration', 'cogs.profile', 'cogs.economy', 'cogs.blackjack']
for cog in cogs:
    bot.load_extension(cog)



#Every time discord bot is ON will print this message on the console
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your heart. \nCall me using ?"))   #activity 
    print('Logged on as {0}!'.format(bot.user))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        timer = str(datetime.timedelta(seconds=int(error.retry_after)))
        msg = "You have a **{0}** second cooldown for using this command again ".format(timer)
        await ctx.send(msg)







