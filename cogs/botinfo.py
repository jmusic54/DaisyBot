import discord
from discord.ext import commands


class BotInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    # displays bot info in an embedded format
    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title='DaisyBot',
            description='DaisyBot is a bot created by Joshua Schladt for the KnightHacks 2020 Hackathon. DaisyBot was written in Python and utilizes the Discord API, discord.py, and MongoDB with PyMongo to allow the user to track and store their mood, write a journal entry, and write a bio.',
            color=discord.Color.dark_purple()
        )
        embed.set_footer(text='What DaisyBot looks like.')
        embed.set_image(url='https://cdn.discordapp.com/attachments/764802563228303390/764802607617146881/botlogo.png')

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(BotInfo(client))
