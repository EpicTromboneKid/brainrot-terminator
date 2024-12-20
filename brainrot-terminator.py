# This example requires the 'message_content' intent.

import discord
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

with open('config.json', 'r') as file:
    data = json.load(file)

token = data['token']

brainrot_words = brainrot_words = [
    "skibidi", "rizz", "gyatt", 'gyat', "sigma", "npc", "cap", "pov", "sus", "finsta", "FYP",
    "simp", "yeet", "bussin", "flex", "ghosting", "clout", "mid", "slaps", "ohio", "sussy",
    "fanum", "gronk", "livvy", "maxxing", 'mog', "galvanized square"
]

disable = False
mentions = False
physics = True

def toggle(arg):
    global disable
    disable = arg
    return disabled

def disabled():
    return disable

def physicsmain(arg):
    global physics
    physics = arg
    return main

def main():
    return physics

def mention(arg):
    global mentions
    mentions = arg
    return mentions

def mentionstatus():
    return mentions
    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
 


@client.event
async def on_message(message):

    if message.content == 'brainrot shut the frik up':
        await message.channel.send('no u')

    # elif message.content == 'brainrot shut the frick up' and message.author.name == 'ic8300':
    #     physicsmain(False)
    #     await message.channel.send('Ok physics main!')
    # elif message.content == 'brainrot where r u' and message.author.name == 'ic8300':
    #     physicsmain(True)
    #     await message.channel.send('PHYSICS MAIN!!!!!!')
        

    if 'oppenheimer' in message.content.lower():
        await message.channel.send('I am become death, destroyer of worlds.')
        await message.channel.send(file=discord.File('oppenheimer.jpeg'))

    if message.author == client.user:
        return
    
    if message.content == '!brainrot off':
        toggle(True)
        await message.channel.send('Brainrot detection has been disabled.')

    elif message.content == '!brainrot on': 
        toggle(False)
        await message.channel.send('Brainrot detection has been enabled.')

    if message.content == '!brainrot status':
        if disabled():
            await message.channel.send('Brainrot detection is currently disabled.')
        else:
            await message.channel.send('Brainrot detection is currently enabled.')
    
    if message.content == '!mentions status':
        if mentionstatus():
            await message.channel.send('Mentions are currently enabled.')
        else:
            await message.channel.send('Mentions are currently disabled.')

    if message.content == '!mentions on':
        mention(True)
        await message.channel.send('Mentions have been enabled.')
    
    elif message.content == '!mentions off':
        mention(False)
        await message.channel.send('Mentions have been disabled.')

    for word in brainrot_words:
        if not disabled() and word.lower() in message.content.lower():
            print(f'Brainrot word detected: {word}')
            await message.delete()
            if mentionstatus():
                await message.channel.send(f'You said a brainrot word, {message.author.mention}! >:(')
            else:
                await message.channel.send(f'You said a brainrot word, {message.author.name}! >:(')


client.run(token)
