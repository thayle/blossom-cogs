from redbot.core import commands

class Hiatus(commands.Cog):
    """ITS REAL DAMN IT"""

    @commands.command(pass_context=True)
    async def hiatus(self, ctx):
        """ITS REAL DAMN IT"""
        await ctx.send("As Riley's faithful companion it is my job to ensure you all know they are on a **REAL** hiatus. There are many doubters but do not trust them, only the word of Blossom is true all others are fake news with an agenda to undermine our great state. Normal activity will resume Tuesday afternoon. Thank you for your patience and fuck sadik for doubting.")
        await ctx.message.delete()
