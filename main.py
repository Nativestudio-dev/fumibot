import discord
import random
from flask import Flask
import threading
import os


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

app = Flask(__name__)

@app.route('/')
def index():
    return "💖 Bot is running on Render!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))  # Render จะกำหนด PORT ให้ใน env
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask).start()

ALLOWED_CHANNEL_ID = 1363995505843109948  # ใส่ Channel ID ที่อนุญาต

IMAGE_FOLDER = "imges"  # โฟลเดอร์ที่เก็บภาพ (อยู่ในโฟลเดอร์เดียวกับไฟล์ .py)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != ALLOWED_CHANNEL_ID:
        return

    if message.content.startswith('!love'):
        image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not image_files:
            await message.channel.send("ไม่มีภาพในโฟลเดอร์เลยน้าา")
            return

        selected_image = random.choice(image_files)
        image_path = os.path.join(IMAGE_FOLDER, selected_image)

        await message.channel.send(file=discord.File(image_path), content="ส่งความรักให้คุณ 💖")

client.run(os.getenv('TOKEN'))
