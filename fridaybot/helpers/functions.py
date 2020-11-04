import requests , os, re
import time
import shlex
import asyncio
import requests
import PIL.ImageOps                        
from os.path import basename                            
from selenium import webdriver                                    
from fridaybot.Configs import Config
from typing import Optional, Tuple
from bs4 import BeautifulSoup
from asyncio import sleep
from random import choice
from telethon import events
from emoji import get_emoji_regexp
from PIL import Image, ImageDraw, ImageFont
from validators.url import url
from .resources.states import states
from telethon.tl.types import Channel, PollAnswer

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time

#gban
async def admin_groups(cat):
    catgroups = []
    async for dialog in cat.client.iter_dialogs():
        entity = dialog.entity  
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            catgroups.append(entity.id)
    return catgroups


# For using gif , animated stickers and videos in some parts , this
# function takes  take a screenshot and stores ported from userge

async def take_screen_shot(video_file: str, duration: int, path: str = '') -> Optional[str]:
    print(
        '[[[Extracting a frame from %s ||| Video duration => %s]]]',
        video_file,
        duration)
    ttl = duration // 2
    thumb_image_path = path or os.path.join(
        "./temp/", f"{basename(video_file)}.jpg")
    command = f"ffmpeg -ss {ttl} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None

# executing of terminal commands


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return (stdout.decode('utf-8', 'replace').strip(),
            stderr.decode('utf-8', 'replace').strip(),
            process.returncode,
            process.pid)

# for getmusic


async def catmusic(cat, QUALITY, hello):
    search = cat
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = Config.CHROME_BIN
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.youtube.com/results?search_query=' + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute('href')
        break
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not video_link:
        await hello.edit(f"Sorry. I can't find that song `{search}`")
        return
    try:
        command = (
            'youtube-dl -o "./temp/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality ' +
            QUALITY +
            ' ' +
            video_link)
        os.system(command)
    except Exception as e:
        return await hello.edit(f"`Error:\n {e}`")
    try:
        thumb = (
            'youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' +
            video_link)
        os.system(thumb)
    except Exception as e:
        return await hello.edit(f"`Error:\n {e}`")


async def catmusicvideo(cat, hello):
    search = cat
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = Config.CHROME_BIN
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.youtube.com/results?search_query=' + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
                                           
                                                                            
        video_link = i.get_attribute('href')
        break
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not video_link:
        await hello.edit(f"Sorry. I can't find that song `{search}`")
        return
    try:
        command = (
            'youtube-dl -o "./temp/%(title)s.%(ext)s" -f "[filesize<20M]" ' +
            video_link)
        os.system(command)
    except Exception as e:
        return await hello.edit(f"`Error:\n {e}`")
    try:
        thumb = (
            'youtube-dl -o "./temp/%(title)s.%(ext)s" --write-thumbnail --skip-download ' +
            video_link)
        os.system(thumb)
    except Exception as e:
        return await hello.edit(f"`Error:\n {e}`")

# for stickertxt


async def waifutxt(text, chat_id, reply_to_id, bot, borg):
    animus = [0, 1, 2, 3, 4, 9, 15, 20, 22, 27, 29, 32, 33, 34, 37, 38,
              41, 42, 44, 45, 47, 48, 51, 52, 53, 55, 56, 57, 58, 61, 62, 63]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{choice(animus)}{text}")
    cat = await sticcers[0].click("me",
                                  hide_via=True)
    if cat:
        await borg.send_file(int(chat_id), cat, reply_to=reply_to_id)
        await cat.delete()

# https://github.com/pokurt/LyndaRobot/blob/7556ca0efafd357008131fa88401a8bb8057006f/lynda/modules/helper_funcs/string_handling.py#L238


async def extract_time(cat, time_val):
    if any(time_val.endswith(unit) for unit in ('m', 'h', 'd', 'w')):
        unit = time_val[-1]
        time_num = time_val[:-1]  # type: str
        if not time_num.isdigit():
            cat.edit("Invalid time amount specified.")
            return ""
        if unit == 'm':
            bantime = int(time.time() + int(time_num) * 60)
        elif unit == 'h':
            bantime = int(time.time() + int(time_num) * 60 * 60)
        elif unit == 'd':
            bantime = int(time.time() + int(time_num) * 24 * 60 * 60)
        elif unit == 'w':
            bantime = int(time.time() + int(time_num) * 7 * 24 * 60 * 60)
        else:
            # how even...?
            return ""
        return bantime
    cat.edit("Invalid time type specified. Expected m , h , d or w but got: {}".format(
        time_val[-1]))
    return ""
song_dl = "youtube-dl --force-ipv4 --write-thumbnail -o './temp/%(title)s.%(ext)s' --extract-audio --audio-format mp3 --audio-quality {QUALITY} {video_link}"
thumb_dl = "youtube-dl --force-ipv4 -o './temp/%(title)s.%(ext)s' --write-thumbnail --skip-download {video_link}"
video_dl = "youtube-dl --force-ipv4 --write-thumbnail  -o './temp/%(title)s.%(ext)s' -f '[filesize<20M]' {video_link}"
name_dl = (
    "youtube-dl --force-ipv4 --get-filename -o './temp/%(title)s.%(ext)s' {video_link}"
)
# for stickertxt

