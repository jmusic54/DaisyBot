from discord.ext import commands


class CommandList(commands.Cog):

    def __init__(self, client):
        self.client = client

    # list of commands
    @commands.command()
    async def commandlist(self, ctx):
        await ctx.send(
            'Here are the current list of commands that DaisyBot can perform: \n```!serverinfo \n!botinfo \n!commandlist \n!trackmood \n!trackjournal \n!setbio```')


def setup(client):
    client.add_cog(CommandList(client))
