from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5157142486:AAG740rXvfWibCUPCkMK8hE6yRPDUMu2FEs")
API_ID = int(getenv("API_ID", "11977266"))
API_HASH = getenv("API_HASH", "a128248e7223b86e6d1c417e8f355704")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kvaiyukki09:kvaiyukki09@cluster0.qvhkz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5032100535").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1968830241").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001510782734"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐃𝐀𝐍𝐈𝐒𝐇 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 ")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = "https://github.com/amaninamdar09/DANISHMUSICBOT"
UPSTREAM_BRANCH = "main"

if str(getenv("SUPPORT_CHANNEL")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "https://t.me/DANISH_BABA"))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "https://t.me/WEFRIENDSCIRCLE"))

THUMBNAIL = getenv("THUMB_LINK") 

botusername = str(getenv("BOT_USERNAME", "DANISHMUSIC_BOT"))

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1", "AQAucqbZ84L7edhayHCKib9J1QARC67ovCb9ePaPGGOzUnlpiZ1y94fExAtkKupkc_DCThAp-jCWQ-f5z8_MfkCGjup8Hu83awRUT9p9FfSuZoBuqsSQoQOJPKjEi8sc-al2rJhlnf8QBnWoM8EgwrW3YkcyCO1JbiqXI4jhKKdySOdy96EDZ6xBDp5ddxXzpsr9BuIX73i5G4Pu6jk-Pnx2wpiowFAT7urPTQQHgYNXG5-Vn0W7RqniX3V_V58KNc7CreIRRlAdjKULQkXyxjs7MBDDeZlBupcmQw7M386fqVK4ZNaT6BAVHbdrcyX4KPCCuFyzDfRS7yLAKrhJpfQFAAAAATf_Kb0A"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))

if str(getenv("LIMIT")).strip().upper() == "FALSE":
    PL_LIMIT = "FALSE"
else:
    PL_LIMIT = "TRUE"

if str(getenv("PM_PERMIT")).strip().upper() == "FALSE":
    PM_PERMIT = "FALSE"
else:
    PM_PERMIT = "TRUE"
