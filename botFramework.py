import discord
import os

#DISCORD CLIENT INITIATION
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#CHECKS IF CHANNEL IS A DM
async def check(channel):
    if isinstance(channel, discord.channel.DMChannel):
        return True
    else:
        return False

#SENDS DM TO USER
async def send_dm(member: discord.Member, content):
    channel = await member.create_dm()
    await channel.send(content)

#CONSOLE LOG
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#WHEN MESSAGE IS RECIEVED
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if await check(message.channel):

        #IF IN DMS

        #RESET BOT MEMORY
        if str(message.content).startswith("!reset"):
            await message.channel.send("Resetting")

        #CLEAR CONVERSATION HISTORY
        elif str(message.content).startswith("!clear"):
            await message.channel.send("Clearing")
            async for m in message.channel.history():
                if m.author == client.user:
                    await m.delete()

        #PRINT BOT INFO
        elif str(message.content).startswith("!info"):
            await message.channel.send("This bot was made for **HackUTD IX** by **Brandon Robertiello** and **Nate Reese**!")

        #PRINT HELP INFO
        elif str(message.content).startswith("!help"):
            await message.channel.send("**Help Menu**")
            await message.channel.send("**!reset** to reset memory\n**!clear** to clear conversation\n**!info** to see bot information")
        
        #AI GENERATED RESPONSE
        else:
            await message.channel.send("This would be my AI generated response")
            #FILL WITH OPENAI CODE

    else:

        #IF IN REGULAR CHANNEL
        if client.user.mentioned_in(message):

            users = [user_mentioned for user_mentioned in message.mentions]
            if(client.user in users):
                users.remove(client.user)

            #IF MULTIPLE USERS MENTIONED
            if(len(users)>0):

                for u in users:
                    await send_dm(u, f"*someone mentioned you and DoctorBot in another server, use **!help** for commands*\n\nHello, <@{u.id}>!\nMy name is **DoctorBot** and I'm here to assist you!\nHow are you feeling today?")

                await message.delete()

            #IF ONLY DOCTORBOT MENTIONED
            else:

                user = message.author
                user_id = user.id

                await send_dm(message.author, f"*you mentioned DoctorBot in another server, use **!help** for commands*\n\nHello, <@{user_id}>!\nMy name is **DoctorBot** and I'm here to assist you!\nHow are you feeling today?")
                await message.delete()

#DISCORD BOT TOKEN
client.run('token')

#PERMISSIONS REQUIRED
    #READ MESSAGES / VIEW CHANNEL
    #SEND MESSAGES
    #MANAGE MESSAGES

#https://discord.com/api/oauth2/authorize?client_id=1041083747900084335&permissions=11264&scope=bot