import zlib
from functools import partial
from typing import Any, Optional

import aiohttp
from discord.ext import commands
from loguru import logger

to_bytes = partial(bytes, encoding='utf-8')


def _to_tio_string(couple: tuple) -> Any:
    name, obj = couple[0], couple[1]
    if not obj:
        return b''
    elif type(obj) == list:
        content = ['V' + name, str(len(obj))] + obj
        return to_bytes('\x00'.join(content) + '\x00')
    else:
        return to_bytes(f"F{name}\x00{len(to_bytes(obj))}\x00{obj}\x00")


class Tio:
    """Helper class for eval command."""

    def __init__(self, language: str, code: str, inputs: str = '',
                 compiler_flags: list = [], command_line_options: list = [], args: list = []):
        self.backend = "https://tio.run/cgi-bin/run/api/"
        self.json = "https://tio.run/languages.json"

        strings = {
            'lang': [language],
            '.code.tio': code,
            '.input.tio': inputs,
            'TIO_CFLAGS': compiler_flags,
            'TIO_OPTIONS': command_line_options,
            'args': args
        }

        bytes_ = b''.join(map(_to_tio_string, zip(strings.keys(), strings.values()))) + b'R'

        # This returns a DEFLATE-compressed byte-string, which is what the API requires
        self.request = zlib.compress(bytes_, 9)[2:-4]

    async def send(self) -> Any:
        """Send Request to Tio Run API."""
        async with aiohttp.ClientSession() as client_session:
            async with client_session.post(self.backend, data=self.request) as res:
                if res.status != 200:
                    raise aiohttp.HttpProcessingError(res.status)

                data = await res.read()
                data = data.decode('utf-8')
                return data.replace(data[:16], '')  # remove token


def get_raw(link: str) -> str:
    """Returns the url for raw version on a hastebin-like."""
    link = link.strip('<>/')  # Allow for no-embed links

    authorized = (
        'https://hastebin.com',
        'https://gist.github.com',
        'https://gist.githubusercontent.com'
    )

    if not any(link.startswith(url) for url in authorized):
        raise commands.BadArgument(message=f"I only accept links from {', '.join(authorized)}. "
                                           f"(Starting with 'http').")

    domain = link.split('/')[2]

    if domain == 'hastebin.com':
        if '/raw/' in link:
            return link
        token = link.split('/')[-1]
        if '.' in token:
            token = token[:token.rfind('.')]  # removes extension
        return f'https://hastebin.com/raw/{token}'
    else:
        # Github uses redirection so raw -> user content and no raw -> normal
        # We still need to ensure we get a raw version after this potential redirection
        if '/raw' in link:
            return link
        return link + '/raw'


async def paste(text: str) -> Optional[str]:
    """Upload the eval output to a paste service and return a URL to it if successful."""
    logger.info("Uploading full output to paste service...")
    async with aiohttp.ClientSession() as session:
        post = await session.post('https://hastebin.com/documents', data=text)
        if post.status == 200:
            response = await post.text()
            return f'https://hastebin.com/{response[8:-2]}'

        # Rollback bin
        post = await session.post("https://bin.drlazor.be", data={'val': text})
        if post.status == 200:
            return post.url
