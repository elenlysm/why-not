import discord
import requests
import asyncio
import re
from deep_translator import GoogleTranslator

TOKEN = ""
USER_ID = ""

SCRIPT_URL = "https://gist.githubusercontent.com/MattIPv4/045239bc27b16b2bcf7a3a9a4648c08a/raw/2411e31293a35f3e565f61e7490a806d4720ea7e/bee%2520movie%2520script"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def split_sentences(text):
    return re.split(r'(?<=[.!?]) +', text)

def translate_text(text):
    parts = [text[i:i+4000] for i in range(0, len(text), 4000)]
    translated = []

    for part in parts:
        fr = GoogleTranslator(source='auto', target='fr').translate(part)
        translated.append(fr)

    return " ".join(translated)

@client.event
async def on_ready():
    print(f"Logado como {client.user}")

    user = await client.fetch_user(USER_ID)

    print("Baixando roteiro...")
    script = requests.get(SCRIPT_URL).text

    print("Traduzindo para francês...")
    script_fr = translate_text(script)

    print("Separando frases...")
    sentences = split_sentences(script_fr)

    for sentence in sentences:
        msg = f"🐝 {sentence.strip()}"

        async with user.typing():
            await asyncio.sleep(1.5)  

        await user.send(msg)

        await asyncio.sleep(2)  

    print("Bee Movie completo enviado 🐝🇫🇷")

client.run(TOKEN)