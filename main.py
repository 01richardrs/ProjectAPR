import discord   # import discord.py
import os        # gae ngambil barang dr environment
import random

# Variables/ Properties
client = discord.Client()
diceNums = [1, 2, 3, 4, 5, 6]


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

  # roll a dice
  if message.content.startswith('$roll'):
    chosenNum = random.choice(diceNums)
    await message.channel.send('You rolled> ' + str(chosenNum))

client.run(os.getenv('TOKEN'))


#"<@"+str(people)+">"
#people = message.mentions[0].id