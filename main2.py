import discord
from discord.ext import commands
import user_info

f = open("token.txt", "r")
TOKEN = f.read()
f.close()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def run():

    
    
    @bot.command()
    async def ping(ctx):
        username = "PunjiChocoBerry"
        embed = user_info.generate_response(username)
        await ctx.send(embed=embed)
        
    @bot.group()
    async def pvzcc(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("nuh")
    
    @bot.command()
    async def user(ctx, username):
        embed = user_info.generate_response(username)
        await ctx.send(embed=embed)
        
    bot.run(TOKEN)
    

if __name__ == "__main__":
    run()