# this is important
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
token = "enter here your bot token!"


# bot event. Its do something if on triggered
@bot.event
	async def on_ready():
	print("bot is started")


# command
@bot.command()
	async def command(ctx):
	# put your code here


# this runs your bot
bot.run(token)
