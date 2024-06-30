from guilded import Embed, Colour
from guilded.ext import commands


class HelpCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.prefix = self.bot.command_prefix

		self.help_alias = ["h", "help", "docs", "huh", "what"]
		self.mods_alias = ["m", "mo", "mod", "mods", "moderation", "moderations"]
		self.utils_alias = ["u", "ut", "uti", "util", "utils", "utility", "utilities"]
		self.kick_alias = ["k", "ki", "kic", "kick", "kicks", "kicking", "kicked"]
		self.ban_alias = ["b", "ba", "ban", "bans", "banning", "banned"]
		self.unban_alias = ["ub", "unb", "unba", "unban", "unbans", "unbanning", "unbanned"]

	def check_is_owner(self, SID, UID):

		return True

	def check_is_server_admin(self, SID, UID):
		return True

	def check_is_server_mod(self, SID, UID):
		return True

	def check_authority(self, SID, UID):
		return True if (self.check_is_owner(SID, UID) or self.check_is_server_admin(SID, UID) or self.check_is_server_mod(SID, UID)) else False

	@staticmethod
	def alias_presentation(target:list):
		if len(target) == 1:
			AP = f"`{target}`"
		else:
			AP = ", ".join(f"`{i}`" for i in target)
			AP = AP.rsplit(", ", 1)
			if len(target) == 2:
				AP = f"{AP[0]} and {AP[1]}"
			else:
				AP = f"{AP[0]}, and {AP[1]}"
		return AP

	@commands.command(name="help", aliases=["h", "help", "docs", "huh", "what"])
	async def help(self, ctx, arg1:str=None, arg2:str=None, arg3:str=None, arg4:str=None):
		E = Embed(title="Help ")
		E.set_footer(text=f"Request from {ctx.author.name}", icon_url=ctx.author.profile_url)
		E.colour = Colour.from_rgb(255, 204, 204)

		def error():
			E.title += "/ Error page"
			E.description = f"Command `{ctx.message.content}` invalid or not found.\nCheck your help query usage and try again.\n\nFor more information, type **`{self.bot.command_prefix}help`** or **`{self.bot.command_prefix}h`** for bot command lists and their usage."
			E.colour = Colour.from_rgb(255, 153, 153)

		# Page 1  ->  %prefix%help
		if arg1 is None:
			E.title += "Page"
			E.description = "Here are my command categories:\n"
			E.add_field(
				name="Mods",
				value="Server moderation related command lists.",

			)
			E.add_field(
				name="Utils",
				value="Server utility related command lists.",

			)
			E.add_field(
				name="\n\nShorten aliases of Help command:",
				value=self.alias_presentation(self.help_alias),
				inline=False
			)

		# Page 2  ->  %prefix%help %arg1%
		elif arg1 is not None and arg2 is None:
			if arg1.lower() in self.mods_alias:
				E.title += "/ Mods page"
				E.description = "Here are my moderation commands:\n"
				E.add_field(
					name="Kick",
					value="Kick a user from this server."
				)
				E.add_field(
					name="Ban",
					value="Ban a user from this server.",
				)
				E.add_field(
					name="Unban",
					value="Unban a user from this server."
				)
				E.add_field(
					name="Mute",
					value="Mute a user from this server."
				)
				E.add_field(
					name="Lockdown",
					value="Lockdown Switches."
				)
				E.add_field(
					name="RoleRegister",
					value="Register a role as an admin, mod, and mute role."
				)
				E.add_field(
					name="Module",
					value="Moderation modules for this server.",
				)
				E.add_field(
					name="\n\nShorten aliases of Mods option",
					value=self.alias_presentation(self.mods_alias),
					inline=False
				)
			elif arg1.lower() in self.utils_alias:
				E.title += "/ Utils page"
				E.description = "Here are my utility commands:\n"
				E.add_field(
					name="Help",
					value="Show this bot commands page."
				)
				E.add_field(
					name="Ping",
					value="Calculate server/s response time."
				)
				E.add_field(
					name="Info",
					value="Show information about this bot."
				)
				E.add_field(
					name="SourceCode",
					value="Show the whole source code for this bot."
				)
				E.add_field(
					name="\n\nShorten aliases of Utils option",
					value=self.alias_presentation(self.utils_alias),
					inline=False
				)

			# Command not found
			else:
				# print(1)
				error()

		# Page 3  ->  %prefix%help %arg1% %arg2%
		elif arg2 is not None and arg3 is None:

			if arg1.lower() in self.mods_alias:
				E.title += "/ Mods "

				if arg2 in self.kick_alias:
					E.title += "/ Kick command"
					E.description = "Kick a user using @ or user id"
					E.add_field(
						name="Requirements before using:",
						value=" - User/s must be an owner or it has an admin role or a mod role.\n"
						      " - The target member must be on this server.",
						inline=False
					)
					E.add_field(
						name="Command Usage:",
						value=f"```git\n"
						      f"- By Mentioning: {self.prefix}kick @<Member>\n"
						      f"  Example: {self.prefix}kick @TestAccount\n\n"
						      f"- By User ID: {self.prefix}kick <UserID>\n"
						      f"  Example: {self.prefix}kick dzDkaKVA```",
						inline=False
					)
					E.add_field(
						name="Shorten aliases for Kick command:",
						value=self.alias_presentation(self.kick_alias),
						inline=False
					)

				elif arg2.lower() in self.ban_alias:
					E.title += "/ Ban command"
					E.description = "Ban a user using @ or user id"
					E.add_field(
						name="Requirements before using:",
						value=" - User/s must be an owner or it has an admin role or a mod role.\n"
						      " - The target member must be on this server.",
						inline=False
					)
					E.add_field(
						name="Command Usage:",
						value=f"```git\n"
						      f"- By Mentioning: {self.prefix}ban @<Member>\n"
						      f"  Example: {self.prefix}ban @TestAccount\n\n"
						      f"- By User ID: {self.prefix}ban <UserID>\n"
						      f"  Example: {self.prefix}ban dzDkaKVA```",
						inline=False
					)
					E.add_field(
						name="Shorten aliases for Ban command:",
						value=self.alias_presentation(self.ban_alias),
						inline=False
					)

				elif arg2.lower() in self.unban_alias:
					E.title += "/ Unban command"
					E.description = "Unban a user using @ or user id"
					E.add_field(
						name="Requirements before using:",
						value=" - User/s must be an owner or it has an admin role or a mod role.\n"
						      " - The target member must be on this server.",
						inline=False
					)
					E.add_field(
						name="Command Usage:",
						value=f"```git\n"
						      f"- By Mentioning: {self.prefix}unban @<Member>\n"
						      f"  Example: {self.prefix}unban @TestAccount\n\n"
						      f"- By User ID: {self.prefix}unban <UserID>\n"
						      f"  Example: {self.prefix}unban dzDkaKVA```",
						inline=False
					)
					E.add_field(
						name="Shorten aliases for Ban command:",
						value=self.alias_presentation(self.unban_alias),
						inline=False
					)

				# Command not found
				else:
					# print(2)
					error()

			# Command not found
			else:
				# print(3)
				error()

		# Command not found
		else:
			# print(4)
			error()

		await ctx.reply(embed=E, mention_author=False)


def setup(bot):
	bot.add_cog(HelpCog(bot))
