from userbot import topfunc
import os
import re
import time
import math
import heroku3
import requests
import spamwatch as spam_watch
from ..helpers import *
from .. import StartTime
from userbot import catdef
from userbot.uniborgConfig import Config
from userbot.utils import admin_cmd
from var import Var 

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY
deEmojify = catdef.deEmojify
trumptweet = catdef.trumptweet 
changemymind = catdef.changemymind
kannagen = catdef.kannagen
moditweet = catdef.moditweet
tweets = catdef.tweets
waifutxt = catdef.waifutxt
catmusic = catdef.catmusic 
catmusicvideo = catdef.catmusicvideo
admin_groups = catdef.admin_groups

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)

thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"

# thumb image
with open(thumb_image_path, "wb") as f:
    f.write(requests.get(Config.THUMB_IMAGE).content)


def check(cat):
    if "/start" in cat:
        return True
    hi = re.search(re.escape(f"\\b{cat}\\b"), "a|b|c|d")
    if hi:
        return True
    return False


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION
    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None

async def catalive():
    _, check_sgnirts = check_data_base_heal_th()
    if Config.SUDO_USERS:
        sudo = "Enabled"
    else:
        sudo = "Disabled"
    uptime = await get_readable_time((time.time() - StartTime))
    try:
        useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/80.0.3987.149 Mobile Safari/537.36'
                     )
        user_id = Heroku.account().id
        headers = {
            'User-Agent': useragent,
            'Authorization': f'Bearer {Config.HEROKU_API_KEY}',
            'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
        }
        path = "/accounts/" + user_id + "/actions/get-quota"
        r = requests.get(heroku_api + path, headers=headers)
        result = r.json()
        quota = result['account_quota']
        quota_used = result['quota_used']

        # Used
        remaining_quota = quota - quota_used
        math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        # Current
        App = result['apps']
        try:
            App[0]['quota_used']
        except IndexError:
            AppQuotaUsed = 0
        else:
            AppQuotaUsed = App[0]['quota_used'] / 60
            math.floor(App[0]['quota_used'] * 100 / quota)
        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)
        dyno = f"{AppHours}h {AppMinutes}m/{hours}h {minutes}m"
    except Exception as e:
        dyno = e
    conclusion = f"Catuserbot Stats\
                 \n\nDatabase : {check_sgnirts}\
                  \nSudo : {sudo}\
                  \nUptime : {uptime}\
                  \nDyno : {dyno}\
                  "
    return conclusion
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "3.0"

if issudousing:
    amiusingsudo = "Active ✅"
else:
    amiusingsudo = "Inactive ❌"

if islogokay:
    logchat = "Connected ✅"
else:
    logchat = "Dis-Connected ❌"

if isherokuokay:
    riplife = "Connected ✅"
else:
    riplife = "Not Connected ❌"

if gdriveisshit:
    wearenoob = "Active ✅"
else:
    wearenoob = "Inactive ❌"

if rmbg:
    gendu = "Added ✅"
else:
    gendu = "Not Added ❌"

if wttrapi:
    starknoobs = "Added ✅"
else:
    starknoobs = "Not Added ❌"

if hmmok:
    meiko = "Added ✅"
else:
    meiko = "Not Added ❌"

if isdbfine:
    dbstats = "Fine ✅"
else:
    dbstats = "Not Fine ❌"

inlinestats = (f"✘ SHOWING FRIDAY STATS ✘\n"
               f"VERSION = {currentversion} \n"
               f"DATABASE = {dbstats} \n"
               f"SUDO = {amiusingsudo} \n"
               f"LOG-CHAT = {logchat} \n"
               f"HEROKU = {riplife} \n"
               f"G-DRIVE = {wearenoob}")