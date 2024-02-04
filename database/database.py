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
 
    def __del__(self):
        print("Destructor called in Database instance")
        self.connect.close()
    def get_all_info_table(self,name_table):
        self.cursor.execute(f'SELECT * FROM {name_table}')
        self.connect.commit()
        return self.cursor.fetchall()
 
    def get_number_column(self,name_table):
        self.cursor.execute(f'SELECT COUNT(*) from {name_table}')
        number_row = self.cursor.fetchone()[0]
        return number_row
 
    def get_column_names(self,name_table):
    #cursor.execute(f'PRAGMA table_info({name_table})')
        column_names = []
        self.cursor.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{name_table}');")
        result = self.cursor.fetchall()
        for element in result:
        #print(type(element))
            column_names.append(element[0])
        return column_names
    def get_index_Cambridge_Book(self,book_name = None, book_test = None, book_section = None, book_task = None):
        self.cursor.execute(f"""SELECT Cambridge_Book.Cambridge_Book_Id
                       FROM Cambridge_Book
                       WHERE Cambridge_Book.Book_Name = "{book_name}"
                       AND Cambridge_Book.Book_Test = "{book_test}"
                       AND Cambridge_Book.Book_Section = "{book_section}"
                       AND Cambridge_Book.Book_Task = {book_task}   
                    """)
        result = self.cursor.fetchone()
        self.connect.commit()
        return result[0]
    def get_words_belong_cambridgebook(self,list_cambridge_book = None):
        print(list_cambridge_book[0])
        if len(list_cambridge_book) > 1:
            list_cambridge_book = tuple(list_cambridge_book)
            self.cursor.execute(f"SELECT Vocabulary.vocabulary_id,Vocabulary.word,Vocabulary.definition FROM Vocabulary WHERE Vocabulary.vocabulary_id IN (SELECT DISTINCT Cambridge_Book_Link_Vocabulary.FK_vocabulary_id FROM Cambridge_Book_Link_Vocabulary WHERE Cambridge_Book_Link_Vocabulary.FK_cambridge_book_id IN {list_cambridge_book})")
        else :
            self.cursor.execute(f"SELECT Vocabulary.vocabulary_id,Vocabulary.word,Vocabulary.definition FROM Vocabulary WHERE Vocabulary.vocabulary_id IN (SELECT DISTINCT Cambridge_Book_Link_Vocabulary.FK_vocabulary_id FROM Cambridge_Book_Link_Vocabulary WHERE Cambridge_Book_Link_Vocabulary.FK_cambridge_book_id IN ({list_cambridge_book[0]}))")
        result = self.cursor.fetchall()
        print(result)    
# connect = sqlite3.connect("../Database/CambridgeBookDatabase.db")
# cursor = self.connect.cursor()
# self.list_column_names = get_column_names("Cambridge_Book")
# database_instance = Database_SQLite3("../Database/CambridgeBookDatabase.db")
# database_instance.get_words_belong_cambridgebook(list_cambridge_book = [2])