import discord
import user_info

f = open("token.txt", "r")
TOKEN = f.read()
f.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event

async def on_ready():

    print('We have successfully loggged in as {0.user}'.format(client))


@client.event

async def on_message(message):

    if message.author == client.user:

        return



    if message.content.lower() == 'hello':

        await message.channel.send(f'Hello, {message.author.display_name}!')

        return



    if message.content.lower() == 'bye':

        await message.channel.send(f'See you later, {message.author.display_name}!')

        return
    

async def ping(ctx):
    await ctx.send("pong")


client.run(TOKEN)