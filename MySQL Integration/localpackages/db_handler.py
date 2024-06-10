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

	def test_connection(self):
		return self.conn.is_connected()
