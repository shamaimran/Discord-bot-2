import discord
from discord.ext import commands
import requests
import os
from flask import Flask
from threading import Thread

# --- Vercel ke liye Flask Server (Bot ko zinda rakhne ke liye) ---
app = Flask('')

@app.route('/')
def home():
    return "Ibrahim, aapka bot online hai!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# --- Discord Bot Code ---
TOKEN = 'YOUR_BOT_TOKEN_HERE'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

AD_LINK = "https://shrinkme.io/xxxx" # Apna naya link yahan dalein

@bot.event
async def on_ready():
    print(f'Ibrahim, Bot Vercel par tayyar hai!')

@bot.command()
async def getcode(ctx):
    await ctx.send(f"Ibrahim, code hasil karne ke liye link open karein:\n{AD_LINK}")

@bot.command()
async def verify(ctx, code: str):
    url = "https://ibrahim654758.pythonanywhere.com/static/codes.txt"
    try:
        r = requests.get(url, timeout=5)
        server_code = r.text.strip().upper()
        
        if code.upper() == server_code:
            await ctx.send(f"✅ Code Sahi hai! Welcome Ibrahim.")
        else:
            await ctx.send(f"❌ Galat code! Ibrahim, website par ja kar naya code dekhein.")
    except Exception as e:
        await ctx.send("⚠️ Website (PythonAnywhere) se rabta nahi ho raha.")

# Flask aur Bot dono ko saath chalana
if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)