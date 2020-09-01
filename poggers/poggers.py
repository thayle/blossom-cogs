from redbot.core import commands

class Poggers(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def poggers(self, ctx, *):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("https://cdn.discordapp.com/attachments/656930670374944829/750344767543574639/poggers.mp4")
