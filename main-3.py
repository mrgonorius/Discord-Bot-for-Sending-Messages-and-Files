import discord
from discord.ext import commands
from flask import Flask
import threading


intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Clientside was successfully turned on.")


@bot.command()
@commands.has_permissions(administrator=True)
async def antifilet(ctx):
    await ctx.send(f"The message can be put here.")



app = Flask("")

@app.route("/")
def home():
    return "Clientside is now online!"

def run_web_server():
    app.run(host="0.0.0.0", port=8080)

thread = threading.Thread(target=run_web_server)
thread.start()



bot.run("TOKEN_HERE")
