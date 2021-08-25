from io import BytesIO
from string import hexdigits

from PIL import Image
from bot.bot import Bot
from discord import File
from discord.ext.commands import Cog, Context, command


class Color(Cog):
    """A cog containing a parser function for parsing the colors and the command function."""

    IMAGE_SIZE = (128, 128)

    @staticmethod
    def parse_color(color_code: str) -> str:
        """Parse a color code string to its respective mode."""
        color_code = color_code.replace("0x", "#")
        color_code = (
            "#" + color_code
            if len(color_code) == 6 and all(i in hexdigits for i in color_code)
            else color_code
        )
        if "rgb" in color_code or "rgba" in color_code:
            return color_code
        color_code = color_code.replace(",", " ")

        if len(ls := color_code.split()) == 3:
            color_code = "rgb(" + ", ".join(ls) + ")"
        elif len(ls) == 4:
            color_code = "rgba(" + ", ".join(ls) + ")"

        return color_code

    @command(
        help="""color <color value>
            Get a visual picture for color given as input, valid formats are -

            rgb, rgba -
                color rgb(v1, v2, v3); color rgba(v1, v2, v3, v4)
                color v1, v2, v3; color v1, v2, v3, v4
            Hex -
                color #181818; color 0x181818
            """,
        brief="Get a image of the color given as input",
        name="color",
        aliases=("col",),
    )
    async def color_command(self, ctx: Context, *, color_code: str) -> None:
        """Sends an image which is the color of provided as the input."""
        parsed_color_code = self.parse_color(color_code)

        try:
            new_col = Image.new("RGB", self.IMAGE_SIZE, parsed_color_code)
        except ValueError:
            await ctx.send(f"Unknown color specifier `{color_code}`")
            return
        bufferio = BytesIO()
        new_col.save(bufferio, format="PNG")
        bufferio.seek(0)

        file = File(bufferio, filename=f"{parsed_color_code}.png")

        await ctx.send(file=file)


def setup(bot: Bot) -> None:
    """Load the Color cog."""
    bot.add_cog(Color(bot))
