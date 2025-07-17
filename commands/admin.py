import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! Latência: {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} foi expulso.")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} foi banido.")

    @commands.command()
    async def unban(self, ctx, *, user_info):
        name, discrim = user_info.split("#")
        for ban in await ctx.guild.bans():
            if ban.user.name == name and ban.user.discriminator == discrim:
                await ctx.guild.unban(ban.user)
                await ctx.send(f"{user_info} desbanido.")
                return
        await ctx.send("Usuário não encontrado.")

    @commands.command()
    async def mute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not role:
            role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False)
        await member.add_roles(role)
        await ctx.send(f"{member.mention} foi silenciado.")

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role:
            await member.remove_roles(role)
            await ctx.send(f"{member.mention} não está mais silenciado.")

    @commands.command()
    async def clear(self, ctx, amount: int = 5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount} mensagens removidas.", delete_after=3)

    @commands.command()
    async def slowmode(self, ctx, delay: int):
        await ctx.channel.edit(slowmode_delay=delay)
        await ctx.send(f"Slowmode definido para {delay} segundos.")

    @commands.command()
    async def lock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("Canal bloqueado.")

    @commands.command()
    async def unlock(self, ctx):
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.send("Canal desbloqueado.")

async def setup(bot):
    await bot.add_cog(Admin(bot))
