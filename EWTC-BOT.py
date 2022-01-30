import discord
from discord import member
from discord.ext import commands

bot = commands.Bot(command_prefix = ">")
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="your commands. Say >help for help"))
    print("bot is loaded and ready")

@bot.group(invoke_without_command=True)
async def help(ctx):
    
    em = discord.Embed(title = "Help", description = "Use >help <command> for more info on the specified command.",color = ctx.author.color)

    em.add_field(name = "Moderation", value = "kick, ban, warn")
    em.add_field(name = "Fun", value = "cat, dmsay, hamburger, kill, dog, spam")
    em.add_field(name = "Other", value = "invite, supportserver, about")
    await ctx.send(embed = em)

@help.command()
async def warn(ctx):
    
    em = discord.Embed(title = "Warn", description = "Warns a member for the specified reason",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">warn <member> <reason>")
    await ctx.send(embed = em)

@help.command()
async def kill(ctx):
    
    em = discord.Embed(title = "Kill", description = "Kills a Member.",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">kill <member>")
    await ctx.send(embed = em)

@help.command()
async def dog(ctx):
    
    em = discord.Embed(title = "Dog", description = "Shows a cute pic of a dog.",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">dog")
    await ctx.send(embed = em)

@help.command()
async def spam(ctx):
    
    em = discord.Embed(title = "Spam", description = "Spams the word SPAM for a very long time. Only admins can use this command.",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">spam")
    await ctx.send(embed = em)



@help.command()
async def kick(ctx):
    
    em = discord.Embed(title = "Kick", description = "Kicks a member from the guild for the specified reason",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">kick <member> <reason>")
    await ctx.send(embed = em)

@help.command()
async def ban(ctx):
    
    em = discord.Embed(title = "Ban", description = "Bans a member from the guild for the specified reason",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">ban <member> <reason>")
    await ctx.send(embed = em)

@help.command()
async def cat(ctx):
    
    em = discord.Embed(title = "Cat", description = "Shows cat images, has some easter eggs too",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">cat <value>")
    em.add_field(name = "Valid Arguments", value = "cute, scream, floppa (wth is a floppa), girl")
    await ctx.send(embed = em)

@help.command()
async def dmsay(ctx):
   
    em = discord.Embed(title = "DMSay", description = "DM's you whatever you want.",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">dmsay <what you want it to say>")
    await ctx.send(embed = em)

@help.command()

async def hamburger(ctx):
    em = discord.Embed(title = "hambruger", description = "Hamburger.",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">hamburger")
    await ctx.send(embed = em)

@help.command()
async def invite(ctx):
    em = discord.Embed(title = "Invite", description = "Shows the bot invite",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">invite")
    await ctx.send(embed = em)

@help.command()
async def about(ctx):
    em = discord.Embed(title = "About", description = "It shows the credits",color = ctx.author.color)
    em.add_field(name = "Usage", value = ">about")
    await ctx.send(embed = em)


@bot.command()
async def supportserver(ctx):
    await ctx.channel.send("https://discord.gg/xJTKWHUhhR")

@bot.command()
async def invite(ctx):
    channel = ctx.channel
    await channel.send("https://discord.com/api/oauth2/authorize?client_id=883090457582772264&permissions=8&scope=bot")

@bot.command()
async def cat(ctx, arg=None):
    if arg == "cute":
        await ctx.channel.send("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhddesktopwallpapers.in%2Fwp-content%2Fuploads%2F2015%2F08%2Fkitten-cute-adorable.jpg&f=1&nofb=1")



    if arg == "scream":

        await ctx.channel.send("https://cdn.discordapp.com/attachments/881609095776440361/882925762766856192/unknown.png")

    if arg == "floppa":
        await ctx.channel.send("WAT IS A FLOPPA")

    if arg == "girl":
        await ctx.channel.send("WAT THA HEK MAHN WAY DO U WAN ME TO SAEY THGAT")
        
    

    if arg != "scream" and arg != "cute" and arg != "floppa" and arg != "girl":
        await ctx.channel.send("what?")




   


@bot.command()
async def dmsay(ctx, *, say=None):
    if say != None:
        try:
            await ctx.message.author.send(say)
            await ctx.channel.send("i sent it i hope its nothing bad")
        except:
            await ctx.channel.send("Fail")
    else:
        await ctx.channel.send("HAY I CANT SAND NOTHANG")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason="thay didnt tall meh what to say ahm thas is akward "):
    await member.send(f"OH U HAV BEN KICKED 4 {reason}")
    await member.kick(reason=reason)
    await ctx.channel.send("I KICKED" + str(member) + " 4 " + str(reason))

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason="thay didnt tall meh what to say ahm thas is akward "):
    await member.send(f"you... gat baned 4 {reason}")
    await member.ban(reason=reason)
    await ctx.channel.send("i banned " + str(member) + " for " + str(reason))

@bot.command()
async def hamburger(ctx):
    await ctx.channel.send("https://media.giphy.com/media/5y2zBKjMF1TEI/giphy.gif?cid=ecf05e47ft2j00zbwuae2ta36jmutkm3hiwuaoehvswaf9rz&rid=giphy.gif&ct=g")

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason="thay dod nat tall me wat to sey"):
    if member == ctx.author:
        await ctx.channel.send("hey i cant realy warn you or ban you or kick you crazy right?")
    else:
        await member.send(f"u gat warned 4 {reason}")
        await ctx.channel.send("i warned " + str(member) + " 4 " + str(reason))

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, reason="thay did not tall me wet to say"):
    await member.unban(reason=reason)
    await ctx.channel.send("i warned " + str(member) + " cuz they did " + str(reason))

@bot.command()
async def owner(ctx):
    channel = ctx.channel
    await channel.send("coding is hard") 

@bot.command()
async def meow(ctx):
    channel = ctx.channel
    await channel.send("meow")


@bot.group(invoke_without_command=True)
async def about(ctx):
    
    em = discord.Embed(title = "About", description = "About me",color = ctx.author.color)

    em.add_field(name = "Owners of the bot", value = "AstralCat1 and TheTown777")
    em.add_field(name = "What is the bot for", value = "My friends Server")
    em.add_field(name = "what did astralcat1 do", value = "He made the code then TheTown777 edited it to make it fit the server more")
    await ctx.send(embed = em)

@bot.command()
async def kill(ctx):
    channel = ctx.channel
    await channel.send("ok i killed them")


@bot.command()
async def dog(ctx):
    channel = ctx.channel
    await channel.send("woof")
    await channel.send("https://cdn.discordapp.com/attachments/884497235960799338/884500046891077712/2Q.png")

@bot.command()
async def windows_7(ctx):
    channel = ctx.channel
    await channel.send("https://cdn.discordapp.com/attachments/882961743582756907/884541774125731920/2C6102E9-704D-4B16-B1C2-FDF7E110E6BB.png")


@bot.command()
@commands.has_permissions(ban_members=True)
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
 
@bot.command()
async def stop(ctx):
    channel = ctx.channel
    await channel.send("NO!1!")

@bot.command()
async def good_bot(ctx):
    channel = ctx.channel
    await channel.send(":D")

bot.run("tokenbruv")
