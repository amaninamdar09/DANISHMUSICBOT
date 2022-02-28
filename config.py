from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN","5157142486:AAHuWCq24yXRIq6MBPaT-B4nYyoEU_ybD84")
API_ID = int(getenv("API_ID", "11977266"))
API_HASH = getenv("API_HASH","a128248e7223b86e6d1c417e8f355704")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "300"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://kvaiyukki09:kvaiyukki09@cluster0.qvhkz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1968830241").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "1968830241").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001510782734"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME","𝐃𝐀𝐍𝐈𝐒𝐇 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓")

if str(getenv("STRING_SESSION1")).strip() == "":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"," AQAJ8gU594D7BR3jasckDWMKQsdDLWNls3rS_Bu1I4HmYQYCfMFIuEnYE2GNA9rFS625Mj_VLcSSIUpjliC_8_ehwSGHCL5yAV4JMHVFctw0muv-SxNujY8ugO-NmKFwXUDDpF2fxIYGlWOauV3Yg801KTxmN4EKz8UVeoXkZBcZLHuFfIMHnBBRerLbHpksNyfQej0p7cd_sECChe-UhPtgyKq9TRkLbmG4Oxx-qWDWH-QkUPZES5Q08VBG_4SkYp7hsIcuLOzQR_1SCi6cyb4exjH5wkIHqIXqfgODkHLNudJljIl153jy2ZRHWHL1nMCoru4wesFAkI8bX1XsuG_8AAAAATf_Kb0A"))

UPSTREAM_REPO = "https://github.com/amaninamdar09/DANISHMUSICBOT"
UPSTREAM_BRANCH = "main"

SUPPORT_CHANNEL = "https://t.me/TechZBots"
SUPPORT_GROUP = "https://t.me/TechZBots_Support"

THUMBNAIL = getenv("THUMB_LINK") 

botusername = str(getenv("BOT_USERNAME"))



if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION","AQAJ8gU594D7BR3jasckDWMKQsdDLWNls3rS_Bu1I4HmYQYCfMFIuEnYE2GNA9rFS625Mj_VLcSSIUpjliC_8_ehwSGHCL5yAV4JMHVFctw0muv-SxNujY8ugO-NmKFwXUDDpF2fxIYGlWOauV3Yg801KTxmN4EKz8UVeoXkZBcZLHuFfIMHnBBRerLbHpksNyfQej0p7cd_sECChe-UhPtgyKq9TRkLbmG4Oxx-qWDWH-QkUPZES5Q08VBG_4SkYp7hsIcuLOzQR_1SCi6cyb4exjH5wkIHqIXqfgODkHLNudJljIl153jy2ZRHWHL1nMCoru4wesFAkI8bX1XsuG_8AAAAATf_Kb0A "))

if str(getenv("LIMIT")).strip().upper() == "FALSE":
    PL_LIMIT = "FALSE"
else:
    PL_LIMIT = "TRUE"

if str(getenv("PM_PERMIT")).strip().upper() == "FALSE":
    PM_PERMIT = "FALSE"
else:
    PM_PERMIT = "TRUE"
