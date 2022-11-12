import os
import openai
import discord
import json

intents = discord.Intents.default()
#intents.message_content = True

client = discord.Client(intents=intents)

openai.api_key ="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"

stdPrompt = "Your name is DoctorBot and you are an AI therapist. Your goal is to make the user feel better\n\nHello!\n"
memory = stdPrompt



@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global memory

  if str(message.content).startswith("!reset"):
    memory = stdPrompt
    return
  if str(message.content).startswith("!print"):
    print(memory)
    return

  memory += str(message.content) + "\n"

  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=memory,
    temperature=.95,
    max_tokens=245,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
  )

  json_object = json.loads(str(response))
  memory += json_object['choices'][0]['text'].split("\n")[-1] + "\n"
  await message.channel.send(json_object['choices'][0]['text'].split("\n")[-1])

client.run('MTA0MTA4Mzc0NzkwMDA4NDMzNQ.G8OJVD.j9M0h4xEjgZt0Q6jFLz6rOXTLcLAALp4M4qwNc')