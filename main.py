import discord
import random
import os
from myserver import server_on


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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

server_on()

client.run("MTM2Mzk2NDYxNDExMDQ4MjUzMg.GRwSL-.vVAUxWnqg52vUHQtJfwNUwqaDJrZ3-sYfCQZa4")