import mysql.connector


class db_handler:
	def __init__(self, host, user, password, database):
		try:
			self.conn = mysql.connector.connect(
				host=host, user=user, password=password, database=database
			)
			self.curs = self.conn.cursor()
		except mysql.connector.Error as Error:
			print(f"Encountered a database error: {Error}")

	def test_connection(self) -> bool:
		"""
		Test if the connection to the database and return its value
		:return:
		"""

		return self.conn.is_connected()

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

	def del_entry(self, table_name:str, condition):
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

	def mod_entry(self, table_name, updates, condition):
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

