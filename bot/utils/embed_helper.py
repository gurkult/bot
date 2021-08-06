from random import choice
from typing import Dict, Optional, Tuple, Union

from discord import Embed

from ..constants import Colours, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES


class EmbedHelper:
    """doctstring."""

    @staticmethod
    def embed_helper(
        *,
        title: str,
        description: str,
        colour: int,
        fields: Union[Tuple[Dict[str, str], ...], Tuple[()]],
        url: Optional[str] = None,
    ) -> Embed:
        """Method that creates an embed."""
        embed = Embed(title=title, description=description, colour=colour, url=url)
        for field in fields:
            embed.add_field(
                name=field.get("name"),
                value=field.get("value"),
                inline=field.get("inline", False),
            )
        return embed

    @classmethod
    def information(
        cls,
        *,
        title: Optional[str] = None,
        description: str,
        fields: Optional[Tuple[Dict[str, str], ...]] = None,
        url: Optional[str] = None,
    ) -> Embed:
        """Embed used in a positive context."""
        title_ = title or choice(POSITIVE_REPLIES)
        fields = fields or tuple()

        return cls.embed_helper(
            title=title_,
            description=description,
            fields=fields,
            url=url,
            colour=Colours.green,
        )

    @classmethod
    def error(
        cls,
        *,
        title: Optional[str] = None,
        description: str,
        fields: Optional[Tuple[Dict[str, str], ...]] = None,
        url: Optional[str] = None,
    ) -> Embed:
        """Embed used for displaying errors."""
        title_ = title or choice(ERROR_REPLIES)
        fields = fields or tuple()

        return cls.embed_helper(
            title=title_,
            description=description,
            fields=fields,
            url=url,
            colour=Colours.soft_red,
        )

    @classmethod
    def warning(
        cls,
        *,
        title: Optional[str] = None,
        description: str,
        fields: Optional[Tuple[Dict[str, str], ...]] = None,
        url: Optional[str] = None,
    ) -> Embed:
        """Embed used to warn user."""
        title_ = title or choice(NEGATIVE_REPLIES)
        fields = fields or tuple()

        return cls.embed_helper(
            title=title_,
            description=description,
            fields=fields,
            url=url,
            colour=Colours.yellow,
        )
