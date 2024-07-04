import os
from guilded.ext import commands
from localpackages.json_to_var import json_to_var
from localpackages.db_handler import db_handler
from localpackages.others import clear_terminal
from localpackages.others import posix_type

class CupcakeBot:
    def __init__(self):
        self.JTV = None
        self.DBH = None
        self.Bot = None

    def get_jtv_instance(self):
        if self.JTV is None:
            self.JTV = json_to_var()
            # Set other JTV properties here
        return self.JTV

    def get_dbh_instance(self):
        if self.DBH is None:
            self.DBH = db_handler(
                self.JTV.mysql_hostname, self.JTV.mysql_username,
                self.JTV.mysql_password, self.JTV.mysql_dbname
            )
        return self.DBH

    def get_bot_instance(self):
        if self.Bot is None:
            self.Bot = commands.Bot(
                command_prefix=self.JTV.Default_Prefix,
                owner_ids=self.JTV.Bot_Owners,
                case_insensitive=False,
                help_command=None
            )
            self.load_cogs()
            print("Bot instance created.")
        return self.Bot

    def load_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        for root, dirs, files in os.walk(cogs_dir):
            for filename in files:
                if filename.endswith("Cog.py"):
                    relative_path = os.path.relpath(os.path.join(root, filename), cogs_dir)
                    cog_name = os.path.splitext(relative_path)[0].replace(os.sep, ".")
                    cog_path = f"cogs.{cog_name}"
                    try:
                        cog = __import__(cog_path, fromlist=["setup"])
                        if "Hidden" in relative_path:
                            cog.setup(self.Bot)
                        else:
                            cog.setup(self.Bot, self.DBH)  # Direct dependency injection
                        print(f"Loaded cog: {cog_path}")
                    except Exception as e:
                        print(f"Error loading cog {cog_path}: {e}")

if __name__ == "__main__":
    clear_terminal()

    bot = CupcakeBot()
    JTV = bot.get_jtv_instance()
    DBH = bot.get_dbh_instance()
    Bot = bot.get_bot_instance()

    print("Validating Database Credentials...")
    if DBH.test_connection():
        print("Credentials verified, running Cupcake_Lite bot.")
        Bot.run(JTV.Guilded_API)
    else:
        print("Cannot connect to the database. Perhaps wrong credentials or MySQL server not running?")
