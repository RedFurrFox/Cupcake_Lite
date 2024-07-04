from guilded import Embed, Colour
from guilded.ext import commands

from ..properties import themes, aliases
TH = themes()
AL = aliases()


class InfoCog(commands.Cog):
	def __init__(self, bot, DBH):
		self.bot = bot

	@commands.command(name="info", aliases=AL.info)
	async def info(self, ctx):
		E = Embed(title="Info command", description="This bot is running on **[Cupcake_Lite](https://github.com/RedFurrFox/Cupcake_Lite)**\n\nCreated and maintained w/ <3 by [RedFurrFox](https://github.com/RedFurrFox/)")
		E.colour = TH.White
		E.set_footer(text=f"Request from {ctx.author.name}", icon_url=ctx.author.profile_url)
		await ctx.reply(embed=E, mention_author=False)


def setup(bot, DBH):
	bot.add_cog(InfoCog(bot, DBH))
