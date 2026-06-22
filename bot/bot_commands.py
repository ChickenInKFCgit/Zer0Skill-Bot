"""
Définit toutes les commandes du bot via la fonction load_commands.
"""

# Import des librairies et modules
import discord
from discord.ext import commands

import bot_console_dialog
import bot_auto_clone

def load_commands(bot:commands.bot.Bot):
    """
    Prend en paramètre un bot discord de discord.ext et lui définit les évènements et commandes rédigées pour Zer0 bot.
    Cette définition des commandes va être validée par l'event on_ready.
    """
 
    #___EVENTS
    @bot.event
    async def on_ready():
        """Lorsque le bot est prêt, syncronise les commandes commentées avec le bot."""
        nb_commandes_syncro = len(await bot.tree.sync())
        bot_console_dialog.confirm(f"{nb_commandes_syncro} commandes ont été chargées avec succès.")
        

    #___COMMANDES
    @bot.tree.command(name="repete", description="Une commande de test qui répète ton message")
    async def repete(interaction: discord.Interaction, a_repeter:str):
        await interaction.response.send_message(a_repeter)

    @bot.tree.command(name="services_introuvables", description="Indique tous les services qui n'ont pas pu être lancés.")
    async def services_introuvables(interaction: discord.Interaction):
        texte="Services qui n'ont pas pu être lancés : "
        for service in L_services_non_trouves:
            texte +=f"\n\t- {service}"
        await interaction.response.send_message(texte)

    @bot.tree.command(name="services_get", description="Pour chaque service introuvable, cloning de ceux-ci.")
    async def services_get(interaction: discord.Interaction):
        texte="Obtention des services non-trouvés :"
        for service in L_services_non_trouves:
            texte +=f"\n\t- {service} : " 
            texte+=bot_auto_clone.clone_service(service)
        await interaction.response.send_message(texte)

    @bot.tree.command(name="annoying_text", description="Permet de randomiser les lettres du texte fourni.")
    async def annoying_text(interaction: discord.Interaction, texte_a_randomiser:str):
        if SERVICE_AT not in L_services_non_trouves:
            resultat = codertexte(texte_a_randomiser)
        else:
            resultat = "Le service annoying text est introuvable."
        await interaction.response.send_message(resultat)
    
    

    
#constantes de noms services
SERVICE_AT = "annoying_text"

# Import des services, et si un service est introuvable, il est flag comme non trouvé.
L_services_non_trouves = []
try:    from services.annoying_text.annoying_text import codertexte
except ModuleNotFoundError: L_services_non_trouves.append(SERVICE_AT)