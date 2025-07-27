import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
 
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
 
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))
 
OWNER_ID = int(getenv("OWNER_ID", None))

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz')
API_KEY = getenv("API_KEY", None)

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/high-tier-bots/ketty-pai-music/",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
 
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
 
PRIVACY_LINK = getenv("PRIVACY_LINK", "privacy link here")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

 
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
PING_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
PLAYLIST_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
STATS_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
STREAM_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
SOUNDCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/aYZ.jpg/IMG20250608719.jpg"


def time_to_seconds(time):
    stringtime = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringtime.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )