from guilded import Embed, Colour
from guilded.ext import commands


class PingCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping", aliases=["p", "pi", "pin", "ping", "pings", "pinging", "pinged"])
	async def ping(self, ctx):
		E = Embed(title="Ping command", description="Pinging...")
		E.colour = Colour.from_rgb(153, 204, 255)
		E.set_footer(text=f"Request from {ctx.author.name}", icon_url=ctx.author.profile_url)
		Message = await ctx.reply(embed=E, mention_author=False)
		guilded_server = round(self.bot.latency * 1000)
		E.description = f"**Pong!** at {guilded_server}ms."
		E.colour = Colour.from_rgb(153, 255, 153) if guilded_server < 75 else Colour.from_rgb(255, 204, 153)
		await Message.edit(embed=E)


def setup(bot):
	bot.add_cog(PingCog(bot))
