import discord
from discord.ext import commands
import requests
import xml.etree.ElementTree as ET

import config

TOKEN = config.TOKEN

description = "a happy robot made with aloha running on a tiny VM in makakilo"
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """hello world"""
    await ctx.send('world')

@bot.command()
async def shakka(ctx):
    """throws you a sweet shakka"""
    await ctx.send('aloha :call_me:')

@bot.command()
async def surf(ctx):
    """queries weather.gov and gives the Oahu surf report"""
    r = requests.get('https://www.weather.gov/source/hfo/xml/Surf.xml')
    root = ET.fromstring(r.content)
    await ctx.send(
        f"The {root[0][0].text} last updated {root[0][6].text}.\n"
        f"{root[0][9][2].text}"
        )

bot.run(TOKEN)
