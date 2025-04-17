import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Cria o bot com prefixo '!'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} entrou no Discord.')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Pega o token do Discord do arquivo .env
bot.run(os.getenv('MTM1ODY0NTAwMzA0NzQwMzU0MA.GHZxil.D44JiG7_sQSgtASiTy_XvO5a4vDr6bpkPO6x4g'))
