import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Good Morning MF!!! - {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Sup Bitj :3')
  if message.content.startswith('$aqua'):
    await message.channel.send('https://imgur.com/Kj7QIfl')

client.run(os.getenv('TOKEN'))


#"<@"+str(people)+">"
#people = message.mentions[0].id