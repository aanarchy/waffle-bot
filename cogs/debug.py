"""Debug commands."""
from discord.ext import commands

class Debug:
    """Debug class."""

    async def on_ready(self):
        """Prints when the cog is ready."""
        print("Debug is ready!")

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def logout(self, ctx):
        """Logs out of the bot user."""
        await self.bot.logout()

def setup(bot):
    """Sets up the cog."""
    bot.add_cog(Debug(bot))
