import discord
from bot.constants import Colours, Minecraft
from discord.ext import commands
from discord.ext.commands import Bot
from mcstatus import MinecraftServer


class Gurkcraft(commands.Cog):
    """Gurkcraft Cog."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.server = MinecraftServer.lookup(Minecraft.server_address)

    @commands.command()
    async def mcstatus(self, ctx: commands.Context) -> None:
        """Collects data from minecraft server."""
        status = self.server.status()
        players = [user["name"] for user in status.raw["players"]["sample"]]
        embed = discord.Embed(
            title="Gurkcraft", color=Colours.green
        )
        embed.add_field(name="Server", value="mc.gurkult.com")
        embed.add_field(name="Server Latency", value=f"{status.latency}ms")
        embed.add_field(name="Gurkans Online", value=status.players.online)
        embed.add_field(name="Gurkans Connected", value=", ".join(players))
        await ctx.send(embed=embed)


def setup(bot: Bot) -> None:
    """Loading the Gurkcraft cog."""
    bot.add_cog(Gurkcraft(bot))
