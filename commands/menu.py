from discord.ext import commands
import discord

class Menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="menu")
    async def menu(self, ctx):
        embed = discord.Embed(
            title="📜 Menu de Comandos do Bot",
            description="Abaixo estão todos os comandos disponíveis, organizados por categoria.",
            color=discord.Color.blurple()
        )

        # Comandos administrativos
        embed.add_field(
            name="🔧 Administração",
            value=(
                "`!ping` - Ver latência do bot\n"
                "`!kick @usuário` - Expulsar membro\n"
                "`!ban @usuário` - Banir membro\n"
                "`!unban Nome#1234` - Desbanir membro\n"
                "`!mute @usuário` - Silenciar usuário\n"
                "`!unmute @usuário` - Remover silêncio\n"
                "`!clear [n]` - Limpar mensagens\n"
                "`!slowmode [s]` - Ativar slowmode\n"
                "`!lock` - Trancar canal\n"
                "`!unlock` - Destrancar canal"
            ),
            inline=False
        )

        # Consultas públicas
        embed.add_field(
            name="🔍 Consultas Públicas",
            value=(
                "`!cpf [número]` - Validar CPF\n"
                "`!cep [xxxxx-xxx]` - Buscar CEP\n"
                "`!cnpj [número]` - Buscar CNPJ\n"
                "`!ip [endereço]` - Info sobre IP\n"
                "`!ddd [código]` - Info sobre DDD\n"
                "`!bin [número]` - Info de cartão (BIN)\n"
                "`!telefone [+55...]` - Verificar telefone\n"
                "`!nome_estado [UF]` - Nome do estado\n"
                "`!moeda` - Cotação do dólar/euro/bitcoin\n"
                "`!clima [cidade]` - Clima (em breve)"
            ),
            inline=False
        )

        # Geração de documentos
        embed.add_field(
            name="📄 Geração de Documentos (Testes)",
            value=(
                "`!gerarcpf` - CPF válido e formatado\n"
                "`!gerarcnh` - CNH com DV válido\n"
                "`!gerarcep` - CEP possível\n"
                "`!gerartitulo` - Título de eleitor válido\n"
                "`!gerartudo` - Gera todos os documentos juntos"
            ),
            inline=False
        )

        # Jogos de azar
        embed.add_field(
            name="🎰 Jogos de Azar",
            value=(
                "`!cassanic` - Sorteio com frutas 🍉🍒\n"
                "`!dado [1-6]` - Jogue um dado 🎲\n"
                "`!dados [qtd]` - Rola vários dados\n"
                "`!jogodobicho` - Sorteio de animais 🐶🐱🐯\n"
                "`!roleta` - Roleta russa (1 chance em 6)\n"
                "`!blackjack` - Jogo simplificado\n"
                "`!loteria` - Gera números da sorte\n"
                "`!coinflip [cara/coroa]` - Cara ou coroa"
            ),
            inline=False
        )

        # Interação
        embed.add_field(
            name="😄 Brincadeiras & Interação",
            value=(
                "`!beijo @usuário` - Manda um beijo\n"
                "`!tapa @usuário` - Dá um tapa virtual\n"
                "`!ship @user1 @user2` - Teste de compatibilidade\n"
                "`!votar [pergunta]` - Cria uma votação\n"
                "`!escolha [opções]` - Escolhe por você"
            ),
            inline=False
        )

        # Utilidades
        embed.add_field(
            name="🛠️ Utilidades",
            value=(
                "`!avatar [@usuário]` - Mostra o avatar\n"
                "`!userinfo [@usuário]` - Informações do usuário\n"
                "`!serverinfo` - Informações do servidor\n"
                "`!lembrete [minutos] [msg]` - Define lembrete\n"
                "`!convite` - Gera convite do servidor"
            ),
            inline=False
        )

        # Imagens
        embed.add_field(
            name="🖼️ Imagens",
            value=(
                "`!meme` - Meme aleatório\n"
                "`!gato` - Foto de gato aleatória\n"
                "`!cachorro` - Foto de cachorro aleatória\n"
                "`!artista` - Gera 'arte' abstrata\n"
                "`!qr [texto]` - Gera QR Code"
            ),
            inline=False
        )

        embed.set_footer(text="Se possível, siga o desenvolvedor no Instagram: @braga12737")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Menu(bot))
