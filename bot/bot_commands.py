"""
Définit toutes les commandes du bot via la fonction load_commands.
"""
import discord
from discord.ext import commands
import bot_console_dialog

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

    @bot.tree.command(name="annoying_text", description="Permet de randomiser les lettres du texte fourni.")
    async def annoying_text(interaction: discord.Interaction, texte_a_randomiser:str):
        await interaction.response.send_message(texte_a_randomiser)

    
