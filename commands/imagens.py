import discord
from discord.ext import commands
import random

class Imagens(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="meme")
    async def meme(self, ctx):
        """Mostra um meme aleatório"""
        memes = [
            "https://i.imgur.com/9EEmSaJ.jpg",
            "https://i.imgur.com/5DRzpb4.jpg",
            "https://i.imgur.com/3ZQwg5V.jpg",
            "https://i.imgur.com/2ZvJZ4Q.jpg",
            "https://i.imgur.com/8J7nK6L.jpg"
        ]
        embed = discord.Embed(title="😂 Meme aleatório", color=0xFF9900)
        embed.set_image(url=random.choice(memes))
        await ctx.send(embed=embed)

    @commands.command(name="gato")
    async def gato(self, ctx):
        """Mostra uma foto aleatória de gato"""
        embed = discord.Embed(title="🐱 Miau!", color=0xFF9900)
        embed.set_image(url=f"https://cataas.com/cat?random={random.randint(1,1000)}")
        await ctx.send(embed=embed)

    @commands.command(name="cachorro")
    async def cachorro(self, ctx):
        """Mostra uma foto aleatória de cachorro"""
        embed = discord.Embed(title="🐶 Au au!", color=0xFF9900)
        embed.set_image(url=f"https://placedog.net/500/300?random={random.randint(1,1000)}")
        await ctx.send(embed=embed)

    @commands.command(name="artista")
    async def artista(self, ctx):
        """Gera uma 'obra de arte' abstrata"""
        cores = ["FF0000", "00FF00", "0000FF", "FFFF00", "FF00FF", "00FFFF"]
        cor1, cor2 = random.sample(cores, 2)
        embed = discord.Embed(title="🎨 Obra de arte gerada", color=0xFF9900)
        embed.set_image(url=f"https://singlecolorimage.com/get/{cor1}/500x300")
        embed.add_field(name="Cores usadas", value=f"#{cor1} e #{cor2}")
        await ctx.send(embed=embed)

    @commands.command(name="qr")
    async def qr(self, ctx, *, texto: str):
        """Gera um QR Code com o texto fornecido"""
        texto = texto.replace(" ", "%20")
        embed = discord.Embed(title="📲 QR Code gerado", color=0x7289DA)
        embed.set_image(url=f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={texto}")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Imagens(bot))