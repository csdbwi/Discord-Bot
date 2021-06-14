import discord
from discordToken import TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    if message.content == 'hello' or message.content == 'Hello':
        await message.channel.send('Pog')

client.run(TOKEN)