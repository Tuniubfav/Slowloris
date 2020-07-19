import discord
from discord.ext import commands
import datetime
import random
import json
import os

from urllib import parse, request
import re

bot_prefix ="a!"
bot = commands.Bot(command_prefix=bot_prefix)
bot.remove_command("help")
TOKEN = "NzMyNDI5MTg5MjM5NjY4OTE4.Xw0eCg.umnrxesYMBnMODD4yJCFKuQx484"

@bot.command()
async def ping(ctx):
    await ctx.send('Tu conexión es de...')
    await ctx.send('<a:ping999:732776001469284434> ms')

@bot.command()
async def asd(ctx):
    embed = discord.Embed(
        title=f"Lista de comandos",
        color=discord.Colour(0xe75933),
        description=""
    )

    embed.description="Pta GAA"
    embed.add_field(
        name=f"Aea",
        value=f"aeaaa",
        inline=False
    )
    embed.add_field(
        name=f"sssss",
        value=f"eaeaea",
        inline=False
    )
    embed.set_author(
        name=f" aea",
        icon_url='',
        )
    embed.set_footer(
        text=f"a!ayuda | En el servidor para detalles del bot",
        icon_url='',
        )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Información del servidor de discord actual.", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.add_field(name="Fecha de creación:", value=f" {ctx.guild.created_at}")
    embed.add_field(name="Server ID:", value=f" {ctx.guild.id}", inline=False)
    embed.add_field(name="Creador:", value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Región: ", value=f" {ctx.guild.region}", inline=True)
    embed.add_field(name="Cantidad de miembros:", value=f"{ctx.guild.member_count}", inline=True)
    embed.add_field(name="Nivel de verificación:", value=f"{ctx.guild.verification_level}")
    embed.add_field(name="Mejoras (Boosts):", value=f"{ctx.guild.premium_subscription_count}", inline=False)
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")

    await ctx.send(embed=embed)

@bot.command(aliases=["comandos"])
async def ayuda(ctx):
    embed = discord.Embed(title=f"Lista de comandos", description="Hola, soy un bot nuevo o.0, cuento con cierta cantidad de comandos para tu servicio, espero que te gusten mis funciones, por aquí te dejo mi lista de comandos para que los uses a tu gusto :).", color=discord.Color.blue())
    embed.add_field(name=f"Comandos Divertidos", value=f"`a!say` `a!sayembed` `a!ping`", inline=False)
    embed.add_field(name=f"Comandos de Moderación", value=f"`a!kick` `a!ban` `a!unban` `a!clear`", inline=False)
    embed.add_field(name=f"Comandos Informativos", value=f"`a!serverinfo`", inline=False)
    embed.add_field(name=f"PROXIMAMENTE", value=f"`a!youtube` `a!twitch` `gimages`", inline=False)
    embed.add_field(name=f"Comandos sobre el bot", value=f"`a!help` `a!suggestbot` `a!reportbug` `a!donate` `a!invite`", inline=False)
    embed.set_footer(text=f"Bot desarrollado por Tuniubfav#6325 | Contactar si encuentras algun error.")

    await ctx.send(embed=embed)

@bot.command(aliases=["ayudame"])
async def help(ctx):
    embed = discord.Embed(title=f"Lista de comandos", description="Hola, soy un bot nuevo o.0, cuento con cierta cantidad de comandos para tu servicio, espero que te gusten mis funciones, por aquí te dejo mi lista de comandos para que los uses a tu gusto :).", color=discord.Color.blue())
    embed.add_field(name=f"Comandos Divertidos", value=f"`a!say` `a!sayembed` `a!ping`", inline=False)
    embed.add_field(name=f"Comandos de Moderación", value=f"`a!kick` `a!ban` `a!unban` `a!clear`", inline=False)
    embed.add_field(name=f"Comandos Informativos", value=f"`a!serverinfo`", inline=False)
    embed.add_field(name=f"PROXIMAMENTE", value=f"`a!youtube` `a!twitch` `gimages`", inline=False)
    embed.add_field(name=f"Comandos sobre el bot", value=f"`a!help` `a!suggestbot` `a!reportbug` `a!donate` `a!invite`", inline=False)
    embed.set_footer(text=f"Bot desarrollado por Tuniubfav#6325 | Contactar si encuentras algun error.")

    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)
    print(f"[Mensaje de texto]")
    print(f"{arg}")
    print(f"De: {ctx.author}")
    print(f"Server: {ctx.guild.name}")
    print(f"[Mensaje de texto]")

@bot.command()
async def sayembed(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"{ctx.message.author}", description=f"{arg}", timestamp=datetime.datetime.utcnow(), color=discord.Color.green())
    embed.set_footer(text=f"a!help ")
    print(f"[Mensaje de texto]")
    print(f"{arg}")
    print(f"De: {ctx.author}")
    print(f"Server: {ctx.guild.name}")
    print(f"[Mensaje de texto]")

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(title=f"Acmin BOT", description="Hola! Soy un bot nuevo, no cuento con muchas funciones, pero puedes invitarme a tu servidor por tu cuenta, te ayudare con lo que tenga, si necesitas ayuda o mas información puedes contactar con mi creador Tuniubfav#6325", color=discord.Color.blue())
    embed.add_field(name=f"> Invitación:", value=f"https://discord.com/api/oauth2/authorize?client_id=732429189239668918&permissions=8&scope=bot", inline=False)
    embed.set_image(url=f"https://otakutherapy.com/wp-content/uploads/2016/12/otku_2893a1ab748b1e20.gif")
    embed.set_footer(text=f"Bot desarrollado por Tuniubfav#6325 | Contactar si encuentras algun error.")

    await ctx.send(embed=embed)

