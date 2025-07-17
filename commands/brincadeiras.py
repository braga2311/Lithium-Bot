import discord
import random
from discord.ext import commands

class Brincadeiras(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="beijo")
    async def beijo(self, ctx, membro: discord.Member):
        """Manda um beijo para alguém"""
        beijos = ["😘", "💋", "😚", "🥰", "😍"]
        await ctx.send(f"{random.choice(beijos)} {membro.mention}, você recebeu um beijo de {ctx.author.mention}!")

    @commands.command(name="tapa")
    async def tapa(self, ctx, membro: discord.Member):
        """Dá um tapa virtual em alguém"""
        tapas = ["👋", "✋", "🤚", "🖐️", "🤛", "🤜"]
        await ctx.send(f"{random.choice(tapas)} {membro.mention} levou um tapa de {ctx.author.mention}!")

    @commands.command(name="ship")
    async def ship(self, ctx, pessoa1: discord.Member, pessoa2: discord.Member):
        """Verifica a compatibilidade de um casal"""
        porcentagem = random.randint(0, 100)
        cor = 0xFF0000 if porcentagem < 30 else 0xFFFF00 if porcentagem < 70 else 0x00FF00
        
        embed = discord.Embed(
            title="💝 Teste de Compatibilidade",
            description=f"{pessoa1.display_name} ❤ {pessoa2.display_name}",
            color=cor
        )
        embed.add_field(name="Resultado", value=f"{porcentagem}% de compatibilidade!")
        
        if porcentagem > 80:
            embed.set_footer(text="Casamento marcado!")
        elif porcentagem > 50:
            embed.set_footer(text="Dá pra tentar!")
        else:
            embed.set_footer(text="Melhor nem começar...")
        
        await ctx.send(embed=embed)

    @commands.command(name="votar")
    async def votar(self, ctx, *, pergunta: str):
        """Cria uma votação rápida"""
        embed = discord.Embed(
            title=f"📊 {pergunta}",
            description="Reaja com 👍 ou 👎 para votar!",
            color=0x7289DA
        )
        embed.set_footer(text=f"Votação criada por {ctx.author.display_name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")

    @commands.command(name="escolha")
    async def escolha(self, ctx, *opcoes: str):
        """Escolhe uma opção aleatória para você"""
        if len(opcoes) < 2:
            await ctx.send("❌ Forneça pelo menos 2 opções!")
            return
        
        await ctx.send(f"🤔 Eu escolho: **{random.choice(opcoes)}**")

async def setup(bot):
    await bot.add_cog(Brincadeiras(bot))