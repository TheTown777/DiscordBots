
import discord
from discord.ext import commands,tasks
from discord import member
import os
from dotenv import load_dotenv
import youtube_dl

bot = commands.Bot(command_prefix = ">")
bot.remove_command("help")

@bot.event
async def on_ready():
   await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name="code. Say >help for help."))
print("Online")

@bot.group(invoke_without_command=True)
async def help(ctx):
    
    em = discord.Embed(title = "Help", description = "Use /help <command> for more info on the specified command. All Commands are lowercase.",color = ctx.author.color)

    em.add_field(name = "Moderation", value = "kick, ban, warn")
    em.add_field(name = "Fun", value = "cat, dmsay, hamburger, dog, spam, kill")
    em.add_field(name = "Other", value = "invite, supportserver, about")
    await ctx.send(embed = em)

@help.command()
async def warn(ctx):
    
    em = discord.Embed(title = "Warn", description = "Warns a member for the specified reason",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/warn <member> <reason>")
    await ctx.send(embed = em)

@help.command()
async def kill(ctx):
    
    em = discord.Embed(title = "Kill", description = "I will kill a member",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/kill <member>")
    await ctx.send(embed = em)

@help.command()
async def kick(ctx):
    
    em = discord.Embed(title = "Kick", description = "Kicks a member from the guild for the specified reason",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/kick <member> <reason>")
    await ctx.send(embed = em)

@help.command()
async def ban(ctx):
    
    em = discord.Embed(title = "Ban", description = "Bans a member from the guild for the specified reason",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/ban <member> <reason>")
    await ctx.send(embed = em)

@help.command()
async def cat(ctx):
    
    em = discord.Embed(title = "Cat", description = "Shows cat images, has some easter eggs too",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/cat <value>")
    em.add_field(name = "Valid Arguments", value = "cute, scream, floppa (wth is a floppa), girl")
    await ctx.send(embed = em)

@help.command()
async def dmsay(ctx):
   
    em = discord.Embed(title = "DMSay", description = "DM's you whatever you want.",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/dmsay <what you want it to say>")
    await ctx.send(embed = em)

@help.command()
async def spam(ctx):
   
    em = discord.Embed(title = "Spam", description = "Spams the words SPAM 103 times.",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/spam")
    await ctx.send(embed = em)

@help.command()
async def about(ctx):
   
    em = discord.Embed(title = "About", description = "Shows about the bot",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/about")
    await ctx.send(embed = em)

@help.command()

async def hamburger(ctx):
    em = discord.Embed(title = "hambruger", description = "Hamburger.",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/hamburger")
    await ctx.send(embed = em)

@help.command()
async def invite(ctx):
    em = discord.Embed(title = "Invite", description = "Shows the bot invite",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/invite")
    await ctx.send(embed = em)

@help.command()
async def dog(ctx):
    em = discord.Embed(title = "dog", description = "It shows a cute picture of a dog (wanted by my friend)",color = ctx.author.color)
    em.add_field(name = "Usage", value = "/dog")
    await ctx.send(embed = em)


@bot.command()
async def supportserver(ctx):
    await ctx.channel.send("https://discord.gg/xJTKWHUhhR")

@bot.command()
async def invite(ctx):
    channel = ctx.channel
    await channel.send("https://discord.com/api/oauth2/authorize?client_id=884552858610044958&permissions=8&scope=bot")

@bot.command()
async def cat(ctx, arg=None):
    if arg == "cute":
        await ctx.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhddesktopwallpapers.in%2Fwp-content%2Fuploads%2F2015%2F08%2Fkitten-cute-adorable.jpg&f=1&nofb=1")



    if arg == "scream":

        await ctx.channel.send("https://cdn.discordapp.com/attachments/881609095776440361/882925762766856192/unknown.png")

    if arg == "floppa":
        await ctx.channel.send("Someone TELL ME WHAT THE HECK IS A FLOPPA")

    if arg == "girl":
        await ctx.channel.send("wth NO weido")
        
    

    if arg != "scream" and arg != "cute" and arg != "floppa" and arg != "girl":
        await ctx.channel.send("???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")


    if arg != "wii" and arg != "cute" and arg != "floppa" and arg != "girl":
        await ctx.channel.send("???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")



   


@bot.command()
async def dmsay(ctx, *, say=None):
    if say != None:
        try:
            await ctx.message.author.send(say)
            await ctx.channel.send("Sent")
        except:
            await ctx.channel.send("Failed Succsesfully")
    else:
        await ctx.channel.send("Hey i cant send NOTHING or images :C my brain is not fancy to have IMAGE only links to images ok?")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="no reason provided"):
    await member.send(f"You have been kicked for {reason} Please be nicer")
    await member.kick(reason=reason)
    await ctx.channel.send("Kicked" + str(member) + " Because" + str(reason))

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="no reason provided "):
    await member.send(f"You have been banned for {reason}. Please never comeback.")
    await member.ban(reason=reason)
    await ctx.channel.send("Banned " + str(member) + " for " + str(reason))

@bot.command()
async def hamburger(ctx):
    await ctx.channel.send("https://media.giphy.com/media/5y2zBKjMF1TEI/giphy.gif?cid=ecf05e47ft2j00zbwuae2ta36jmutkm3hiwuaoehvswaf9rz&rid=giphy.gif&ct=g")

@bot.command()
async def wii_u(ctx):
    await ctx.channel.send("https://media.giphy.com/media/esVOIs6Fyj1gLxW7LP/giphy.gif")

@bot.command()
async def dance(ctx):
    await ctx.channel.send("https://media.giphy.com/media/RTVur5J0hr1dWiIdZf/source.gif?cid=ecf05e47ynb8fls7wk0thdhbynr9o9q2ejb6dq0fs0yiaj84&rid=source.gif&ct=g")


@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason="no reason provided"):
    if member == ctx.author:
        await ctx.channel.send("I cannot warn you. Choose someone else.")
    else:
        await member.send(f"You have been warned for {reason}")
        await ctx.channel.send("Warned " + str(member) + " 4 " + str(reason))

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, reason="no reason provided"):
    await member.unban(reason=reason)
    await ctx.channel.send("Unbanned " + str(member) + " because " + str(reason))



@bot.group(invoke_without_command=True)
async def about(ctx):
    
    em = discord.Embed(title = "About", description = "About me",color = ctx.author.color)

    em.add_field(name = "Owners of the bot", value = "AstralCat1 and TheTown777")
    em.add_field(name = "What is the bot for", value = "Realy everything you can do whatever")
    await ctx.send(embed = em)

@bot.command()
async def kill(ctx):
    channel = ctx.channel
    await channel.send("Ok They died")
    


@bot.command()
async def dog(ctx):
    channel = ctx.channel
    await channel.send("woof")
    await channel.send("(this was a cmd wanted by my friend)")
    await channel.send("https://cdn.discordapp.com/attachments/884497235960799338/884500046891077712/2Q.png")

@bot.command()
async def windows_7(ctx):
    channel = ctx.channel
    await channel.send("https://cdn.discordapp.com/attachments/882961743582756907/884541774125731920/2C6102E9-704D-4B16-B1C2-FDF7E110E6BB.png")


@bot.command()
async def spam(ctx):
    channel = ctx.channel
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")
    await channel.send("spam")

#music
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@bot.command(name='play_song', help='To play song')
async def play(ctx,url):
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))



@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "general" :
                await channel.send('hello am now online')
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))
if __name__ == "__main__" :
    bot.run("token")  
     
