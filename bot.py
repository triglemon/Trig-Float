"""
_.-=[ Trig-Float ]=-._
Personal helper bot to keep me "afloat".
"""
import discord
from discord.ext import commands
from modules.logger import log

# Startup cogs and bot defined
STARTUP_EXTENSIONS = ['cogs.calendar']
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready() -> None:
    """
    When the bot logs in, print the bot user's name and id and change his activity to playing a game.
    :return: None
    """
    print(f"Logged in as: {bot.user.name}, {bot.user.id}")
    game = discord.Game("Tryna Stay Chill")
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.command()
@commands.is_owner()
async def cog(command: str, extension_name: str) -> None:
    """
    If the user that triggered this is the owner of the bot, allow loading/unloading/reloading of specified cog.
    :param command: str
    :param extension_name: str
    :return: None
    """
    if command is "load":
        bot.load_extension(extension_name)
    elif command is "unload":
        bot.unload_extension(extension_name)
    elif command is "reload":
        bot.reload_extension(extension_name)

if __name__ == "__main__":
    # In the following order, this will try to:
    # 1. Set up a logger
    # 2. Load every extension listed in STARTUP_EXTENSIONS
    # 3. Read the token file
    # 4. Connect the bot as the respective token holder
    log()
    for extension in STARTUP_EXTENSIONS:
        bot.load_extension(extension)
    with open('token') as file:
        token = file.read()
    bot.run(token, bot=True, reconnect=True)
