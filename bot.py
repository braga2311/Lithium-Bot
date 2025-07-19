import os
import discord
from discord.ext import commands
import asyncio

TOKEN = "MTEwNz...coloque_seu_token_aqui..."
COMMAND_PREFIX = "!"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Conectado como {bot.user}")

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and not filename.startswith("__"):
            try:
                await bot.load_extension(f"commands.{filename[:-3]}")
                print(f"✅ Comando {filename} carregado.")
            except Exception as e:
                print(f"❌ Erro ao carregar {filename}: {e}")

async def main():
    await load_extensions()
    await bot.start(TOKEN)

asyncio.run(main())
