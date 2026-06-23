"""
Définit toutes les commandes du bot via la fonction load_commands.
"""

# Import des librairies et modules
import discord
import sys
import os
from discord.ext import commands

import bot_console_dialog

def deplacer_chemin_courant():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

async def envoyer_message_en_morceaux(message:str, interaction: discord.Interaction): 
    """
    Découpe un message bien trop long en petits messages afin de permettre l'envoi.
    """ 
    taille_max = 1900 

    for morceau in [message[i:i + taille_max] for i in range(0, len(message), taille_max)]:
        await interaction.followup.send(morceau)

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
    @bot.tree.command(name="restart", description="Redémarre le bot.")
    async def restart(interaction: discord.Interaction):
        """
        Permet de rédémarrer le bot.
        """
        # laisse le temps au bot de réfléchir, mais on indique que ça ne doit pas durer longtemps
        await interaction.response.send_message("Okay le goat, je redémarre pour toi <3", ephemeral=True)

        # 1. On ferme proprement la connexion Discord
        await bot.close()
        
        from pathlib import Path
        import subprocess
        import os
        
        # 2. On calcule la racine absolue du projet
        racine_projet = Path(__file__).resolve().parent.parent
        
        python_env = str(racine_projet / ".env" / "Scripts" / "python.exe")
        script_bot = str(racine_projet / "bot" / "bot.py")
        
        # On relance le bot en forçant sont répertoire de travail
        subprocess.Popen([python_env, script_bot], cwd=str(racine_projet))
        
        # 4. On tue INSTANTANÉMENT le processus actuel pour laisser la place au nouveau
        os._exit(0)

    @bot.tree.command(name="services_introuvables", description="Indique tous les services qui n'ont pas pu être lancés.")
    async def services_introuvables(interaction: discord.Interaction):
        # laisse le temps au bot de réfléchir
        await interaction.response.defer(thinking=True) 
        
        if len(L_services_non_trouves) > 0:
            texte="Services qui n'ont pas pu être lancés : "
        else :
            texte="✅ Aucun service  introuvable."
        
        for service in L_services_non_trouves:
            texte +=f"\n- {service}"
        await interaction.followup.send(texte)

    @bot.tree.command(name="services_obtain", description="Charge chacun des services introuvables depuis github.")
    async def services_obtain(interaction: discord.Interaction):
        # laisse le temps au bot de réfléchir
        await interaction.response.defer(thinking=True) 

        if len(L_services_non_trouves) > 0:
            texte="Obtention des services non-trouvés :"
        else :
            texte="✅ Aucun service non trouvé, obtention des services annulée."
        deplacer_chemin_courant()
        for service in L_services_non_trouves:
            texte +=f"\n- {service} : " 
            texte+=bot_git.clone_service(service)

        await interaction.followup.send(texte)
    
    @bot.tree.command(name="services_update", description="Met à jour chacun des services à la version disponible sur github.")
    async def services_update(interaction: discord.Interaction):
        # laisse le temps au bot de réfléchir
        await interaction.response.defer(thinking=True) 
        
        if len(L_services) > 0:
            texte="Actualisation des services :"
        else:
            texte="❌ Aucun service, impossible d'en actualiser."
        deplacer_chemin_courant()
        for service in L_services:
            texte +=f"\n- {service} : " 
            if service not in L_services_non_trouves:
                texte+=bot_git.pull_service(service)
            else:
                texte+=f"Impossible de pull, service {service} introuvable"

        await interaction.followup.send(texte)

    @bot.tree.command(name="services_force", description="/service_obtain → /service_update → /restart")
    async def services_force(interaction: discord.Interaction):
        # laisse le temps au bot de réfléchir
        await interaction.response.defer(thinking=True) 

        await services_obtain(interaction)
        await services_update(interaction)
        await restart(interaction)

    @bot.tree.command(name="annoying_text", description="Permet de randomiser les lettres du texte fourni.")
    async def annoying_text(interaction: discord.Interaction, texte_a_randomiser:str):
        # laisse le temps au bot de réfléchir
        await interaction.response.defer(thinking=True) 

        if SERVICE_AT not in L_services_non_trouves:
            resultat = codertexte(texte_a_randomiser)
        else:
            resultat = SERVICE_INTROUVABLE
        await interaction.followup.send(resultat)

    @bot.tree.command(name="chest_hunt_simulator_idle_slayer", description="Permet de randomiser les lettres du texte fourni.")
    async def chest_hunt_simulator_idle_slayer(interaction: discord.Interaction, nombre_generations:int, nombre_simulations:int):
        # laisse le temps au bot de réfléchir
        await interaction.response.defer(thinking=True) 
        
        resultat = simuler(nombre_generations,nombre_simulations)
        await envoyer_message_en_morceaux(resultat,interaction)
    
    

#constantes messsages d'erreur
SERVICE_INTROUVABLE = "❌ Le service est introuvable, essayez /services_obtain et de relancer le bot."

#constantes de noms services
SERVICE_AT = "annoying_text"
SERVICE_CHSIS = "chest_hunt_simulator_idle_slayer"

# Chargement des repositories
deplacer_chemin_courant()
import bot_git as bot_git

# Import des services, et si un service est introuvable, il est flag comme non trouvé.
L_services = [SERVICE_AT,SERVICE_CHSIS]
L_services_non_trouves = []
try:    from services.annoying_text.annoyingtext import codertexte
except ModuleNotFoundError: L_services_non_trouves.append(SERVICE_AT)

try:    from services.chest_hunt_simulator_idle_slayer.simu import simuler
except ModuleNotFoundError: L_services_non_trouves.append(SERVICE_CHSIS)
