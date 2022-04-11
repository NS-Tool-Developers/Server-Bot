import discord
from discord.ext import commands


class RCordBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='>')