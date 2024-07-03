import os
import logging
import guilded
from guilded.ext import commands
import localpackages


# Initialize a global variable to store their instances.
JTV = None
DBH = None
Bot = None

# Making my life easier xd. yes I know this is bad.
LP = localpackages

def get_jtv_instance():
	global JTV
	if JTV is None:
		# Create the JTV instance only if it doesn't exist
		JTV = localpackages.json_to_var()

		JTV.os_environ_mode = False
		# If this ^^^^^^^^^^^^^^^^^ is true then it will ignore empty required datas from JTV.run()
		# and you can manually add your secret credentials here. Example (You can uncomment this):
		# JTV.Guilded_API = os.environ["Guilded_API"]
		# JTV.mysql_hostname = os.environ["mysql_hostname"]
		# JTV.mysql_username = os.environ["mysql_username"]
		# JTV.mysql_dbname = os.environ["mysql_dbname"]
		# JTV.mysql_password = os.environ["mysql_password"]


def get_dbh_instance():
	global DBH
	if DBH is None:
		# Create the DBH instance only if it doesn't exist
		DBH = localpackages.db_handler(
			JTV.mysql_hostname, JTV.mysql_username, JTV.mysql_password, JTV.mysql_dbname
		)
	return DBH

def get_bot_instance():
	global Bot
	if Bot is None:
		# Create the Bot instance only if it doesn't exist
		Bot = commands.Bot(
			command_prefix=JTV.Default_Prefix, owner_ids=JTV.Bot_Owners, case_insensitive=False, help_command=None
		)
		# Load cogs
		def load_cogs():
			# Get the path to the cogs directory
			cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")

			# Recursively load all Python files in the cogs directory and its subdirectories
			for root, dirs, files in os.walk(cogs_dir):
				for filename in files:
					if filename.endswith("Cog.py"):
						# Construct the full path to the cog (e.g., "cogs.Hidden.SecretFeatureCog")
						relative_path = os.path.relpath(os.path.join(root, filename), cogs_dir)
						cog_name = os.path.splitext(relative_path)[0].replace(os.sep, ".")
						cog_path = f"cogs.{cog_name}"
						Bot.load_extension(cog_path)
						print(f"Loaded cog: {cog_path}")
		load_cogs()
		print("Bot instance created.")
	return Bot

if __name__ == "__main__":
	get_jtv_instance()
	get_dbh_instance()

	Bot = get_bot_instance()

	print("Validating Database Credentials...")
	if DBH.test_connection():
		print("Credentials verified, running Cupcake_Lite bot.")

		Bot.run(JTV.Guilded_API)
	else:
		print("Cannot connect to database. Perhaps wrong database credentials or MySQL server not enabled?")
