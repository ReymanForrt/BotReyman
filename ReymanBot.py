import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import os
from discord.ext import commands
import time
import asyncio

client = commands.Bot(command_prefix="?")


@client.command()
async def support(ctx):
    await ctx.channel.send("Нужна поддержка?Напиши письмо на почту helpivreibot@gmail.com")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Pycharm'))
    print("Бот готов")

@client.command()
async def channel(ctx):
    await ctx.channel.send('Подпишсь https://www.youtube.com/channel/UCR9Yjz7lJMeDU-qUmlj16bw?view_as=subscriber')





client.run('NzA1Nzc2OTY0MTcwMDIyOTU0.XvT0kg.MpOjjdAwBE0_PGlOqkx43AE9aGg')
