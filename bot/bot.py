"""
Lance le bot discord. Est l'entry point de Zer0.
"""
import discord 
import os
from pathlib import Path
import bot_console_dialog
from discord.ext import commands 

#forcer l'exécution à la racine
racine_globale = Path(__file__).resolve().parent.parent
os.chdir(racine_globale)

#chargement du token
with open(file="token.secret", mode="r") as f: TOKEN = f.read()
bot_console_dialog.confirm("Token chargé avec succès.")

# Récupération des intentions du bot
import bot_intents as boti
intents = boti.get_intents()

#initialisation du bot 
client = commands.Bot(command_prefix='/', intents=intents) 

# Chargement des commandes et évènements du bot
import bot_commands as botc
botc.load_commands(client)

# Chargement du bot
bot_console_dialog.confirm("Client lancé.")
client.run(token=TOKEN)
bot_console_dialog.confirm("Client arrêté.")
