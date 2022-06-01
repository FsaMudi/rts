import discord
from discord.ext import commands
import requests
import asyncio
import time
from quest import question
from sheets import GoogleSheet
import datetime

date = str(datetime.datetime.now())






DISCORD_BOT_TOKEN = '' #token

client = discord.Client()

googlesheet = GoogleSheet()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        print('Started')
    elif before.channel is not None and after.channel is None:
        user = client.get_user(member.id)
        user = await client.fetch_user(member.id)
        for role in member.roles:
            if role.name == 'Test':
                print('Teacher!')
            else:   
                await user.send(embed = discord.Embed(description = f'{question[0]}', colour = discord.Color.green()))



@client.event
async def on_message(message):
    if message.content.startswith('1.'):
        member = message.author.id
        name = message.author.name
        content = message.content
        user = client.get_user(member)
        user = await client.fetch_user(member)
        await user.send(embed = discord.Embed(description = f'Спасибо за оценку', colour = discord.Color.green()))
        googlesheet.sendData(name, str(member), content[2:], date)









client.run(DISCORD_BOT_TOKEN)


