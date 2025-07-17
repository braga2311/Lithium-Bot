import discord
import random
from discord.ext import commands

class JogosDeAzar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roleta")
    async def roleta(self, ctx):
        """Jogo de roleta russa - 1 chance em 6 de perder"""
        if random.randint(1, 6) == 1:
            await ctx.send("💥 BANG! Você perdeu!")
        else:
            await ctx.send("🔫 *click* Você sobreviveu... desta vez.")

    @commands.command(name="blackjack")
    async def blackjack(self, ctx):
        """Jogo simplificado de blackjack"""
        cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        sua_mao = random.sample(cartas, 2)
        dealer = random.sample(cartas, 2)
        
        msg = f"Suas cartas: {sua_mao} (Total: {sum(sua_mao)})\n"
        msg += f"Dealer mostra: {dealer[0]}"
        
        if sum(sua_mao) == 21:
            msg += "\n🎉 BLACKJACK! Você ganhou!"
        elif sum(sua_mao) > 21:
            msg += "\n💥 Estourou! Você perdeu."
        else:
            msg += "\nDigite `!hit` para mais uma carta ou `!stand` para parar"
        
        await ctx.send(msg)

    @commands.command(name="loteria")
    async def loteria(self, ctx):
        """Sorteia 6 números para loteria"""
        numeros = sorted(random.sample(range(1, 61), 6))  # Corrigido: parêntese fechado
        await ctx.send(f"🎟 Seus números da sorte: {', '.join(map(str, numeros))}")
    
    @commands.command(name="coinflip")
    async def coinflip(self, ctx, escolha: str = None):
        """Cara ou coroa - aposte se quiser"""
        resultado = random.choice(["cara", "coroa"])
        if escolha and escolha.lower() in ["cara", "coroa"]:
            if escolha.lower() == resultado:
                await ctx.send(f"🎉 {resultado.upper()}! Você acertou!")
            else:
                await ctx.send(f"💔 {resultado.upper()}! Você errou...")
        else:
            await ctx.send(f"A moeda caiu em: {resultado.upper()}")

    @commands.command(name="dados")
    async def dados(self, ctx, quantidade: int = 2):
        """Rola vários dados de uma vez"""
        if quantidade > 10:
            await ctx.send("❌ No máximo 10 dados por vez!")
            return
        
        resultados = [random.randint(1, 6) for _ in range(quantidade)]
        await ctx.send(f"🎲 Resultados: {', '.join(map(str, resultados))} (Total: {sum(resultados)})")

async def setup(bot):
    await bot.add_cog(JogosDeAzar(bot))