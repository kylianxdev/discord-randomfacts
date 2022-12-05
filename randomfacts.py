import discord
import time
import requests

client = discord.Client(
    intents=discord.Intents.all()
)

@client.event
async def on_ready():
    print('Bot is ready')
    while True:
        fun_fact = get_random_fun_fact()
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(fun_fact)
        time.sleep(60 * 15)

def get_random_fun_fact():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = response.json()
    return data["text"]

client.run('YOUR_TOKEN_HERE')