import mysql.connector


class db_handler:
	def __init__(self, host, user, password, database):
		self.conn = None
		self.curs = None
		try:
			self.conn = mysql.connector.connect(
				host=host, user=user, password=password, database=database
			)
			self.curs = self.conn.cursor()
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")

	def __del__(self):
		# Automatically closes the created instances of self.conn if unused
		if self.conn:
			self.conn.close()

	def test_connection(self):
		"""
		Test if the connection to the database and return its value
		:return:
		"""

		try:
			return self.conn.is_connected() if self.conn else False
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			return False

	def add_entry(self, table_name:str, columns:list, values:list):
		"""
		Used to add an entry on a selected table.\n

		**Example:**\n
		db = db_handler('localhost', 'root', 'password', 'my_database')\n
		columns = ['column1', 'column2', 'column3']\n
		values = ['value1', 'value2', 'value3']\n
		db.add_entry('my_table', columns, values)

		:param table_name:
		:param columns:
		:param values:
		:return:
		"""

		try:
			# Prepare the SQL query for inserting data into the table
			query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(values))})"
			# Execute the query
			self.curs.execute(query, values)
			# Commit the transaction
			self.conn.commit()
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			# Rollback the transaction in case of error
			self.conn.rollback()

	def del_entry(self, table_name:str, condition:str):
		"""
		Used to delete an entry on a selected table.\n

		**Example:**\n
		db = db_handler('localhost', 'root', 'password', 'my_database')\n
		condition = "column1 = 'value1'"\n
		db.del_entry('my_table', condition)

		:param table_name:
		:param condition:
		:return:
		"""

		try:
			# Prepare the SQL query for deleting data from the table
			query = f"DELETE FROM {table_name} WHERE {condition}"
			# Execute the query
			self.curs.execute(query)
			# Commit the transaction
			self.conn.commit()
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			# Rollback the transaction in case of error
			self.conn.rollback()

	def mod_entry(self, table_name:str, updates:dict, condition:str):
		"""
		Used to modify an entry on a selected table.\n

		**Example:**\n
		db = db_handler('localhost', 'root', 'password', 'my_database')\n
		updates = {'column2': 'new_value2', 'column3': 'new_value3'}\n
		condition = "column1 = 'value1'"\n
		db.mod_entry('my_table', updates, condition)

		:param table_name:
		:param updates:
		:param condition:
		:return:
		"""

		try:
			# Prepare the SQL query for updating data in the table
			update_query = ', '.join([f"{column} = %s" for column in updates.keys()])
			query = f"UPDATE {table_name} SET {update_query} WHERE {condition}"
			# Execute the query
			self.curs.execute(query, list(updates.values()))
			# Commit the transaction
			self.conn.commit()
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			# Rollback the transaction in case of error
			self.conn.rollback()

	def get_entries(self, query: str, params=None):
		"""
		Used to fetch entries from the database based on the provided query and parameters.\n

		**Example:**\n
		db = db_handler('localhost', 'root', 'password', 'my_database')\n
		query = "SELECT * FROM my_table WHERE column1 = %s"\n
		params = ('value1',)\n
		entries = db.get_entries(query, params)
		for entry in entries:
			print(entry)

		:param query: The SQL query to execute.
		:param params: The parameters to pass to the SQL query.
		:return: A list of tuples containing the fetched records.
		"""

		try:
			# Execute the query
			self.curs.execute(query, params or ())
			# Fetch all the records
			entries = self.curs.fetchall()
			return entries
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			return []

	def search_entry(self, table_name: str, search_condition: str, params=None):
		"""
		Searches for an entry in the database based on the provided condition.\n

		**Example:**\n
		db = db_handler('localhost', 'root', 'password', 'my_database')\n
		search_condition = "column1 = %s AND column2 = %s"\n
		params = ('value1', 'value2')\n
		found = db.search_entry('my_table', search_condition, params)\n
		print(f'Entry found: {found}')

		:param table_name: The name of the table to search in.
		:param search_condition: The condition to match against records in the table.
		:param params: The parameters to pass to the SQL query.
		:return: True if an entry is found, False otherwise.
		"""

		try:
			# Prepare the SQL query for searching data in the table
			query = f"SELECT 1 FROM {table_name} WHERE {search_condition} LIMIT 1"
			# Execute the query with params
			self.curs.execute(query, params or ())
			# Fetch one record
			entry = self.curs.fetchone()
			return bool(entry)
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			return False

	def search_entry_content(self, table_name: str, search_condition: str, params=None):
		"""
		Searches for an entry in the database based on the provided condition and returns column data.

		:param table_name: The name of the table to search in.
		:param search_condition: The condition to match against records in the table.
		:param params: The parameters to pass to the SQL query.
		:return: Column data if an entry is found, None otherwise.
		"""

		try:
			# Prepare the SQL query for selecting data from the table
			query = f"SELECT * FROM {table_name} WHERE {search_condition} LIMIT 1"
			# Execute the query with params
			self.curs.execute(query, params or ())
			# Fetch one record
			entry = self.curs.fetchone()
			return entry  # Returns the entire row (column data) if found
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")
			return None
