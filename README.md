# Lithium Bot - Documentação Técnica

![Badge Status](https://img.shields.io/badge/Status-Ativo-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Discord.py](https://img.shields.io/badge/discord.py-2.0%2B-blue)

## Visão Geral

O Lithium Bot é um bot para Discord desenvolvido em Python utilizando a biblioteca `discord.py`. Sua arquitetura modular permite fácil expansão de funcionalidades através do sistema de Cogs.

## Estrutura do Projeto

```
Lithium-Bot/
├── commands/
│   ├── admin.py
│   ├── brincadeiras.py
│   ├── consultas.py
│   ├── imagens.py
│   ├── jogos.py
│   ├── jogos-azar.py
│   ├── menu.py
│   └── utilidades.py
├── config.py
└── bot.py
```

## Como Criar Novos Comandos

### 1. Criando um novo arquivo de comandos

Na pasta `commands`, crie um novo arquivo Python (ex: `meu_comando.py`) com a seguinte estrutura básica:

```python
from discord.ext import commands

class MeuComando(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nomecomando")
    async def comando(self, ctx, *args):
        """Descrição do comando que aparece no !help"""
        # Implementação do comando aqui
        await ctx.send("Resposta do comando")

async def setup(bot):
    await bot.add_cog(MeuComando(bot))
```

### 2. Adicionando ao menu de ajuda

Edite o arquivo `menu.py` para incluir seu novo comando na seção apropriada:

```python
embed.add_field(
    name="Categoria do Comando",
    value=(
        # Comandos existentes...
        "`!nomecomando` - Descrição breve do comando\n"
    ),
    inline=False
)
```

### 3. O bot carregará automaticamente

O sistema de carregamento automático em `bot.py` já detectará seu novo arquivo na próxima reinicialização:

```python
async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and not filename.startswith("__"):
            await bot.load_extension(f"commands.{filename[:-3]}")
```

## Tipos de Comandos

### Comandos Básicos

```python
@commands.command(name="ping")
async def ping(self, ctx):
    """Verifica a latência do bot"""
    await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
```

### Comandos com Argumentos

```python
@commands.command(name="echo")
async def echo(self, ctx, *, mensagem: str):
    """Repete a mensagem enviada"""
    await ctx.send(mensagem)
```

### Comandos com Permissões

```python
@commands.has_permissions(kick_members=True)
@commands.command(name="kick")
async def kick(self, ctx, member: discord.Member, *, reason=None):
    """Expulsa um membro do servidor"""
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} foi expulso.")
```

## Exemplo Completo

`commands/exemplo.py`:
```python
from discord.ext import commands
import random

class Exemplo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dado")
    async def dado(self, ctx, lados: int = 6):
        """Rola um dado com o número de lados especificado"""
        if lados < 2:
            await ctx.send("O dado deve ter pelo menos 2 lados")
            return
        
        resultado = random.randint(1, lados)
        await ctx.send(f"🎲 Resultado: {resultado}")

async def setup(bot):
    await bot.add_cog(Exemplo(bot))
```

Adicione em `menu.py`:
```python
embed.add_field(
    name="Jogos",
    value=(
        # Outros comandos...
        "`!dado [lados]` - Rola um dado com N lados\n"
    ),
    inline=False
)
```

## Requisitos Técnicos

- Python 3.8 ou superior
- Bibliotecas:
  - discord.py >= 2.0
  - requests (para comandos de API)
- Token de bot Discord válido

## Configuração

1. Configure as variáveis:
```
DISCORD_TOKEN=seu_token_aqui
BOT_OWNER_ID=seu_id_de_usuario
```

## Contribuição

Contribuições são bem-vindas. Siga o padrão existente de:
1. Criar comandos em arquivos separados
2. Documentar no menu.py
3. Manter consistência com a estrutura atual

## Contato

Desenvolvedor: Braga  
GitHub: [braga2311](https://github.com/braga2311)  
Repositório: [Lithium-Bot](https://github.com/braga2311/Lithium-Bot)
