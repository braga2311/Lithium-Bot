import requests
from discord.ext import commands
from utils.validators import validar_cpf

class Consultas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cpf(self, ctx, cpf: str):
        if validar_cpf(cpf):
            await ctx.send(f"✅ CPF `{cpf}` é válido.")
        else:
            await ctx.send(f"❌ CPF `{cpf}` é inválido.")

    @commands.command()
    async def cep(self, ctx, cep: str):
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if r.status_code == 200 and "erro" not in r.json():
            data = r.json()
            await ctx.send(f"📍 {data['logradouro']}, {data['bairro']}, {data['localidade']} - {data['uf']}")
        else:
            await ctx.send("❌ CEP inválido.")

    @commands.command()
    async def cnpj(self, ctx, cnpj: str):
        cnpj = ''.join(filter(str.isdigit, cnpj))
        r = requests.get(f"https://publica.cnpj.ws/cnpj/{cnpj}")
        if r.status_code == 200:
            data = r.json()
            await ctx.send(f"🏢 {data['razao_social']} - {data['estabelecimento']['cidade']['nome']}/{data['estabelecimento']['estado']['sigla']}")
        else:
            await ctx.send("❌ CNPJ inválido.")

    @commands.command()
    async def ip(self, ctx, ip: str):
        r = requests.get(f"http://ip-api.com/json/{ip}")
        data = r.json()
        if data["status"] == "success":
            await ctx.send(f"🌐 {data['city']}, {data['regionName']} - {data['country']}")
        else:
            await ctx.send("❌ IP inválido.")

    @commands.command()
    async def ddd(self, ctx, ddd: str):
        r = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}")
        if r.status_code == 200:
            cidades = ", ".join(r.json()["cities"][:5])
            await ctx.send(f"📞 DDD {ddd}: {cidades}...")
        else:
            await ctx.send("❌ DDD inválido.")

    @commands.command()
    async def bin(self, ctx, bin: str):
        r = requests.get(f"https://lookup.binlist.net/{bin}")
        if r.status_code == 200:
            data = r.json()
            await ctx.send(f"💳 {data['scheme']} - {data['bank']['name']} ({data['country']['name']})")
        else:
            await ctx.send("❌ BIN inválido.")

    @commands.command()
    async def telefone(self, ctx, tel: str):
        if tel.startswith("+55"):
            await ctx.send("📱 Telefone brasileiro detectado.")
        else:
            await ctx.send("❌ Telefone não identificado.")

    @commands.command()
    async def nome_estado(self, ctx, uf: str):
        r = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf.upper()}")
        if r.status_code == 200:
            data = r.json()
            await ctx.send(f"{data['nome']} - {data['regiao']['nome']}")
        else:
            await ctx.send("❌ Sigla inválida.")

    @commands.command()
    async def moeda(self, ctx):
        r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
        if r.status_code == 200:
            data = r.json()
            usd = data["USDBRL"]["bid"]
            eur = data["EURBRL"]["bid"]
            btc = data["BTCBRL"]["bid"]
            await ctx.send(f"💰 USD: R${usd}, EUR: R${eur}, BTC: R${btc}")
        else:
            await ctx.send("❌ Erro na API")

    @commands.command()
    async def clima(self, ctx, cidade: str):
        await ctx.send(f"☀️ Clima em {cidade} não implementado nesta versão.")

async def setup(bot):
    await bot.add_cog(Consultas(bot))
