import logging


def log() -> None:
    """
    This function sets up a logger that writes error and debug information to a file named 'discord.log'.
    :return: None
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(handler)
