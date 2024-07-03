from guilded.ext import commands


class OnDisconnectCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_disconnect(self):
		print("\n\n")
		print(f"Connection to {self.bot.user.name}({self.bot.user.id}) broke!")

def setup(bot):
	bot.add_cog(OnDisconnectCog(bot))
