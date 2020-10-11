import asyncio
from pymongo import MongoClient
import mongo
from discord.ext import commands


class TrackJournal(commands.Cog):

    def __init__(self, client):
        self.client = client

    # main mood tracking command
    @commands.command()
    async def trackjournal(self, ctx):
        # mongoDB setup
        mongo_url = mongo.mongoCredentials
        cluster = MongoClient(mongo_url)
        db = cluster["daisyDB"]
        collection = db["journaldata"]

        # check so that only user who sent initial command can input response
        def check(author):
            def inner_check(message):
                if message.author != author:
                    return False

            return inner_check

        # take in user response for date and journal entry and have bot store data to MongoDB
        await ctx.send('Hello! This command lets you write a journal entry about your day.')
        await asyncio.sleep(1)
        await ctx.send('What is the date?')
        date_response = await self.client.wait_for('message', check=check, timeout=120)
        await ctx.send('The date you are storing this entry is ' + date_response.content)
        await asyncio.sleep(1)
        await ctx.send(
            'Input your journal entry.')
        journal_response = await self.client.wait_for('message', check=check, timeout=600)
        await ctx.send('Journal entry complete. Let me get that stored for you.')
        journal_insert = {"_id": ctx.author.id, "date": date_response.content, "entry": journal_response.content}
        collection.insert_one(journal_insert)

        await ctx.send("Journal entry stored.")


def setup(client):
    client.add_cog(TrackJournal(client))
