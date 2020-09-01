import discord
from redbot.core import commands
import aiohttp
from numbers import Number
from random import randint

BaseCog = getattr(commands, "Cog", object)


class Poggers(BaseCog):
    """Show something is Poggers!"""

    @commands.command()
    @commands.bot_has_permissions(embed_links=True, add_reactions=True)
    async def poggers(self, ctx, *, entry_number=None, arg):
        """Show something is poggers"""

        await ctx.send(arg)
