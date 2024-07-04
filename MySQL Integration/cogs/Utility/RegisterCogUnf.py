from guilded import Embed, Colour
from guilded.ext import commands
from main import DBH

from ..properties import themes, aliases

TH = themes()
AL = aliases()


class RegisterCog(commands.Cog):
	def __init__(self, bot):
		self.DBH = DBH
		self.bot = bot

	async def check_is_owner(self, SID, UID):
		Server = await self.bot.getch_server(SID)
		Owner = Server.owner_id
		return True if (Owner == UID) else False

	async def check_is_server_admin(self, SID, UID):
		search_condition = "ServerID = %s AND PrivilegeRoles_Admins LIKE %s"
		params = (SID, f"%{UID}%")
		return DBH.search_entry(table_name="gserver_configs", search_condition=search_condition, params=params)

	async def check_is_server_mod(self, SID, UID):
		search_condition = "ServerID = %s AND PrivilegeRoles_Mods LIKE %s"
		params = (SID, f"%{UID}%")
		return DBH.search_entry(table_name="gserver_configs", search_condition=search_condition, params=params)

	async def check_authority(self, SID, UID):
		return True if (await self.check_is_owner(SID, UID) or await self.check_is_server_admin(SID, UID) or await self.check_is_server_mod(SID, UID)) else False

	@commands.command(name="register", aliases=AL.ping)
	async def register(self, ctx):
		E = Embed(title="Register command ")
		E.set_footer(text=f"Request from {ctx.author.name}", icon_url=ctx.author.profile_url)

		if not await self.check_authority(ctx.server.id, ctx.author.id):
			E.title += "/ Authority error page"
			E.description = "You lack authority to view/use this usage/documentation command, you must meet one or more of these criteria:"
			E.add_field(
				name="1.) Server owner",
				value="The person who owns this server",
			)

			E.colour = TH.Orange

			await ctx.reply(embed=E, mention_author=False)

		# self.DBH.

		# await Message.edit(embed=E)


def setup(bot):
	bot.add_cog(RegisterCog(bot))