async def waifutxt(text, chat_id ,reply_to_id , bot, borg):
    animus = [0, 1, 2, 3, 4, 7, 9, 10, 11, 15, 20, 22, 27, 29, 31, 32, 33, 34, 36, 37, 38, 
              40, 41, 42, 43, 44, 45, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 63]
    sticcers = await bot.inline_query(
        "stickerizerbot", f"#{choice(animus)}{text}")
    cat = await sticcers[0].click( "me" ,
                            hide_via=True)
    if cat:
        await borg.send_file(int(chat_id) , cat , reply_to = reply_to_id ) 
        await cat.delete()

EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, '', inputString)
def Build_Poll(options):
    return [PollAnswer(option, bytes(i)) for i, option in enumerate(options, start=1)]


def convert_toimage(image):
    img = Image.open(image)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    os.remove(image)
    return "temp.jpg"
async def convert_tosticker(image):
    img = Image.open(image)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("./temp/temp.webp", "webp")
    os.remove(image)
    return "./temp/temp.webp"

async def covidindia(state):
    url = "https://www.mohfw.gov.in/data/datanew.json"
    req = requests.get(url).json()
    for i in states:
        if i == state:
            return req[states.index(i)]
    return None
async def fakegs(search, result):
    imgurl = "https://i.imgur.com/wNFr5X2.jpg"
    with open("./temp/temp.jpg", "wb") as f:
        f.write(requests.get(imgurl).content)
    img = Image.open("./temp/temp.jpg")
    drawing = ImageDraw.Draw(img)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font1 = ImageFont.truetype("userbot/helpers/styles/ProductSans-BoldItalic.ttf", 20)
    font2 = ImageFont.truetype("userbot/helpers/styles/ProductSans-Light.ttf", 23)
    drawing.text((450, 258), result, fill=blue, font=font1)
    drawing.text((270, 37), search, fill=black, font=font2)
    img.save("./temp/temp.jpg")
    return "./temp/temp.jpg"

# for nekobot
    
# for nekobot
async def trumptweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=trumptweet&text={text}").json()
        sandy = r.get("message")
        caturl = url(sandy)
        if not caturl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(sandy).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.webp", "webp")    
        return "temp.webp"

async def changemymind(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}").json()
        sandy = r.get("message")
        caturl = url(sandy)
        if not caturl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(sandy).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.jpg", "jpeg")    
        return "temp.jpg"
    
async def kannagen(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=kannagen&text={text}").json()
        sandy = r.get("message")
        caturl = url(sandy)
        if not caturl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(sandy).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.webp", "webp")    
        return "temp.webp"    
    
async def moditweet(text):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi").json()
        sandy = r.get("message")
        caturl = url(sandy)
        if not caturl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(sandy).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.webp", "webp")    
        return "temp.webp"     
    
async def tweets(text1,text2):
        r = requests.get(
            f"https://nekobot.xyz/api/imagegen?type=tweet&text={text1}&username={text2}").json()
        sandy = r.get("message")
        caturl = url(sandy)
        if not caturl:
            return  "check syntax once more"
        with open("temp.png", "wb") as f:
            f.write(requests.get(sandy).content)
        img = Image.open("temp.png").convert("RGB")
        img.save("temp.webp", "webp")    
        return "temp.webp"


async def iphonex(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=iphonex&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def baguette(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=baguette&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png").convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def threats(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def lolice(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=lolice&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def awooify(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=awooify&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"

# http://effbot.org/imagingbook/imageops.html
# https://stackoverflow.com/questions/2498875/how-to-invert-colors-of-image-with-pil-python-imaging/38378828


async def invert_colors(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(endname)


async def flip_image(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.flip(image)
    inverted_image.save(endname)


async def grayscale(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.grayscale(image)
    inverted_image.save(endname)


async def mirror_file(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.mirror(image)
    inverted_image.save(endname)


async def solarize(imagefile, endname):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.solarize(image, threshold=128)
    inverted_image.save(endname)


async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)

async def yt_search(cat):
    try:
        cat = urllib.parse.quote(cat)
        html = urllib.request.urlopen(
            "https://www.youtube.com/results?search_query=" + cat
        )
        user_data = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video_link = None
        if user_data:
            video_link = "https://www.youtube.com/watch?v=" + user_data[0]
        if video_link:
            return video_link
        return "Couldnt fetch results"
    except:
        return "Couldnt fetch results"


async def sanga_seperator(sanga_list):
    for i in sanga_list:
        if i.startswith("🔗"):
            sanga_list.remove(i)
    s = 0
    for i in sanga_list:
        if i.startswith("Username History"):
            break
        s += 1
    usernames = sanga_list[s:]
    names = sanga_list[:s]
    return names, usernames
# unziping file
async def unzip(downloaded_file_name):
    with zipfile.ZipFile(downloaded_file_name, "r") as zip_ref:
        zip_ref.extractall("./temp")
    downloaded_file_name = os.path.splitext(downloaded_file_name)[0]
    return f"{downloaded_file_name}.gif"


# https://github.com/pokurt/LyndaRobot/blob/7556ca0efafd357008131fa88401a8bb8057006f/lynda/modules/helper_funcs/string_handling.py#L238

