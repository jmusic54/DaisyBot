import discord
from discord.ext import commands


class ServerInfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    # displays server info
    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.send(
            'Welcome to The Mental Garden! Our bot, DaisyBot will be here to help you track your mental health. Visit the <#764607333854347264> channel to see more info about the commands!')


def setup(client):
    client.add_cog(ServerInfo(client))
