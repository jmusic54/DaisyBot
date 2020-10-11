# DaisyBot
My submission for the hackathon KnightHacks 2020, of which I am the sole contributor. DaisyBot is a Discord bot that allows the user to track their mood, and if they choose to, be routinely notified via a ping to do their mood tracking. The bot utilizes the Discord API, discord.py, and MongoDB with PyMongo and the Google Cloud hosting platform. This bot was made at a beginner (no prior experience) level of MongoDB and PyMongo, and a semi-beginner (some prior experience) level of Python, discord.py, and the Discord API.

## Author
* Joshua Schladt

## Getting Started
You can download the source code for the repository as a ZIP file, or use Git by typing the following command into a terminal:

 ```git clone https://github.com/jmusic54/DaisyBot```

You will need to have Python installed along with the following modules installed for the code, which you can do by running the following commands in your command line:

```pip install discord.py```

```pip install pymongo```

```pip install dnspython```
 
## What is DaisyBot?
DaisyBot is a mental health focused bot that allows for discord users to track their mood, write a bio, and store a journal entry. The nifty commands that DaisyBot allows the user to do involve:
* ```!botinfo```
    * Lets the user see info about DaisyBot in an embedded format.
* ```!commandlist```
    * Lets the user see all of the available commands that DaisyBot offers, along with an explanation of said commands in an embedded format.
* ```!trackmood```
    * Allows the user to track their mood and and store it to the database.
* ```!trackjournal```
    * Allows the user to write a journal entry and stores it to the database.
* ```!setbio```
    * Allows the user to write a bio and stores it to the database.
* ```!getmood/journal/bio```
    * Three different commands that retrieve the mood, journal entry, and bio for the user from the database, depending on which one was inputted.

## Built With
* Discord API
* discord.py
* Google Cloud API
* MongoDB
* PyMongo
* Python 3.8
