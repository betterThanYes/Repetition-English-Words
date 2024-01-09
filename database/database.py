import sqlite3

class Database_SQLite3:

	def __init__(self,dbpath):
		self.connect = sqlite3.connect(dbpath)
		self.cursor = self.connect.cursor()

	def create_table(self,name_table):
		self.cursor.execute(f"SELECT name from sqlite_master WHERE type = 'table' AND name = '{name_table}'")
		table_exists = self.cursor.fetchone()
		if table_exists:
			print("The table exits. Delete it and create new one")
			self.cursor.execute(f"DROP TABLE {name_table};")
		self.cursor.execute(f"""CREATE TABLE {name_table} (
								word TEXT,
								definition TEXT,
								spelling TEXT,
								example TEXT,
								http_audio TEXT
							)""")
		print(f"Create {name_table} table")
		self.connect.commit()
	def insert_each_word(self,table_name,word,definition,spelling,example,http_audio):
		try:
				self.cursor.execute(f"INSERT INTO {table_name} VALUES(?,?,?,?,?)",(word,definition,spelling,example,http_audio))
				self.connect.commit()
				print("insert successfully")
		except Exception as e:
			print(f"error insert {e}")
	def close_database(self):
		self.connect.close()
# database = Database_SQLite3('database.db')
# database.create_table('words')
# database.insert_each_word(table_name='words', word='hello', definition='xinchao',
#                            spelling='camon', example='helloVietNam', http_audio='https')
# database.close_database()


