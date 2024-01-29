# Api : https://api.crafty.gg/api/v2/players?limit=18&page=1&search=
import discord
import json
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix="!" , intents=discord.Intents.all())


@bot.command()
async def profile(ctx , username):
    if username is not None :
        request = requests.get(f"https://api.crafty.gg/api/v2/players?limit=18&page=1&search={username}")
        info = request.json()
        embed = discord.Embed(description=f"User Profile `{username}`\n\n``skin_count : {info['data'].get('skins_count',None)}\nuuid : {info['data'].get('uuid',None)}\nid : {info['data'].get('id',None)}``")
        await ctx.send(embed=embed)


bot.run(Token)
