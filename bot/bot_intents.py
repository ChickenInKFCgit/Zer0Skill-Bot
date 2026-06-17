"""
Configure les intentions du bot.
Cela permet de décrire à discord quelles fonctionnalités il utilise et donc quelles permissions demander.
"""

import discord

#intialisation des intentions du bot
intents = discord.Intents.default()
intents.message_content = True

#getter intents
get_intents = lambda: intents