import discord
from discord.ext import commands
import datetime

class Utilidades(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="avatar")
    async def avatar(self, ctx, membro: discord.Member = None):
        """Mostra o avatar de um usuário"""
        membro = membro or ctx.author
        embed = discord.Embed(title=f"🖼 Avatar de {membro.display_name}", color=0x7289DA)
        embed.set_image(url=membro.avatar.url)
        embed.set_footer(text=f"Solicitado por {ctx.author.display_name}")
        await ctx.send(embed=embed)

    @commands.command(name="userinfo")
    async def userinfo(self, ctx, membro: discord.Member = None):
        """Mostra informações sobre um usuário"""
        membro = membro or ctx.author
        embed = discord.Embed(
            title=f"ℹ Informações de {membro.display_name}",
            color=membro.color
        )
        embed.set_thumbnail(url=membro.avatar.url)
        embed.add_field(name="📛 Nome", value=membro.name, inline=True)
        embed.add_field(name="#️⃣ Tag", value=membro.discriminator, inline=True)
        embed.add_field(name="🆔 ID", value=membro.id, inline=True)
        embed.add_field(name="📅 Entrou em", value=membro.joined_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="🎂 Criado em", value=membro.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="🏷 Cargos", value=", ".join([role.name for role in membro.roles[1:]]), inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="serverinfo")
    async def serverinfo(self, ctx):
        """Mostra informações sobre o servidor"""
        guild = ctx.guild
        embed = discord.Embed(
            title=f"ℹ Informações do Servidor",
            color=0x7289DA
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(name="📛 Nome", value=guild.name, inline=True)
        embed.add_field(name="👑 Dono", value=guild.owner, inline=True)
        embed.add_field(name="🆔 ID", value=guild.id, inline=True)
        embed.add_field(name="📅 Criado em", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.add_field(name="👥 Membros", value=guild.member_count, inline=True)
        embed.add_field(name="💬 Canais", value=len(guild.channels), inline=True)
        embed.add_field(name="😎 Emojis", value=len(guild.emojis), inline=True)
        embed.add_field(name="🎭 Cargos", value=len(guild.roles), inline=True)
        await ctx.send(embed=embed)

    @commands.command(name="lembrete")
    async def lembrete(self, ctx, tempo: int, *, mensagem: str):
        """Define um lembrete (em minutos)"""
        await ctx.send(f"⏰ Lembrete definido para {tempo} minutos!")
        await asyncio.sleep(tempo * 60)
        await ctx.send(f"⏰ Lembrete para {ctx.author.mention}: {mensagem}")

    @commands.command(name="convite")
    async def convite(self, ctx):
        """Gera um convite para o servidor"""
        invite = await ctx.channel.create_invite(max_age=300)
        await ctx.send(f"🔗 Convite gerado: {invite.url}")

async def setup(bot):
    await bot.add_cog(Utilidades(bot))