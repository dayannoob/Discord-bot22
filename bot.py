import os
import discord
from discord.ext import commands

# فعال کردن Intents
intents = discord.Intents.default()
intents.message_content = True

# ساخت ربات با prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# وقتی ربات روشن شد
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    # وضعیت ربات را آنلاین و با Activity مشخص می‌کنیم
    await bot.change_presence(activity=discord.Game(name="!ping"))

# دستور ساده ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# اجرای ربات با توکن از Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)
