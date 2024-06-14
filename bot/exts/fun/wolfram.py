import random
from io import BytesIO
from typing import Literal, Union
from urllib import parse

import disnake
from disnake import Embed
from disnake.ext import commands

from bot.constants import ERROR_REPLIES, Colours, Tokens


class WolframCommands(commands.Cog):
    """
    Wolfram Category cog, containing commands related to the WolframAlpha API.

    Commands
        └ image         Fetch the response to a query in the form of an image.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.image_url = "https://api.wolframalpha.com/v1/simple"
        self.params = {
            "appid": Tokens.wolfram_token,
            "background": "2F3136",
            "foreground": "white",
            "layout": "labelbar",
            "fontsize": "23",
            "width": "700",
            "location": "the moon",
            "latlong": "0.0,0.0",
            "ip": "1.1.1.1",
        }

    async def web_request(self, url: str, params: dict) -> Union[bytes, str]:
        """Web request handler for wolfram group of commands."""
        async with self.bot.http_session.get(url=url, params=params) as resp:
            if resp.status == 200:
                return await resp.read()
            elif resp.status == 501:
                return "Sorry, the API could not understand your input"
            elif resp.status == 400:
                return "Sorry, the API did not find any input to interpret"

    @commands.slash_command()
    async def wolfram(self, inter: disnake.ApplicationCommandInteraction) -> None:
        """Commands for wolfram."""

    @wolfram.sub_command()
    async def image(
        self,
        inter: disnake.ApplicationCommandInteraction,
        query: str,
        theme: Literal["light", "dark"] = "dark",
    ) -> None:
        """
        Send wolfram image corresponding to the given query.

        Parameters
        ----------
        query: The user query.
        theme: The theme of the image generated. dark by default.
        """
        await inter.response.defer()

        params = self.params

        if theme == "light":
            params |= {"background": "white", "foreground": "2F3136"}

        response = await self.web_request(
            url=self.image_url, params=params | {"i": query}
        )

        if isinstance(response, str):
            embed = Embed(title=random.choice(ERROR_REPLIES), description=response)
        else:
            original_url = parse.quote_plus(query)
            file = disnake.File(BytesIO(response), filename="image.png")

            embed = Embed(title="Wolfram Alpha", colour=Colours.green)
            embed.set_image(file=file)
            embed.add_field(
                name="Cannot see image?",
                value=f"[Click here](https://www.wolframalpha.com/input/?i={original_url})",
            )

        await inter.edit_original_message(embed=embed)


def setup(bot: commands.Bot) -> None:
    """Load the Wolfram cog."""
    bot.add_cog(WolframCommands(bot))
