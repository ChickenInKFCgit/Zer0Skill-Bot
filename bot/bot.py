"""
Lance le bot discord. Est l'entry point de Zer0.
"""
import bot_commands as botc
import bot_intents as boti
from discord.ext import commands


#chargement du token
with open(file="token.secret", mode="r") as f:
    TOKEN = f.read()


# Récupération du bot
#initialisation du bot et récupération de ses intentions
intents = boti.get_intents()
client = commands.Bot(command_prefix='/', intents=intents) 

botc.load_commands(client)

# Chargement du bot
client.run(token=TOKEN)
