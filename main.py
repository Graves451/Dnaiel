import discord
import json

client = discord.Client()

file_dir = ""

#reading the file
with open(file_dir,"r") as f:
    file = f.read()
f.close()

#intializing the bot
@client.event
async def on_ready():
    print("Dnaiel's online and ready to go!")

@client.event
async def on_reaction_add(reaction,user):
    print(reaction)

@client.event
async def on_message(message):
    #made here so that the bot doesn't respond to it's own messages
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

def write(newfile):
    with open(file_dir,"w") as w:
        json.dump(newfile,w,indent=4)
    w.close()


client.run('your token here')
