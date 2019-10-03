from discord.ext import commands


class Calendar(commands.Cog):
    def __init__(self, bot) -> None:
        """

        :param bot: discord.Bot
        :return: None
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, member):
        print('yeet')

    @commands.command()
    async def yeet(self):
        pass


def setup(bot):
    bot.add_cog(Calendar(bot))
