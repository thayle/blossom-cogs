from redbot.core import commands

class Poggers(commands.Cog):
    """Poggers!"""

    @commands.command(pass_context=True)
    async def poggers(self, ctx):
        """Poggers!"""
        await ctx.send("https://cdn.discordapp.com/attachments/656930670374944829/750344767543574639/poggers.mp4")
        await Message.delete(ctx.message)
