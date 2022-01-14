import random

from disnake import Embed, Forbidden
from disnake.ext import commands

from bot.bot import Bot
from bot.constants import NEGATIVE_REPLIES, POSITIVE_REPLIES, Colours, GurkanNameEndings
from bot.utils.is_gurkan import gurkan_check


class Gurkify(commands.Cog):
    """Cog for the gurkify command."""

    @commands.command(name="gurkify")
    async def gurkify(self, ctx: commands.Context) -> None:
        """Gurkify user's display name."""
        display_name = ctx.author.display_name

        if gurkan_check(display_name):
            embed = Embed(
                title="I love the ambition...",
                description=(
                    "... but you're already a gurkan! Instead of becoming a 'double-gurkan', "
                    "why not focus on living a truly gurkan life instead?"
                ),
                color=Colours.yellow,
            )
        elif len(display_name) > 26:
            embed = Embed(
                title=random.choice(NEGATIVE_REPLIES),
                description=(
                    "Your nick name is too long to be gurkified. "
                    "Please change it to be under 26 characters."
                ),
                color=Colours.soft_red,
            )

        else:  # No obvious issues with gurkifying were found
            try:
                display_name += random.choice(GurkanNameEndings.name_endings)
                await ctx.author.edit(nick=display_name)
            except Forbidden:
                embed = Embed(
                    title="You're too powerful!",
                    description="I can't change the names of users with top roles higher than mine.",
                    color=Colours.soft_red,
                )
            else:
                embed = Embed(
                    title=random.choice(POSITIVE_REPLIES),
                    description="You nick name has been gurkified.",
                    color=Colours.green,
                )

        await ctx.send(content=ctx.author.mention, embed=embed)


def setup(bot: Bot) -> None:
    """Loads the gurkify cog."""
    bot.add_cog(Gurkify())
