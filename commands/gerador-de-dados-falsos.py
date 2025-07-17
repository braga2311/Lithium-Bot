import random
import discord
from discord.ext import commands

def gerar_cpf():
    def calc_digito(parcial):
        peso = list(range(len(parcial)+1, 1, -1))
        soma = sum(int(d) * p for d, p in zip(parcial, peso))
        r = soma % 11
        return '0' if r < 2 else str(11 - r)

    base = ''.join(str(random.randint(0, 9)) for _ in range(9))
    d1 = calc_digito(base)
    d2 = calc_digito(base + d1)
    cpf = base + d1 + d2
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

def gerar_cnh():
    numeros = [random.randint(0, 9) for _ in range(9)]
    soma = sum((9 - i) * n for i, n in enumerate(numeros))
    d1 = (soma % 11)
    d1 = 0 if d1 >= 10 else d1

    soma2 = sum((1 + i) * n for i, n in enumerate(numeros))
    d2 = (soma2 % 11)
    d2 = 0 if d2 >= 10 else d2

    cnh = ''.join(map(str, numeros)) + f'{d1}{d2}'
    return cnh

def gerar_cep():
    return f'{random.randint(10000, 99999)}-{random.randint(100, 999)}'

def gerar_titulo():
    def calcular_digito(parcial, peso_inicial):
        soma = sum(int(num) * peso for num, peso in zip(parcial, range(peso_inicial, 1, -1)))
        resto = soma % 11
        return '0' if resto in (0, 1) else str(11 - resto)

    numero = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    uf = f"{random.randint(1, 28):02}"
    parcial = numero + uf
    d1 = calcular_digito(parcial, 10)
    d2 = calcular_digito(parcial + d1, 11)
    return f'{parcial}{d1}{d2}'

@commands.command(name='gerarcpf')
async def gerarcpf(ctx):
    cpf = gerar_cpf()
    embed = discord.Embed(title="📄 CPF Gerado", description=f"`{cpf}`", color=0x00ff88)
    embed.set_footer(text="Documento gerado automaticamente — apenas para testes.")
    await ctx.send(embed=embed)

@commands.command(name='gerarcnh')
async def gerarcnh(ctx):
    cnh = gerar_cnh()
    embed = discord.Embed(title="🚗 CNH Gerada", description=f"`{cnh}`", color=0x0088ff)
    embed.set_footer(text="Documento gerado automaticamente — apenas para testes.")
    await ctx.send(embed=embed)

@commands.command(name='gerarcep')
async def gerarcep(ctx):
    cep = gerar_cep()
    embed = discord.Embed(title="📬 CEP Gerado", description=f"`{cep}`", color=0xff8800)
    embed.set_footer(text="CEP gerado automaticamente — pode não corresponder a uma região real.")
    await ctx.send(embed=embed)

@commands.command(name='gerartitulo')
async def gerartitulo(ctx):
    titulo = gerar_titulo()
    embed = discord.Embed(title="🗳️ Título de Eleitor Gerado", description=f"`{titulo}`", color=0xaa00ff)
    embed.set_footer(text="Documento gerado automaticamente — apenas para testes.")
    await ctx.send(embed=embed)

@commands.command(name='gerartudo')
async def gerartudo(ctx):
    cpf = gerar_cpf()
    cnh = gerar_cnh()
    cep = gerar_cep()
    titulo = gerar_titulo()

    embed = discord.Embed(title="📄 Documentos Gerados", color=0xffffff)
    embed.add_field(name="🧾 CPF", value=f"`{cpf}`", inline=False)
    embed.add_field(name="🚗 CNH", value=f"`{cnh}`", inline=False)
    embed.add_field(name="📬 CEP", value=f"`{cep}`", inline=False)
    embed.add_field(name="🗳️ Título de Eleitor", value=f"`{titulo}`", inline=False)
    embed.set_footer(text="Todos os dados são fictícios e para uso em testes ou protótipos.")
    await ctx.send(embed=embed)
