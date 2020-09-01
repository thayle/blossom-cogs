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
    async def poggers(self, ctx, *, entry_number=None):
        """Show something is poggers"""

        # Build Embed
        embed = discord.Embed()
        embed.url = "https://cdn.discordapp.com/attachments/656930670374944829/750344767543574639/poggers.mp4"
        embed.description = f"**{author.mention} thinks something is Poggers!**"
        await ctx.send(embed=embed)
