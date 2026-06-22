"""
Définit toutes les commandes du bot et l'initialise.
"""
import discord





#Commandes

def load_commands(bot):
    @bot.tree.command(name="repete", description="Une commande de test qui répète ton message")
    async def repete(interaction: discord.Interaction, arg:str):
        await interaction.response.send_message(arg)


    @bot.event
    async def on_ready():
        await bot.tree.sync()

    
