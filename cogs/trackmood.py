import asyncio
from pymongo import MongoClient
import mongo
from discord.ext import commands


class TrackMood(commands.Cog):

    def __init__(self, client):
        self.client = client

    # main mood tracking command
    @commands.command()
    async def trackmood(self, ctx):
        # mongoDB setup
        mongo_url = mongo.mongoCredentials
        cluster = MongoClient(mongo_url)
        db = cluster["daisyDB"]
        collection = db["mooddata"]

        # check so that only user who sent initial command can input response
        def check(author):
            def inner_check(message):
                if message.author != author:
                    return False

            return inner_check

        # take in user response for date and mood and have bot output corresponding response to the user and store data to MongoDB
        await ctx.send('Hello! Lets track your mood for the day.')
        await asyncio.sleep(1)
        await ctx.send('What is the date?')
        date_response = await self.client.wait_for('message', check=check, timeout=120)
        await ctx.send('The date you are storing this entry is ' + date_response.content)
        await asyncio.sleep(1)
        await ctx.send(
            'How was your day? Reply with the number 1, 2, or 3 depending on how your day was. \n1: My day was great. \n2: My day was fine. \n3. My day was not good.')
        mood_response = await self.client.wait_for('message', check=check, timeout=60)
        if mood_response.clean_content.lower() == '1':
            mood = "Good"
            await ctx.send('You said your day was great. Let me get that stored for you.')

            mood_insert = {"_id": ctx.author.id, "date": date_response.content, "mood": mood}
            collection.insert_one(mood_insert)

            await ctx.send("Mood stored.")

        elif mood_response.clean_content.lower() == '2':
            mood = "Fine"
            await ctx.send('You said your day was fine. Let me get that stored for you.')

            mood_insert = {"_id": ctx.author.id, "date": date_response.content, "mood": mood}
            collection.insert_one(mood_insert)

            await ctx.send("Mood stored.")

        elif mood_response.clean_content.lower() == '3':
            mood = "Not Good"
            await ctx.send('You said your day was not good. Let me get that stored for you.')

            mood_insert = {"_id": ctx.author.id, "date": date_response.content, "mood": mood}
            collection.insert_one(mood_insert)

            await ctx.send("Mood stored.")

        else:
            await ctx.send('Invalid response. Please run the command from the beginning and try again.')


def setup(client):
    client.add_cog(TrackMood(client))
