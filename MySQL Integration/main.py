import localpackages

localpackages.clear_terminal()

JTV = localpackages.json_to_var()
JTV.run()

DBH = localpackages.db_handler(
	JTV.mysql_hostname, JTV.mysql_username, JTV.mysql_password, JTV.mysql_dbname
)

print(DBH.test_connection())
