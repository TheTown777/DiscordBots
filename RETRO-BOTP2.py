import discord
from discord import member
from discord.ext import commands

bot = commands.Bot(command_prefix = "")


@bot.event
async def on_ready():
   await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="code. Say >help for help."))
print("Online")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def no(ctx):
    await ctx.send('yes')

@bot.command()
async def yes(ctx):
    await ctx.send('no')

@bot.command()
async def wii(ctx):
    await ctx.send('mmm yes the wii beautiful')

@bot.command()
async def dsi(ctx):
    await ctx.send('i miss the dsi shop')


@bot.command()
async def boom(ctx):
    await ctx.send('https://media3.giphy.com/media/oe33xf3B50fsc/giphy.gif')

@bot.command()
async def porn(ctx):
    await ctx.send('https://c.tenor.com/I59BxE--GvsAAAAM/stop-get-some-help.gif')

@bot.command()
async def joke(ctx):
    await ctx.send('hahahahhahahahahhahahhahahahahahahah')

@bot.command()
async def windows(ctx):
    await ctx.send('what version of windows is your favouite')

@bot.command()
async def cool(ctx):
    await ctx.send('@LakeTheImperial#9107 is cool')

bot.run("ODg0NTUyODU4NjEwMDQ0OTU4.YTaKCw.y85ZfO6A6XsqLp0d_SkbsO7soik")
