"""
Définit toutes les commandes du bot et l'initialise.
"""
import discord

import bot_intents as boti
from discord.ext import commands

#initialisation du bot et récupération de ses intentions
intents = boti.get_intents()
bot = commands.Bot(command_prefix='/', intents=intents) # Note : self.intents a été corrigé en intents ici pour que le code puisse s'exécuter

#getter du bot
get_bot = lambda : bot

#Commandes

@bot.tree.command(name="test", description="Une commande de test qui répète ton message")
async def test(interaction: discord.Interaction, arg:str):
    await interaction.response.send_message(arg)


@bot.event
async def on_ready():
    """
    Tente de syncroniser les descriptions des commandes avec les commandes, et affiche une erreur si échec.
    Cette fonction s'éxecute automatiquement lorsque le bot se connecte.
    """
    try:
        await bot.tree.sync()
        print("syncronisation réalisée")
    except Exception as e:
        print("Erreur lors de la syncronisation : "+e)
    
