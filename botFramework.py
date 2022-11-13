import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def check(channel):
    if isinstance(channel, discord.channel.DMChannel):
        return True
    else:
        return False

async def send_dm(member: discord.Member, content):
    channel = await member.create_dm()
    await channel.send(content)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if await check(message.channel):
        #IF IN DMS
        if str(message.content).startswith("!reset"):
            await message.channel.send("Resetting")
            #RESET CODE
        elif str(message.content).startswith("!clear"):
            await message.channel.send("Clearing")
            #CLEAR CONVERSATION
            async for m in message.channel.history():
                if m.author == client.user:
                    await m.delete()
        elif str(message.content).startswith("!info"):
            await message.channel.send("This bot was made for **HackUTD IX** by **Brandon Robertiello** and **Nate Reese**!")
            #BOT INFO
        elif str(message.content).startswith("!help"):
            await message.channel.send("**Help Menu**")
            #HELP INFO
            await message.channel.send("**!reset** to reset memory\n**!clear** to clear conversation\n**!info** to see bot information")
        else:
            await message.channel.send("This would be my AI generated response")
            #FILL WITH OPENAI CODE
    else:
        #IF IN REGULAR CHANNEL
        if client.user.mentioned_in(message):

            users = [user_mentioned for user_mentioned in message.mentions]
            users.remove(client.user)

            if(len(users)>0):

                for u in users:
                    await send_dm(u, f"*someone mentioned you and DoctorBot in another server, use **!help** for commands*\n\nHello, <@{u.id}>!\nMy name is **DoctorBot** and I'm here to assist you!\nHow are you feeling today?")

                await message.delete()

            else:

                user = message.author
                user_id = user.id

                #DELETE ALL PREVIOUS DMS
                #for ch in client.private_channels:
                #    if await check(ch):
                #        messages = ch.history()
                #        async for m in messages:
                #            if m.author == client.user:
                #                await m.delete()

                await send_dm(message.author, f"*you mentioned DoctorBot in another server, use **!help** for commands*\n\nHello, <@{user_id}>!\nMy name is **DoctorBot** and I'm here to assist you!\nHow are you feeling today?")
                await message.delete()

client.run('token')

#PERMISSIONS
#READ MESSAGES / VIEW CHANNEL
#SEND MESSAGES
#MANAGE MESSAGES