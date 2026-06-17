"""
Lance le bot discord
"""
import bot_commands as botc


#chargement du token
with open(file="token.secret", mode="r") as f:
    TOKEN = f.read()


# Récupération du bot
client = botc.get_bot()

# Chargement du bot
client.run(token=TOKEN)
