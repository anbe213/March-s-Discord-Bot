import discord, os, requests, json
import ChessMain

client = discord.Client()

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + ' +' + json_data[0]['a']
  return quote


@client.event
async def on_ready():
  print('We has logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!xl'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if message.content == ('!chess'):
    chessBoard = ChessMain.GameMain
    await message.channel.send('Game starting')



client.run(os.getenv('TOKEN'))