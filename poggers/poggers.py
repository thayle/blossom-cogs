from redbot.core import commands

class Poggers(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def poggers(self, ctx, *):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")
