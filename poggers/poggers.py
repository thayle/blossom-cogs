import discord
from redbot.core import commands, Config
from random import randint
import aiohttp
import logging

log = logging.getLogger("Poggers")  # Thanks to Sinbad for the example code for logging
log.setLevel(logging.DEBUG)

console = logging.StreamHandler()

if logging.getLogger("red").isEnabledFor(logging.DEBUG):
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.INFO)
log.addHandler(console)

BaseCog = getattr(commands, "Cog", object)


class Poggers(BaseCog):
    """Interact with people!"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=842364413)
        default_global = {
            "poggers": [
                "https://cdn.discordapp.com/attachments/656930670374944829/750344767543574639/poggers.mp4"
            ]
        }
        self.config.register_global(**default_global)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poggers(self, ctx, *, user: discord.Member):
        """Poggers!"""

        author = ctx.message.author
        images = await self.config.poggers()

        nekos = await self.fetch_poggers_life(ctx, "hug")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    async def fetch_poggers_life(self, ctx, rp_action):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://cdn.discordapp.com/attachments/656930670374944829/750344767543574639/poggers.mp4") as resp:
                try:
                    content = await resp.json(content_type=None)
                except (ValueError, aiohttp.ContentTypeError) as ex:
                    log.debug("Pruned by exception, error below:")
                    log.debug(ex)
                    return []

        if content["data"]["status"]["code"] == 200:
            return content["data"]["response"]["urls"]

