from guilded import Colour

class themes:
	def __init__(self):
		self.Red = Colour.from_rgb(255, 150, 150)
		self.Orange = Colour.from_rgb(255, 190, 130)
		self.Yellow = Colour.from_rgb(255, 240, 150)
		self.Green = Colour.from_rgb(170, 255, 170)
		self.Blue = Colour.from_rgb(150, 180, 255)
		self.White = Colour.from_rgb(255, 255, 255)

class aliases:
	def __init__(self):
		# Hidden
		# ------

		# Moderation
		self.mods = ["m", "mo", "mod", "mods", "moderation", "moderations"]
		self.utils = ["u", "ut", "uti", "util", "utils", "utility", "utilities"]
		self.kick = ["k", "ki", "kic", "kick", "kicks", "kicking", "kicked"]
		self.ban = ["b", "ba", "ban", "bans", "banning", "banned"]
		self.unban = ["ub", "unb", "unba", "unban", "unbans", "unbanning", "unbanned"]

		# Utility
		self.help = ["h", "help", "docs", "huh", "what"]
		self.info = ["i", "in", "info", "infos", "information", "informations"]
		self.ping = ["p", "pi", "pin", "ping", "pings", "pinging", "pinged"]
