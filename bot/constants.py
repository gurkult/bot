import os
import pathlib
from typing import NamedTuple

import yaml

ENVIRONMENT = os.getenv("ENVIRONMENT")
if ENVIRONMENT is None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path=f"{os.getcwd()}/.env")

# env vars
PREFIX = os.getenv("PREFIX", "!")

TOKEN = os.getenv("TOKEN")

BOT_REPO_URL = "https://github.com/gurkult/gurkbot"

DATABASE_URL = os.getenv("DATABASE_URL")

# paths
EXTENSIONS = pathlib.Path("bot/exts/")
LOG_FILE = pathlib.Path("log/gurkbot.log")


if TEST_GUILDS := os.getenv("TEST_GUILDS"):
    TEST_GUILDS = [int(x) for x in TEST_GUILDS.split(",")]


class Emojis(NamedTuple):
    issue_emoji = "<:IssueOpen:794834041450266624>"
    issue_closed_emoji = "<:IssueClosed:794834041240289321>"
    pull_request_emoji = "<:PROpen:794834041416187935>"
    pull_request_closed_emoji = "<:PRClosed:794834041073172501>"
    merge_emoji = "<:PRMerged:794834041173704744>"

    cucumber_emoji = "\U0001f952"

    invalid_emoji = "\u274c"
    trashcan = str(os.getenv("EMOJI_TRASHCAN", "<:trash:798179380626587658>"))

    confirmation_emoji = "<:confirmation:824252277262123029>"
    warning_emoji = "\u26a0"

    CHECK_MARK_EMOJI = "\U00002705"
    CROSS_MARK_EMOJI = "\U0000274C"
    MAG_RIGHT_EMOJI = "\U0001f50e"


class Colours:
    green = 0x1F8B4C
    yellow = 0xF1C502
    soft_red = 0xCD6D6D


class GurkanNameEndings:
    name_endings = ["gurk", "gurkan", "urkan"]


class Channels(NamedTuple):
    off_topic = int(os.getenv("CHANNEL_OFF_TOPIC", 789198156218892358))
    gurkcraft = int(os.getenv("CHANNEL_GURKCRAFT", 878159594189381662))
    gurkcraft_relay = int(os.getenv("CHANNEL_GURKCRAFT_RELAY", 932334985053102101))

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
    devops = int(os.getenv("ROLE_DEVOPS", 918880926606430308))

    announcements = int(os.getenv("ANNOUNCEMENTS_ID", 789978290844598272))
    polls = int(os.getenv("POLLS_ID", 790043110360350740))
    events = int(os.getenv("EVENTS_ID", 890656665328820224))


class Tokens(NamedTuple):
    wolfram_token = os.getenv("WOLFRAM_TOKEN")


# Bot replies
with pathlib.Path("bot/resources/bot_replies.yml").open(encoding="utf8") as file:
    bot_replies = yaml.safe_load(file)
    ERROR_REPLIES = bot_replies["ERROR_REPLIES"]
    POSITIVE_REPLIES = bot_replies["POSITIVE_REPLIES"]
    NEGATIVE_REPLIES = bot_replies["NEGATIVE_REPLIES"]


# Minecraft Server
class Minecraft(NamedTuple):
    server_address = "mc.gurkult.com"
