from guilded.ext import commands


class OnReadyCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("\n\n")
		print(f"Connected to {self.bot.user.name}({self.bot.user.id})!")

def setup(bot):
	bot.add_cog(OnReadyCog(bot))
