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
    "69", "skibidi", "rizz", "gyatt", 'gyat', "sigma", "NPC", "cap", "POV", "sus", "finsta", "FYP",
    "simp", "stan", "yeet", "bussin", "flex", "ghosting", "clout", "mid", "slaps", "ohio", "sussy",
]


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for word in brainrot_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f'You said a brainrot word, {message.author.mention}!')

client.run(token)
