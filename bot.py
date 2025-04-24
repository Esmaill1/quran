import discord
from discord.ext import commands

TOKEN = "YOUR_DISCORD_BOT_TOKEN"
STREAM_URL = "https://stream.radiojar.com/0tpy1h0kxtzuv"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(STREAM_URL), after=lambda e: print("Stream ended.", e))
        await ctx.send("📻 Quran FM is now playing.")
    else:
        await ctx.send("You need to be in a voice channel!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Disconnected from the voice channel.")
    else:
        await ctx.send("I'm not in a voice channel.")

bot.run(TOKEN)
