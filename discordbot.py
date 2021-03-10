import discord
import asyncio
import ytvid
import json

client = discord.Client()

with open("data.json", "r") as f:
    data = json.loads(f.read())

yt = ytvid.vid(data["id"], data["key"])

@client.event
async def on_message(message):
    await message.author.send("Started notify system!")

    #latestid = yt.parsevid()[0]

    latestid = ""

    request = 0

    while True:
        newvid = yt.parsevid()
        if latestid != newvid[0]:
            msg = f"{message.author.mention} \nLTT posted a new video!: {newvid[1]}. Link: https://youtu.be/{newvid[0]}"
            await message.author.send(msg)
            print(msg)
            latestid = newvid[0]

        await asyncio.sleep(30)

        print(request)
        
        request += 1

client.run(data["token"])