import os

import discord
from dotenv import load_dotenv
from tahm_demo import chat2
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
@client.event
async def  on_message(message):
    if message.author == client.user:
        return
    
    await message.channel.send(chat2(message.content))
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)