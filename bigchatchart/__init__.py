from .bigchatchart import BigChatChart


def setup(bot):
    bot.add_cog(BigChatChart(bot))
