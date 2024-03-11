import re, logging
from os import environ
from Script import script


def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f"Error - {type} is invalid, exiting now")
        exit()


def is_valid_ip(ip):
    ip_pattern = r"\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    return re.match(ip_pattern, ip) is not None


# Bot information
API_ID = environ.get("API_ID", "20725471")
if len(API_ID) == 0:
    print("Error - API_ID is missing, exiting now")
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get("API_HASH", "7d32846e37e769270e94b6085b61bebf")
if len(API_HASH) == 0:
    print("Error - API_HASH is missing, exiting now")
    exit()
BOT_TOKEN = environ.get("BOT_TOKEN", "6719328690:AAH8__XIctQL6MadGXX2EzjcJIiqBDkaJNM")
if len(BOT_TOKEN) == 0:
    print("Error - BOT_TOKEN is missing, exiting now")
    exit()
PORT = int(environ.get("PORT", "80"))

# Bot pics
PICS = (
    environ.get(
        "PICS",
        "https://graph.org/file/908d420964ba210446d95.jpg https://graph.org/file/6cf41461bed9069511bca.jpg https://graph.org/file/d5a09d3192152dc4e3c85.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg",
    )
).split()

# Bot Admins
ADMINS = environ.get("ADMINS", "6093349648 2015261342")
if len(ADMINS) == 0:
    print("Error - ADMINS is missing, exiting now")
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [
    (
        int(index_channels)
        if index_channels.startswith("-1001931435328 -1001952883830 -1002032241046")
        else index_channels
    )
    for index_channels in environ.get("INDEX_CHANNELS", "").split()
]
if len(INDEX_CHANNELS) == 0:
    print("Info - INDEX_CHANNELS is empty")
AUTH_CHANNEL = [
    int(auth_channels)
    for auth_channels in environ.get("AUTH_CHANNEL", "-1002103005544").split()
]
if len(AUTH_CHANNEL) == 0:
    print("Info - AUTH_CHANNEL is empty")
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002083165096")
if len(LOG_CHANNEL) == 0:
    print("Error - LOG_CHANNEL is missing, exiting now")
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
IS_FSUB = is_enabled("IS_FSUB", True)

# support group
SUPPORT_GROUP = environ.get("SUPPORT_GROUP", "-1002103005544")
if len(SUPPORT_GROUP) == 0:
    print("Error - SUPPORT_GROUP is missing, exiting now")
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# for chatGPT
OPENAI_API = environ.get("OPENAI_API", "t.me/moviehiap")
if len(OPENAI_API) == 0:
    print("Info - OPENAI_API is empty")

# MongoDB information
DATABASE_URL = environ.get(
    "DATABASE_URL",
    "mongodb+srv://shivamcharan7773:shivacharan7@cluster0.se91yp0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
if len(DATABASE_URL) == 0:
    print("Error - DATABASE_URL is missing, exiting now")
    exit()
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
COLLECTION_NAME = environ.get("COLLECTION_NAME", "Files")

# Links
SUPPORT_LINK = environ.get("SUPPORT_LINK", "https://t.me/movies_group7")
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/shivacharan7773")
UPDATES_LINK = environ.get("UPDATES_LINK", "https://t.me/moviehiap")
FILMS_LINK = environ.get("FILMS_LINK", "https://t.me/movies_group7")
TUTORIAL = environ.get("TUTORIAL", "https://t.me/moviehiap/42")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/moviehiap/42")

# Bot settings
DELETE_TIME = int(environ.get("DELETE_TIME", 3600))  # Add time in seconds
CACHE_TIME = int(environ.get("CACHE_TIME", 300))
MAX_BTN = int(environ.get("MAX_BTN", 10))
LANGUAGES = [
    language.lower()
    for language in environ.get(
        "LANGUAGES", "english hindi telugu tamil kannada malayalam"
    ).split()
]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "zipshort.net")
SHORTLINK_API = environ.get("SHORTLINK_API", "f120cb64411e025a60b7b71d4636c9321c7713f9")
VERIFY_EXPIRE = int(environ.get("VERIFY_EXPIRE", 86400))  # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [
    extensions.lower()
    for extensions in environ.get("INDEX_EXTENSIONS", "mp4 mkv").split()
]

# boolean settings
IS_VERIFY = is_enabled("IS_VERIFY", False)
AUTO_DELETE = is_enabled("AUTO_DELETE", True)
WELCOME = is_enabled("WELCOME", False)
PROTECT_CONTENT = is_enabled("PROTECT_CONTENT", False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled("AUTO_FILTER", True)
IMDB = is_enabled("IMDB", True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled("SHORTLINK", True)

PAYMENT_QR = environ.get(
    "PAYMENT_QR", "https://graph.org/file/aaa41aa91bb4c5fd5f6ea.jpg"
)

# for stream
IS_STREAM = is_enabled("IS_STREAM", True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001819881264")
if len(BIN_CHANNEL) == 0:
    print("Error - BIN_CHANNEL is missing, exiting now")
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://aimoviebot-0a8ee4d86edb.herokuapp.com/")
if len(URL) == 0:
    print("Error - URL is missing, exiting now")
    exit()
else:
    if URL.startswith(("https://", "http://")):
        if not URL.endswith("/https://drragon-6b68519b6c55.herokuapp.com"):
            URL += "/"
    elif is_valid_ip(URL):
        URL = f"http://{URL}/https://drragon-6b68519b6c55.herokuapp.com"
    else:
        print("Error - URL is not valid, exiting now")
        exit()
