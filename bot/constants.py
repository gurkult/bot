import os
import pathlib
from typing import NamedTuple

import yaml

# env vars
PREFIX = os.getenv("PREFIX") or "!"
TOKEN = os.getenv("TOKEN")
BOT_REPO_URL = "https://github.com/gurkult/gurkbot"
DATABASE_URL = os.getenv("DATABASE_URL")

# paths
EXTENSIONS = pathlib.Path("bot/exts/")
LOG_FILE = pathlib.Path("log/gurkbot.log")


class Emojis(NamedTuple):
    issue_emoji = "<:IssueOpen:794834041450266624>"
    issue_closed_emoji = "<:IssueClosed:794834041240289321>"
    pull_request_emoji = "<:PROpen:794834041416187935>"
    pull_request_closed_emoji = "<:PRClosed:794834041073172501>"
    merge_emoji = "<:PRMerged:794834041173704744>"

    cucumber_emoji = "\U0001f952"

    invalid_emoji = "\u274c"
    trashcan = str(os.getenv("EMOJI_TRASHCAN", "<:trash:798179380626587658>"))

    CHECK_MARK_EMOJI = "\U00002705"
    CROSS_MARK_EMOJI = "\U0000274C"
    MAG_RIGHT_EMOJI = "\U0001f50e"

    # Number unicode emojis for TicTacToe
    number_emojis = {
        1: "\u0031\ufe0f\u20e3",
        2: "\u0032\ufe0f\u20e3",
        3: "\u0033\ufe0f\u20e3",
        4: "\u0034\ufe0f\u20e3",
        5: "\u0035\ufe0f\u20e3",
        6: "\u0036\ufe0f\u20e3",
        7: "\u0037\ufe0f\u20e3",
        8: "\u0038\ufe0f\u20e3",
        9: "\u0039\ufe0f\u20e3",
    }
    confirmation = "\u2705"
    decline = "\u274c"
    cucumber = "\U0001f952"
    watermelon = "\U0001f349"


class Colours:
    green = 0x1F8B4C
    yellow = 0xF1C502
    soft_red = 0xCD6D6D


class Channels(NamedTuple):
    off_topic = int(os.getenv("CHANNEL_OFF_TOPIC", 789198156218892358))

    devalerts = int(os.getenv("CHANNEL_DEVALERTS", 796695123177766982))
    devlog = int(os.getenv("CHANNEL_DEVLOG", 789431367167377448))

    dev_gurkbot = int(os.getenv("CHANNEL_DEV_GURKBOT", 789295038315495455))
    dev_reagurk = int(os.getenv("CHANNEL_DEV_REAGURK", 789241204696416287))
    dev_gurklang = int(os.getenv("CHANNEL_DEV_GURKLANG", 789249499800535071))
    dev_branding = int(os.getenv("CHANNEL_DEV_BRANDING", 789193817051234306))

    log = int(os.getenv("CHANNEL_LOGS", 831432092226158652))
    dm_log = int(os.getenv("CHANNEL_LOGS", 833345326675918900))


class Roles(NamedTuple):
    gurkans = int(os.getenv("ROLE_GURKANS", 789195552121290823))
    steering_council = int(os.getenv("ROLE_STEERING_COUNCIL", 789213682332598302))
    moderators = int(os.getenv("ROLE_MODERATORS", 818107766585163808))
    gurkult_lords = int(os.getenv("ROLE_GURKULT_LORDS", 789197216869777440))


# Bot replies
with pathlib.Path("bot/resources/bot_replies.yml").open(encoding="utf8") as file:
    bot_replies = yaml.safe_load(file)
    ERROR_REPLIES = bot_replies["ERROR_REPLIES"]
    POSITIVE_REPLIES = bot_replies["POSITIVE_REPLIES"]
    NEGATIVE_REPLIES = bot_replies["NEGATIVE_REPLIES"]
