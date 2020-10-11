import discord
from discord.ext import commands


class CommandList(commands.Cog):

    def __init__(self, client):
        self.client = client

    # list of commands in an embedded format
    @commands.command()
    async def commandlist(self, ctx):
        embed = discord.Embed(
            title='Command List',
            color=discord.Color.dark_purple()
        )
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/764802563228303390/764802607617146881/botlogo.png')
        embed.add_field(name='!botinfo', value='Displays info about DaisyBot.', inline=True)
        embed.add_field(name='!commandlist', value='Display the list of commands.', inline=True)
        embed.add_field(name='!trackmood',
                        value='Allows the user to track their mood and and store it to the database.', inline=True)
        embed.add_field(name='!trackjournal',
                        value='Allows the user to write a journal entry and stores it to the database.', inline=True)
        embed.add_field(name='!setbio', value='Allows the user to write a bio and stores it to the database.',
                        inline=True)
        embed.add_field(name='!getmood/journal/bio',
                        value='Three different commands that retrieve the mood, journal entry, and bio for the user from the database, depending on which one was inputted.',
                        inline=True)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(CommandList(client))
