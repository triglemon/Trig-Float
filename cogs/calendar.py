"""
_.-=[ Calendar Cog ]=-._
This should allow me to send a calendar entry to any channel in the calendar category (courses, general, social, etc)
and will post it to the feed channel at the top of the server. The time argument will decide the order of entries.
The format should go like this:

# CSC148
"Do assignment 1"

"""
from discord.ext import commands
from typing import List


class Calendar(commands.Cog):
    def __init__(self, bot) -> None:
        """
        :param bot: discord.Bot
        :return: None
        """
        self.bot = bot

    @commands.command
    async def log(self, ctx, *message: List[str]) -> None:
        """
        :param ctx: commands context
        :param message: List[str]
        :return: None
        """
        for x in message:
            print(x)


def setup(bot):
    bot.add_cog(Calendar(bot))
