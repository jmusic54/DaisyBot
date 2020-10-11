import discord
from discord.ext import commands
import env
import os

client = discord.Client()

client = commands.Bot(command_prefix='!')


# message bot prints to the console when online
@client.event
async def on_ready():
    print('DaisyBot is online!')


# loads the cogs for implementation with discord
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# calls the discord token to run the bot on server, will not be pushed to github for security reasons
client.run(env.DISCORD_TOKEN)
