from pymongo import MongoClient
import mongo
from discord.ext import commands


class GetJournal(commands.Cog):

    def __init__(self, client):
        self.client = client

    # command for getting journal entry
    @commands.command()
    async def getjournal(self, ctx):
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
                try:
                    int(message.content)
                    return True
                except ValueError:
                    return False

            return inner_check

        # get and print journal entry from database
        for entry in collection.find():
            await ctx.send(entry)


def setup(client):
    client.add_cog(GetJournal(client))
