import discord
from discord.ext import commands
from bot_logic import gen_pass
import random
#creacion y configuracion de los permisos
permisos=discord.Intents.default()
permisos.message_content=True

#creacion del bot
bot = commands.Bot(command_prefix="/",intents=permisos)

#eventos
@bot.event
async def on_ready():
    print("El bot esta en linea")

@bot.command()
async def hola(ctx):
    await ctx.send(f"Hola mi nombre es {bot.user.name}")

@bot.command()
async def adios(ctx):
    await ctx.send(f"Hasta luego {ctx.author.mention}, espero que te haya sido de ayuda")

@bot.command()
async def lanzar_moneda(ctx):
    resultado = random.choice(['Cara', 'Cruz']) 
    await ctx.send(f'{ctx.author.mention} lanzó la moneda y salió: **{resultado}**')

@bot.command()
async def generador(ctx, longitud: int):
    if longitud <= 0:
        await ctx.send("La longitud debe ser un número positivo.")
        return
    contraseña = gen_pass(longitud)
    await ctx.send(f"Contraseña generada: {contraseña}")

bot.run("MTQwMTU3NDg3NDY2MDczMzAxOQ.GltOUp.YLxPZT96r1AioaI8Vi2tG6BNodtxql2ri-NGWg")
