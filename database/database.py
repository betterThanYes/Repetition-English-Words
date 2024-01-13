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
								CEFR_Level INTERGER,
								http_audio TEXT
							)""")
		print(f"Create {name_table} table")
		self.connect.commit()
	def insert_each_word(self,table_name,word,definition,spelling,example,CEFR_Level,http_audio):
		try:
				self.cursor.execute(f"INSERT INTO {table_name} VALUES(?,?,?,?,?,?)",(word,definition,spelling,example,CEFR_Level,http_audio))
				self.connect.commit()
				print("insert successfully")
		except Exception as e:
			print(f"error insert {e}")
	def query_data(self,name_table):
		# should implement in the comming future 
		self.cursor.execute(f"SELECT word FROM {name_table} WHERE CEFR_Level >=3")
		print(self.cursor.fetchall())
		self.connect.commit()

	def close_database(self):
		self.connect.close()
# name_table = "words"
# database = Database_SQLite3('cambridge.db')
# database.create_table(name_table)
# database.insert_each_word(table_name=name_table, word='hello', definition='hi',
#                            spelling='camon', example='helloVietNam',CEFR_Level = 3, http_audio='https://api.dictionaryapi.dev/media/pronunciations/en/hello-au.mp3')
# database.insert_each_word(table_name=name_table, word='word', definition='hi',
#                            spelling='camon', example='word',CEFR_Level = 1, http_audio='https://api.dictionaryapi.dev/media/pronunciations/en/word-us.mp3')
# database.insert_each_word(table_name=name_table, word='entertainment', definition='hi',
#                            spelling='camon', example='entertainment',CEFR_Level = 2, http_audio='https://api.dictionaryapi.dev/media/pronunciations/en/entertainment-us.mp3')
# database.insert_each_word(table_name=name_table, word='destiny', definition='hi',
#                            spelling='camon', example='destiny',CEFR_Level = 5, http_audio='https://api.dictionaryapi.dev/media/pronunciations/en/destiny-us.mp3')
# database.insert_each_word(table_name=name_table, word='definition', definition='hi',
#                            spelling='camon', example='definition',CEFR_Level = 3, http_audio='https://api.dictionaryapi.dev/media/pronunciations/en/definition-us.mp3')
# database.query_data(name_table)
# database.close_database()


