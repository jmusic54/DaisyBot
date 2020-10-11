from pymongo import MongoClient
import mongo
from discord.ext import commands


class GetBio(commands.Cog):

    def __init__(self, client):
        self.client = client

    # main mood tracking command
    @commands.command()
    async def getbio(self, ctx):
        # mongoDB setup
        mongo_url = mongo.mongoCredentials
        cluster = MongoClient(mongo_url)
        db = cluster["daisyDB"]
        collection = db["userbio"]

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

        # get and print user bio from database
        for entry in collection.find():
            await ctx.send(entry)


def setup(client):
    client.add_cog(GetBio(client))
