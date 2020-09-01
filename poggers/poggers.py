from redbot.core import commands

class Poggers(commands.Cog):
    """Poggers!"""

    @commands.command()
    async def poggers(self, ctx):
        """Just send poggers"""
        await ctx.send("https://cdn.discordapp.com/attachments/656930670374944829/750344767543574639/poggers.mp4")
        await bot.delete_message(ctx.message)
