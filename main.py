import os
import openai
import discord
import json

intents = discord.Intents.default()
#intents.message_current = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

stdPrompt = "You are an AI therapist named DoctorBot. Respond as if you were a therapist. \n\n"

memory = stdPrompt

openai.api_key = "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"

@client.event
async def on_message(message):

    global memory

    if message.author == client.user:
        return

    if str(message.content).startswith("!print"):
        print(memory)
        return

    if str(message.content).startswith("!reset"):
        memory = stdPrompt
        return

    memory += "You: " + str(message.content) + "\nDoctorBot: "

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt= memory,
      temperature=0.95,
      max_tokens=500,
      top_p=1.0,
      frequency_penalty=2.0,
      presence_penalty=1.0
    )

    json_object = json.loads(str(response))
    reply = json_object['choices'][0]['text']
    memory += reply + "\n"
    await message.channel.send(reply)

client.run('MTA0MTA4Mzc0NzkwMDA4NDMzNQ.G4Y44v.1Tv4sJmgQabbUziG0nZnTDBpPx-9ErXlxrmAKw')
