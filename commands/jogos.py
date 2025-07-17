import discord
import random
from discord.ext import commands

# Classe principal do cog de jogos
class Jogos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  # guarda referência ao bot principal

    # Comando !cassanic — Sorteio com emojis de frutas
    @commands.command(name="cassanic")
    async def cassanic(self, ctx):
        # Lista de emojis de frutas que podem ser sorteados
        frutas = ['🍎', '🍌', '🍉', '🍇', '🍒', '🍍', '🥝', '🌶️']

        # Sorteamos 4 frutas aleatórias (podem repetir)
        resultado = random.choices(frutas, k=4)

        # Juntamos as frutas em uma string para exibir
        linha = ''.join(resultado)

        # Verifica se todas as frutas sorteadas são iguais (ex: 🍌🍌🍌🍌)
        ganhador = len(set(resultado)) == 1

        # Monta a mensagem com base no resultado
        if ganhador:
            msg = f"{linha} 🎉 Você venceu! Sorte pura!"
        else:
            msg = f"{linha} Infelizmente você não ganhou..."

        # Envia o resultado para o canal
        await ctx.send(msg)

    # Comando !dado <número> — você escolhe e tenta acertar o dado
    @commands.command(name="dado")
    async def dado(self, ctx, escolha: int):
        # Validação: só aceita números entre 1 e 6
        if escolha < 1 or escolha > 6:
            await ctx.send("❌ Escolha um número entre 1 e 6.")
            return

        # Suspense...
        await ctx.send("🎲 Girando dado...")

        # Sorteia um número aleatório entre 1 e 6
        numero = random.randint(1, 6)

        # Compara com a escolha do usuário
        if numero == escolha:
            await ctx.send(f"✅ Dado caiu no número {numero}! Você venceu!")
        else:
            await ctx.send(f"Dado caiu no número {numero}... Infelizmente você não ganhou.")

    # Comando !jogodobicho — Sorteia 3 bichos, se forem iguais, você ganha
    @commands.command(name="jogodobicho")
    async def jogodobicho(self, ctx):
        # Lista de tuplas com emojis e nomes dos bichos
        bichos = [
            ("🐶", "Cachorro"), ("🐱", "Gato"), ("🦁", "Leão"),
            ("🐮", "Vaca"), ("🐷", "Porco"), ("🐵", "Macaco"),
            ("🐰", "Coelho"), ("🐯", "Tigre"), ("🐸", "Sapo"), ("🐔", "Galo")
        ]

        # Sorteia 3 bichos aleatórios (podem repetir)
        sorteados = random.choices(bichos, k=3)

        # Junta só os emojis para mostrar o resultado
        linha = ' '.join([b[0] for b in sorteados])

        # Verifica se os três bichos sorteados têm o mesmo nome (ex: 🐶🐶🐶)
        ganhou = len(set([b[1] for b in sorteados])) == 1

        # Mensagem de vitória ou fracasso
        if ganhou:
            msg = f"{linha} 🎉 Você venceu com 3x **{sorteados[0][1]}**!"
        else:
            msg = f"{linha} Não foi dessa vez... tente de novo!"

        # Envia a mensagem no canal
        await ctx.send(msg)

# Função padrão para adicionar o cog ao bot
async def setup(bot):
    await bot.add_cog(Jogos(bot))