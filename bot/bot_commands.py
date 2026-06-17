"""
Définit toutes les commandes du bot et l'initialise.
"""
import bot_intents as boti
from discord.ext import commands

#initialisation du bot et récupération de ses intentions
intents = boti.get_intents()
bot = commands.Bot(command_prefix='/', intents=intents) # Note : self.intents a été corrigé en intents ici pour que le code puisse s'exécuter

#getter du bot
get_bot = lambda : bot

#Commandes

@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)
