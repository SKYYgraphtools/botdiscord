from email import message
from json import JSONDecodeError
from pydoc import TextRepr
import discord
from discord.ext import commands
import asyncio
bot = commands.Bot(command_prefix = "+" , description = "skyy bot")

@bot.event
async def on_ready():
    print("ready!")

@bot.command()
async def support(ctx):
    await ctx.send ("https://discord.gg/xMvNReH8eE")
@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    numbertc = len(server.text_channels)
    numberVc = len(server.voice_channels)
    serverdes = server.description 
    numberp = server.member_count
    servern = server.name
    message =f"le server **{servern}** contient *{numberp}*  personne . \n la description du serveur {serverdes}. \n ce serveur possede {numbertc} salons ecrit ansi que {numberVc} vocaux." 
    await ctx.send(message)
@bot.command()
async def me(ctx):
    server = ctx.guild
    servern = server.name
    await ctx.send(f""" bonjour je suis 𝐴𝐷𝑁#0001 tu est sur le serv **{servern}** proteger par mon bot [+] Protecte \n 
     mon github - https://github.com/SKYYgraphtools/ddoos.skyy.grpah.grab""")

@bot.command()
async def say(ctx , *texte):
    await ctx.send(" ".join(texte))


@bot.command()
async def translate(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append(" ")
	await ctx.send("".join(chineseText))



@bot.command()
async def getinfoNcv(ctx):
    server = ctx.guild
    numberVc = len(server.voice_channels)
    message = f"**le nombre de channels vocal est { numberVc}**"
    await ctx.send(message)

@bot.command()
async def clear (ctx, nombre: int):
    message = await ctx.channel.history(limit = nombre + 1  ).flatten()
    for message in message:
        await message.delete()


@bot.command()
async def kick (ctx, user : discord.User, *reason):
    reason = "".join(reason)
    await ctx.guild.kick(user, reason = reason )
    await ctx.send(f"{user} a été kick pour raison : {reason}")


@bot.command()
async def ban(ctx, user : discord.User, *reason):
    reason = "".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} a été ban  pour raison : {reason}")
        
@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")























bot.run("OTg5MDczNjc4OTEyMzM5OTY5.GRP_5o.Hwtq6sUY-9V4KmPhHnz9mp7Vz6Agh4FRl0neQQ")

