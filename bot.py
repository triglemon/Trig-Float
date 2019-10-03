"""
Trig-Float. Personal helper bot to keep me "afloat".
"""
import discord
from discord.ext import commands
from modules.logger import log

# Startup cogs and bot defined
STARTUP_EXTENSIONS = ['cogs.']
bot = commands.Bot(command_prefix='&')


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
async def load(ctx: commands.Context, extension_name: str):
    """
    If the user that triggered this is the owner of the bot, allow loading of specified cog.
    :param ctx: command context
    :param extension_name: str
    :return: None
    """
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as error:
        await ctx.send(f"```py\n{type(error).__name__}: {str(error)}\n```")
        return
    await ctx.send(f"{extension_name} loaded.")


@bot.command()
@commands.is_owner()
async def unload(ctx: commands.Context, extension_name: str):
    """
    If the user that triggered this is the owner of the bot, allow unloading of specified cog.
    :param ctx: command context
    :param extension_name: str
    :return: None
    """
    bot.unload_extension(extension_name)
    await ctx.send(f"{extension_name} unloaded.")

if __name__ == "__main__":
    # In the following order, this will try to:
    # 1. Set up a logger
    # 2. Load every extension listed in STARTUP_EXTENSIONS
    # 3. Read the token file
    # 4. Connect the bot as the respective token holder
    log()
    for extension in STARTUP_EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = f"{type(e).__name__}: {e}"
            print(f'Failed to load extension {extension}\n{exc}')
    with open('token') as file:
        token = file.read()
    bot.run(token, bot=True, reconnect=True)