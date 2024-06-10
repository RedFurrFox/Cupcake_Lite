import os
import json

from . import others


class json_to_var:
	def __init__(self):
		self.posix = others.posix_type()
		self.Guilded_API = ""
		self.Default_Prefix = ""
		self.Bot_Owner = None
		self.Bot_Error_Log_CID = None
		self.mysql_hostname = ""
		self.mysql_username = ""
		self.mysql_password = None
		self.mysql_dbname = ""

	def run(self):
		print("on json_to_var.py file")

		if self.validate_configs_file() is False:
			self.rebuild_configs_file()
			print("Please reconfig the configs.json file first! and run the program again.")
			exit("configs.json = new")
		else:
			self.get_configs_content()

	def validate_configs_file(self):
		print("Checking if configs.json file exists...")
		if os.path.isfile(path=rf".{self.posix}configs.json"):
			print("File found!")
			return True
		else:
			print("File not found!")
			return False

	def rebuild_configs_file(self):
		print("Creating new configs.json file")
		configs_format = ("{\n"
		                  "	\"Guilded_API\": \"\",\n"
		                  "	\"Default_Prefix\": \"\",\n"
		                  "	\"Bot_Owner\": null,\n"
		                  "	\"Bot_Error_Log_CID\": null,\n"
		                  "	\n"
		                  "	\"MySQL_Connection\": {\n"
		                  "		\"hostname\": \"\",\n"
		                  "		\"username\": \"\",\n"
		                  "		\"password\": \"\",\n"
		                  "		\"dbname\": \"\"\n"
		                  "	}\n"
		                  "}\n")
		with open(rf".{self.posix}configs.json", "w") as file:
			file.write(configs_format)
			file.close()
		print("configs.json created!")

	def get_configs_content(self):
		print("Opening the configs.json file")
		with open(rf".{self.posix}configs.json") as raw_content:
			content = json.load(raw_content)

		try:
			print("Grabbing the value for Guilded_API")
			self.Guilded_API = content["Guilded_API"]
			print("Checking the value...")
			if self.Guilded_API is None or self.Guilded_API.replace(" ", "") == "":
				print("Guilded_API cannot be empty!")
				exit("configs.json -> Guilded_API = null")

			print("Grabbing the value for Default_Prefix")
			self.Default_Prefix = content["Default_Prefix"]
			print("Checking the value...")
			if self.Default_Prefix is None or self.Default_Prefix.replace(" ", "") == "":
				print("Default_Prefix empty! using cl. instead.")
				self.Default_Prefix = "cl."

			print("Grabbing the value for Bot_Owner")
			self.Bot_Owner = content["Bot_Owner"]

			print("Grabbing the value for Bot_Error_Log_CID")
			self.Bot_Error_Log_CID = content["Bot_Error_Log_CID"]

			print("Grabbing the value for MySQL > hostname")
			self.mysql_hostname = content["MySQL_Connection"]["hostname"]

			print("Grabbing the value for MySQL > username")
			self.mysql_username = content["MySQL_Connection"]["username"]

			print("Grabbing the value for MySQL > password")
			self.mysql_password = content["MySQL_Connection"]["password"]

			print("Grabbing the value for MySQL > dbname")
			self.mysql_dbname = content["MySQL_Connection"]["dbname"]

			print("Checking the MySQL connection values")
			if self.mysql_hostname.replace(" ", "") == "" or self.mysql_username.replace(" ", "") == "" or self.mysql_hostname.replace(" ", "") == "":
				print("MySQL connection values cannot be empty!")
				exit("configs.json -> MySQL_Connection... = has null")

			print("Content grabbing complete!")
		except json.JSONDecodeError as error:
			print(
				f"\nSomething is wrong with the config file. If this error persists after making some changes, try deleting the configs file and run this again.\n\n{error}")
		finally:
			print("Closing configs.json file")
			raw_content.close()