@bot.command(aliases=["donar"])
async def donate(ctx):
    embed = discord.Embed(title=f"Acmin BOT", description="Si quieres donar para ayudar a mi creador a que siga programandome, puedes hacerlo depositando dinero a este paypal:", color=discord.Color.green())
    embed.add_field(name=f"> PayPal", value=f"https://paypal.me/JosePazT?locale.x=es_XC", inline=False)
    embed.set_image(url=f"https://i.pinimg.com/originals/12/68/28/126828476cd6caba2b8c4d73cbaba857.gif")
    embed.add_field(name="⠀⠀⠀⠀⠀⠀", value=f"> No es obligatorio donar pero si me seria de mucha ayuda para mi", inline=False)
    embed.set_footer(text=f"Bot desarrollado por Tuniubfav#6325 | Contactar si encuentras algun error.")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    # print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[1])

@bot.command()
async def suggestbot(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    print("-----------[SUGERENCIA]---------")
    print(arg)
    print(f"De: {ctx.author}")
    print(f"Servidor: {ctx.guild.name}")
    print(f"Cantidad de usuarios: {ctx.guild.member_count}")
    print("-----------[SUGERENCIA]---------")
    await ctx.send(f"**Gracias por tu sugerencia `{ctx.author}`, en unos momentos lo estara leyendo mi creador** <a:verificado:733766251133927524>")

@bot.command()
async def reportbug(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    print("-----------[REPORTE]---------")
    print(arg)
    print(f"De: {ctx.author}")
    print(f"Servidor: {ctx.guild.name}")
    print(f"Cantidad de usuarios: {ctx.guild.member_count}")
    print("-----------[REPORTE]---------")
    await ctx.send(f"**Gracias por tu reporte `{ctx.author}`, estare trabajando en ello para arreglarlo** <a:verificado:733766251133927524>")

#moderación

@bot.command()
@commands.has_permissions(ban_members=True)
async def announce(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f"   {ctx.guild.name}  ", description=f"{arg}", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
    embed.set_footer(text=f"{ctx.author}")

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"<a:SSS:732790339449913364> {member.mention} `ha sido baneado correctamente de:` **{ctx.guild.name}**")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"<a:SSS:732790339449913364> {member.mention} `ha sido expulsado correctamente de:` **{ctx.guild.name}**")

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"<a:SSS:732790339449913364> **Usuario correctamente perdonado** `{user.name}#{user.discriminator}`")

@bot.command()
@commands.has_permissions(manage_guild=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"<a:SSS:732790339449913364> **{amount} mensaje`s eliminados**")
    await ctx.channel.purge(limit=1)

#Errores
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:Not:732791695904866359> Coloca la cantidad de mensajes que quieres eliminar")
        await ctx.send("<a:arrow_rightt:732777439679348877> `¬|Ejemplo: a!clear 100`")

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:Not:732791695904866359> Coloca el mensaje que quieres enviar")
        await ctx.send("<a:arrow_rightt:732777439679348877> `¬|Ejemplo: a!say Hola, que tal!`") 

@sayembed.error
async def sayembed_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:Not:732791695904866359> Coloca el mensaje que quieres enviar")
        await ctx.send("<a:arrow_rightt:732777439679348877> `¬|Ejemplo: a!sayembed Hola, que tal!`") 

@suggestbot.error
async def suggestbot_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:Not:732791695904866359> Coloca la sugerencia del bot que quieres enviar")

@reportbug.error
async def reportbug_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("<a:Not:732791695904866359> Coloca el reporte que quieres enviar")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" <a:Not:732791695904866359> **Por favor mencione al miembro**")
        await ctx.send("<a:arrow_rightt:732777439679348877> `¬|Ejemplo: a!kick Tuniubfav#6325 Limite de advertencias`")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" <a:Not:732791695904866359> **Por favor mencione al miembro**")
        await ctx.send("<a:arrow_rightt:732777439679348877> `¬|Ejemplo: a!ban Tuniubfav#6325 Insultos al servidor`")

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(" <a:Not:732791695904866359> **Por favor mencione al miembro baneado**")
        await ctx.send("<a:arrow_rightt:732777439679348877> `¬|Ejemplo: a!unban Tuniubfav#6325`")

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=" a!help | versión BETA 1.0"))
    print('Estoy devuelta!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("<a:dinosaurioerror:733749658966425671> Comando desconocido")

@bot.event
async def on_member_join(member):
    from time import sleep
    embed = discord.Embed(
        title=f"¡Bienvenido {member.display_name}!",
        color=discord.Colour(0xe75933),
        description=""
    )

    embed.description=f"Hola usuario, acabas de unirte al servidor **{member.guild}**                                                                                                               Recuerda respetar las reglas del servidor."
    embed.set_thumbnail(url=f"{member.guild.icon_url}")
    embed.set_author(
        name=f" {member.guild}",
        icon_url='',
        )
    embed.set_footer(
        text=f"a!ayuda | En el servidor para detalles del bot",
        icon_url='',
        )
    embed.timestamp = datetime.datetime.utcnow()
    await member.send(embed=embed)


bot.run(TOKEN)
