import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
	print(f"Bot logged as {bot.user}")

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return

	if "ping" == message.content:
		await message.channel.send("pong!")

TOKEN = os.environ['TOKEN']

bot.run(TOKEN)