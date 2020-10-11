import asyncio
from pymongo import MongoClient
import mongo
from discord.ext import commands


class SetBio(commands.Cog):

    def __init__(self, client):
        self.client = client

    # main mood tracking command
    @commands.command()
    async def setbio(self, ctx):
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

        await ctx.send('Input your user bio.')

        # take in user response for bio and have bot store data to MongoDB
        bioResponse = await self.client.wait_for('message', check=check, timeout=600)
        await ctx.send('User bio complete. Let me get that stored for you.')
        bioInsert = {"_id": ctx.author.id, "entry": bioResponse.content}
        collection.insert_one(bioInsert)

        await ctx.send("Journal entry stored.")


def setup(client):
    client.add_cog(SetBio(client))
