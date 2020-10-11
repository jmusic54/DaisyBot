import discord
from discord.ext import commands


class SetReminder(commands.Cog):

    def __init__(self, client):
        self.client = client

    # command that will let the bot set whether or not they would like to be pinged every day to be reminded to do their tracking
    @commands.command()
    async def setreminder(self, ctx):
        await ctx.send(
            'Would you like me to ping you every day to remind you to do your mood tracking? Please respond with yes or no.')

        # check so that only user who sent initial command can input response
        def check(author):
            def inner_check(message):
                if message.author != author:
                    return False

            return inner_check

        # take in user response and have bot output corresponding response to the user
        remindresponse = await self.client.wait_for('message', check=check, timeout=60)
        if remindresponse.clean_content.lower() == 'Yes' or 'yes':
            await ctx.send('I will ping you every day to remind you to do your mood tracking.')
        elif remindresponse.clean_content.lower() == 'No' or 'no':
            await ctx.send('I will not ping you every day to remind you to do your mood tracking.')
        else:
            await ctx.send('Invalid response. Please run the command from the beginning and try again.')


def setup(client):
    client.add_cog(SetReminder(client))
