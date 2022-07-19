import discord   # import discord.py
import os        # gae ngambil barang dr environment
import random    # random nums gennerator
import pytz
from datetime import datetime, date, time, timezone

# Variables/ Properties
client = discord.Client()
diceNums = [1, 2, 3, 4, 5, 6]
hololiveMembers = ['Tokino Sora', 'Roboco', 'Sakura Miko', 'Hoshimachi Suisei', 'AZKi', 'Yozora Mel', 'Shirakami Fubuki', 'Natsuiro Matsuri', 'Akai Haato', 'Aki Rosenthal', 'Minato Aqua', 'Murasaki Shion', 'Nakiri Ayame', 'Yuzuki Choco', 'Oozora Subaru', 'Ookami Mio', 'Nekomata Okayu', 'Inugami Korone', 'Usada Pekora', 'Shiranui Flare', 'Shirogane Noel', 'Houshou Marine', 'Uruha Rushia', 'Amane Kanata', 'Tsunomaki Watame', 'Tokoyami Towa', 'Himemori Luna', 'Kiryu Coco', 'Yukihana Lamy', 'Momosuzu Nene', 'Shishiro Botan', 'Omaru Polka', 'Mano Aloe', 'La+ Darkness', 'Takane Lui', 'Hakui Koyori', 'Sakamata Chloe', 'Kazama Iroha', 'Mori Calliope', 'Takanashi Kiara', "Ninomae Ina'nis", 'Gawr Gura', 'Watson Amelia', 'IRyS', 'Tsukumo Sana', 'Ceres Fauna', 'Ouro Kronii', 'Nanashi Mumei', 'Hakoz Baelz']
UTC = pytz.utc
IST = pytz.timezone('America/Indiana/Indianapolis')
SBY = pytz.timezone('Asia/Jakarta')

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
def aslocaltimestr(utc_dt):
  return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')



#lek bot e tangi
@client.event
async def on_ready():
  print('Good Morning MF!!! - {0.user}'.format(client))

# lek ngirim message
@client.event
async def on_message(message):
  # make all messages lower case
  lowerCaseMsg = message.content.lower()
  
  # supaya bot e ga baca msg ne dw
  if message.author == client.user:
    return
  
  # baca string tertentu
  if message.content.startswith('$hello'):
    await message.channel.send('Sup Bitj :3')
  if message.content.startswith('$aqua'):
    await message.channel.send('https://imgur.com/Kj7QIfl')

  # roll custom num range
  # if(message.content.startswith('roll') && ):
  
  # roll a dice
  if message.content.startswith('$roll'):
    chosenNum = random.choice(diceNums)
    await message.channel.send('You rolled> ' + str(chosenNum))

  # random waifu picker
  if(lowerCaseMsg.startswith('$hololiveWaifu') or lowerCaseMsg.startswith('$hw')):
    chosenHololiveWaifu = random.randrange(0, len(hololiveMembers), 1)
    await message.channel.send('Your waifu is ' + hololiveMembers[chosenHololiveWaifu])

  # time
  if(lowerCaseMsg.startswith('$checktime') or lowerCaseMsg.startswith('$ct')):
    #await message.channel.send('current time(iso format)> ' + aslocaltimestr(datetime.now().isoformat()))
    #await message.channel.send('current time(ctime)> ' + aslocaltimestr(datetime.now().ctime()))
    await message.channel.send('ISO FORMAT')
    await message.channel.send('current time(UTC time test)> ' + datetime.now(UTC).isoformat())
    await message.channel.send('current time(aljosh)> ' + datetime.now(IST).isoformat())
    await message.channel.send('current time(hoganRicad)> ' + datetime.now(SBY).isoformat())
    await message.channel.send('CTIME')
    await message.channel.send('current time(UTC time test)> ' + datetime.now(UTC).ctime())
    await message.channel.send('current time(aljosh)> ' + datetime.now(IST).ctime())
    await message.channel.send('current time(hoganRicad)> ' + datetime.now(SBY).ctime())

client.run(os.getenv('TOKEN'))


#"<@"+str(people)+">"
#people = message.mentions[0].id