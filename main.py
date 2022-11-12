import os
import discord
import random
import threading
from discord import client
import requests
import json
from dotenv import load_dotenv

class M_handler:

    def __init__(self,message):
        self.message=message
        global content
        self.content=self.message.content.lower()


    async def send(self,content):
        print("sending")
        await self.message.channel.send(content)
        print("sent")

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    m_handler = M_handler(message)

    if message.content.startswith('$hello'):
        await message.channel.send('Helloooooo!!')

async def send(m_handler):


async def recieve(m_handler):


client.run(os.getenv('TOKEN'))