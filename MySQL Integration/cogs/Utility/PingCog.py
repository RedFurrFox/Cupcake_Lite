from guilded import Embed, Colour
from guilded.ext import commands

from ..properties import themes, aliases
TH = themes()
AL = aliases()


class PingCog(commands.Cog):
	def __init__(self, bot, DBH):
		self.bot = bot

	@commands.command(name="ping", aliases=AL.ping)
	async def ping(self, ctx):
		E = Embed(title="Ping command", description="Pinging...")
		E.colour = TH.White
		E.set_footer(text=f"Request from {ctx.author.name}", icon_url=ctx.author.profile_url)

		Message = await ctx.reply(embed=E, mention_author=False)

		guilded_server = round(self.bot.latency * 1000)

		E.description = f"**Pong!** at {guilded_server}ms."
		if 0 < guilded_server < 50:
			E.colour = TH.Green
		elif 50 < guilded_server < 150:
			E.colour = TH.Orange
		elif 150 < guilded_server < 250:
			E.colour = TH.Yellow
		else:
			E.colour = TH.Red

		await Message.edit(embed=E)


def setup(bot, DBH):
	bot.add_cog(PingCog(bot, DBH))
