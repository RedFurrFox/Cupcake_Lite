import logging
import guilded
from guilded.ext import commands

import localpackages


localpackages.clear_terminal()

JTV = localpackages.json_to_var()
JTV.run()

DBH = localpackages.db_handler(
	JTV.mysql_hostname, JTV.mysql_username, JTV.mysql_password, JTV.mysql_dbname
)

if not DBH.test_connection():
	print("Database not connected, perhaps wrong credentials or database server not running?")
	exit("Database = not connected")

Bot = commands.Bot(
	command_prefix=JTV.Default_Prefix, owner_id=JTV.Bot_Owner, case_insensitive=False, help_command=None
)

