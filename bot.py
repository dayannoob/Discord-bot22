from flask import Flask
import threading
import os
from discord.ext import commands
import discord

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

# اجرا کردن Flask در Thread جداگانه
threading.Thread(target=run).start()+

# فعال کردن Intents کامل برای دریافت پیام‌ها
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # اضافه کردن این خط برای اطمینان

# ساخت ربات با prefix "!"
bot = commands.Bot(command_prefix="!", intents=intents)

# وقتی ربات روشن شد
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    await bot.change_presence(activity=discord.Game(name="!ping"))

# دستور ساده ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# اجرای ربات با توکن از Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("توکن ربات در Environment Variable پیدا نشد!")

bot.run(TOKEN)

