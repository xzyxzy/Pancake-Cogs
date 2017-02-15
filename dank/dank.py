from discord.ext import commands


class Dank:
    """Dank memes, yo."""

    def __init__(self, bot):
        self.bot = bot
        self.base = "data/dank/"

    @commands.command(pass_context=True)
    async def dickbutt(self, ctx):
        """Dickbutt."""
        await self.bot.send_file(ctx.message.channel,
                                 "{}dickbutt.png".format(self.base))

    @commands.command(pass_context=True)
    async def barbaric(self, ctx):
        """Absolutely."""
        await self.bot.send_file(ctx.message.channel,
                                 "{}barbaric.jpg".format(self.base))

    @commands.command(pass_context=True)
    async def pathetic(self, ctx):
        """Pathetic."""
        await self.bot.send_file(ctx.message.channel,
                                 "{}pathetic.png".format(self.base))

    @commands.command(pass_context=True)
    async def ts(self, ctx):
        """Thinking suicide."""
        await self.bot.send_file(ctx.message.channel,
                                 "{}thinkingsuicide.png".format(self.base)) 

def setup(bot):
    bot.add_cog(Dank(bot))
