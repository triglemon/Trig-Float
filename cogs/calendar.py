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
from datetime import datetime as dt



class Calendar(commands.Cog):
    def __init__(self, bot) -> None:
        """
        :param bot: discord.Bot
        :return: None
        """
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx) -> None:
        """
        This listener function should ONLY take in messages under the following format:
        {message} {time}
        For example:
        Everything we need that is not food or love is here in the tabloid racks. 2019/10/3/4/39
        :param ctx: commands context
        :return: None
        """
        if str(ctx.channel.category) == 'Calendar':

            cal_entry = ctx.content.rsplit(' ', 1)
            # We're splitting 2019/9/3 into an actual time
            date = dt(*[int(unit) for unit in cal_entry[1].split('/')])
            if date.hour:
                time = date.strftime('%H:%M, ')
            else:
                time = ''
            message = f'{ctx.channel}: {cal_entry[0]} — {time}{date.strftime("%A, %b %d, %Y")}'
            print(message)


def setup(bot):
    bot.add_cog(Calendar(bot))
