import discord
from discord.ext import commands
from config import settings




bot = commands.Bot(command_prefix = settings['prefix']) #Префикс в config.py
    
    
    
@bot.command() 
async def start(ctx): 
    file1 = open('1question.txt', encoding='utf-8') #Открытие файла
    file2 = open('2question.txt', encoding='utf-8')
    file3 = open('3question.txt', encoding='utf-8')
    file4 = open('4question.txt', encoding='utf-8')
    file5 = open('5question.txt', encoding='utf-8')
    read1 = file1.read() #Просмотр содержимого файла
    read2 = file2.read()
    read3 = file3.read()
    read4 = file4.read()
    read5 = file5.read()
    await ctx.send(read1) #Сообщение
    await ctx.send(read2)
    await ctx.send(read3)
    await ctx.send(read4)
    await ctx.send(read5) 
    






bot.run(settings['token'])

