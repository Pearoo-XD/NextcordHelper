

import nextcord
from nextcord.ext import commands
import os

# The bot
client = commands.AutoShardedBot(command_prefix = "prefix", intents = nextcord.Intents.default())
client.remove_command("help")

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.event
async def on_ready():
    print(f"Bot successfully started!")
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"{client.command_prefix}help"))

client.run("INSERT_YOUR_TOKEN_HERE")


@commands.command(aliases=["yes"], usage=".yes", description = "yeah")
@commands.guild_only(True)
@commands.has_permissions(manage_messages=True)
@commands.bot_has_permissions(manage_messages=True)
@commands.cooldown(1, 2, commands.BucketType.member)
async def yas(ctx):
    await ctx.send("yes my friend")