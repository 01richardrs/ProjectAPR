import discord   # import discord.py
import os        # gae ngambil barang dr environment
import random    # random nums gennerator

# Variables/ Properties
client = discord.Client()
diceNums = [1, 2, 3, 4, 5, 6]
hololiveMembers = ['Tokino Sora', 'Roboco', 'Sakura Miko', 'Hoshimachi Suisei', 'AZKi', 'Yozora Mel', 'Shirakami Fubuki', 'Natsuiro Matsuri', 'Akai Haato', 'Aki Rosenthal', 'Minato Aqua', 'Murasaki Shion', 'Nakiri Ayame', 'Yuzuki Choco', 'Oozora Subaru', 'Ookami Mio', 'Nekomata Okayu', 'Inugami Korone', 'Usada Pekora', 'Shiranui Flare', 'Shirogane Noel', 'Houshou Marine', 'Uruha Rushia', 'Amane Kanata', 'Tsunomaki Watame', 'Tokoyami Towa', 'Himemori Luna', 'Kiryu Coco', 'Yukihana Lamy', 'Momosuzu Nene', 'Shishiro Botan', 'Omaru Polka', 'Mano Aloe', 'La+ Darkness', 'Takane Lui', 'Hakui Koyori', 'Sakamata Chloe', 'Kazama Iroha', 'Mori Calliope', 'Takanashi Kiara', "Ninomae Ina'nis", 'Gawr Gura', 'Watson Amelia', 'IRyS', 'Tsukumo Sana', 'Ceres Fauna', 'Ouro Kronii', 'Nanashi Mumei', 'Hakoz Baelz']


#lek bot e tangi
@client.event
async def on_ready():
  print('Good Morning MF!!! - {0.user}'.format(client))

# lek ngirim message
@client.event
async def on_message(message):
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
  lowerCaseMsg = message.content.lower()
  if(lowerCaseMsg.startswith('$hololiveWaifu') or lowerCaseMsg.startswith('$hw')):
    chosenHololiveWaifu = random.randrange(0, len(hololiveMembers), 1)
    await message.channel.send('Your waifu is ' + hololiveMembers[chosenHololiveWaifu])

client.run(os.getenv('TOKEN'))


#"<@"+str(people)+">"
#people = message.mentions[0].id