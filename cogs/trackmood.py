import discord
import asyncio
from discord.ext import commands


class TrackMood(commands.Cog):

    def __init__(self, client):
        self.client = client

    # main mood tracking command
    @commands.command()
    async def trackmood(self, ctx):
        await ctx.send('Hello! Lets track your mood for the day.')
        await asyncio.sleep(1)
        await ctx.send(
            'How was your day? Reply with the number 1, 2, or 3 depending on how your day was. \n1: My day was great. \n2: My day was fine. \n3. My day could have been better.')

        # check so that only user who sent initial command can input response
        def check(author):
            def inner_check(message):
                if message.author != author:
                    return False
                try:
                    int(message.content)
                    return True
                except ValueError:
                    return False

            return inner_check

        # take in user response and have bot output corresponding response to the user
        moodresponse = await self.client.wait_for('message', check=check, timeout=60)
        if moodresponse.clean_content.lower() == '1':
            await ctx.send('You said your day was great. Let me get that stored for you.')
        elif moodresponse.clean_content.lower() == '2':
            await ctx.send('You said your day was fine. Let me get that stored for you.')
        elif moodresponse.clean_content.lower() == '3':
            await ctx.send('You said your day could have been better. Let me get that stored for you.')
        else:
            await ctx.send('Invalid response. Please run the command from the beginning and try again.')


def setup(client):
    client.add_cog(TrackMood(client))
