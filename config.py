import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "26586185")) #optional
API_HASH = getenv("API_HASH", "d5be9bfd3997341780f0b141fb339dad") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1064619217").split()))
OWNER_ID = int(getenv("OWNER_ID", "1064619217"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://nobu:nobu@cluster0.gwxdimu.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5454631162:AAF7GxHRY7BWwUrhW2VyjgZn4fSOp9XPF98")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "-735029137")
LOG_GROUP = getenv("LOG_GROUP", "-735029137")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAgSdTIS_e4BhuE_sO_1Eo8NpRhc6Ww-daHDLRrOmYbGhU8vdfol5_iEPB7XDKMiARga6l9C_tUGUTe9ZX8S-RmQdl19w-X7iKldQ7L4MlUSdYiie0iBsOfw3yW44ptOcMS5IKyQnuQJejtZUC5sz-lsO4X_zYqUkQiYqBwmacniovHNLXjxgtEXUcH0x4tGqfL0jqAhm8A6s3FhrV2fU496tZhl6v_D3t0nmXA2WOnXdGKMRhTynS8NX8HQWytE1tWBAB1HPeOtHCC2OfZMHTG49P-ImlHBR5SwiuQw_ZIgyzGkHFHTW6EHfdadBWgi9Xi1eZ89DSSkSC6cO4ZfT9zQAAAAFjoTNqAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
