import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
token = "enter your bot token here"


@bot.event
async def on_ready():
print("bot template by HayotoGHG#9999 is started")


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, reason=None):
  if member is None:
      await ctx.send('You must specify a user')
      return
  elif reason is None:
      await ctx.send("You have to give a reason!")
  embed = discord.Embed(title="💢 | User is banned", color=0xff0000)
  embed.set_author(name="#teamhayoto")
  embed.add_field(name="", value=f"The user {member} is banned!", inline=True)
  embed.add_field(name="Reason:", value=f"{reason}", inline=False)
  await ctx.send(embed=embed)
  await member.ban(reason=reason)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, reason=None):
  if member is None:
      await ctx.send('You must specify a user')
      return
  elif reason is None:
      await ctx.send("You have to give a reason!")
  embed = discord.Embed(title="💢 | User is kicked", color=0xff0000)
  embed.set_author(name="#teamhayoto")
  embed.add_field(name="", value=f"The user {member} is kicked!", inline=True)
  embed.add_field(name="Reason:", value=f"{reason}", inline=False)
  await ctx.send(embed=embed)
  await member.kick(reason=reason)


@bot.command()
async def help(ctx):
  embed=discord.Embed(title="🗣 | Help", description="Here you find help about the bot!", color=0x002aff)
  embed.set_author(name="#teamhayoto")
  embed.add_field(name="Ban command:", value="!ban {user} {reason}", inline=True)
  embed.add_field(name="Kick command:", value="!kick {user} {reason}", inline=True)
  await ctx.send(embed=embed)


bot.run(token)