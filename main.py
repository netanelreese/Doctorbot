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

stdPrompt = "You are an AI therapist named DoctorBot. Respond as if you were a therapist.\n\n"

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

    memory += "You: " + str(message.content) + "\n"

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt= memory + "DoctorBot: ",
      temperature=0.95,
      max_tokens=245,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0
    )

    json_object = json.loads(str(response))
    reply = json_object['choices'][0]['text'][2:]
    memory += "DoctorBot: " + reply + "\n"
    await message.channel.send(reply)

client.run('MTA0MTA4Mzc0NzkwMDA4NDMzNQ.G8OJVD.j9M0h4xEjgZt0Q6jFLz6rOXTLcLAALp4M4qwNc')
