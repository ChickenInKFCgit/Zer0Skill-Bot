import discord



class Bot:
    def __init__(self,TOKEN:str):
        self.token = TOKEN

        intents = self.__setintents()
        self.client = discord.Client(intents=intents)
        

    def start(self):
        self.client.run(token=self.token)

    def __setintents(self):
        discord.Intents.default()


def main():
    with open(file="token.secret", mode="r") as f:
        TOKEN=f.read()
        Zer0Skill = Bot(TOKEN)
        Zer0Skill.start()

main()