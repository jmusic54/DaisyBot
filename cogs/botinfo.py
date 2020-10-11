from discord.ext import commands


class BotInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    # displays bot info
    @commands.command()
    async def botinfo(self, ctx):
        await ctx.send(
            '```DaisyBot is a bot created by Joshua Schladt for the KnightHacks 2020 Hackathon. DaisyBot was written in Python and utilizes the Discord API, discord.py, and MongoDB with PyMongo to allow the user to track and store their mood.```')

def setup(client):
    client.add_cog(BotInfo(client))
