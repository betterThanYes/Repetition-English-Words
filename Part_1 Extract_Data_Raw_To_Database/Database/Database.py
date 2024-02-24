import sqlite3
#from typing import List
 
class Database_SQLite3:
    def __init__(self,dbpath):
        self.connect = sqlite3.connect(dbpath)
        self.cursor = self.connect.cursor()
 
    # def create_table(self,name_table):
    #     self.cursor.execute(f"SELECT name from sqlite_master WHERE type = 'table' AND name = '{name_table}'")
    #     table_exists = self.cursor.fetchone()
    #     if table_exists:
    #         print("The table exits. Delete it and create new one")
    #         self.cursor.execute(f"DROP TABLE {name_table};")
    #     self.cursor.execute(f"""CREATE TABLE {name_table} (
    #                             word TEXT,
    #                             definition TEXT,
    #                             spelling TEXT,
    #                             example TEXT,
    #                             CEFR_Level INTERGER,
    #                             http_audio TEXT
    #                         )""")
    #     print(f"Create {name_table} table")
    #     self.connect.commit()
    def insert_each_word(self,table_name,word,type_word,spelling,CEFR_Level,definitions,examples):
        # pick word as unique word
            try:
                new_index = self.get_last_index_table("Vocabulary_Id","Vocabulary")+1
                print("new_index:" + str(new_index))
                print(type(word))
                print(type(type_word))
                print(type(spelling))
                print(type(CEFR_Level))
                print(type(definitions))
                print(type(examples))

                self.cursor.execute(f"INSERT INTO {table_name} VALUES(?,?,?,?,?,?,?)",(new_index,word,type_word,spelling,CEFR_Level,definitions,examples))
                self.connect.commit()
                print("insert successfully the word:" + word)
            except Exception as e:
                print(f"error insert {e}")

    def __del__(self):
        print("Destructor called in Database instance")
        self.connect.close()
    def get_all_info_table(self,name_table):
        self.cursor.execute(f'SELECT * FROM {name_table}')
        self.connect.commit()
        return self.cursor.fetchall()
 
    def get_number_rows(self,name_table):
        self.cursor.execute(f'SELECT COUNT(*) from {name_table}')
        number_row = self.cursor.fetchone()[0]
        return number_row
 
    def get_column_names(self,name_table):
    #cursor.execute(f'PRAGMA table_info({name_table})')
        column_names = []
        self.cursor.execute(f"SELECT name FROM PRAGMA_TABLE_INFO('{name_table}');")
        result = self.cursor.fetchall()
        for element in result:
            column_names.append(element[0])
        return column_names
    def get_index_Cambridge_Book(self,book_name = None, book_test = None, book_section = None, book_task = None):
        self.cursor.execute(f"""SELECT CambridgeBook.Cambridge_Book_Id
                       FROM CambridgeBook
                       WHERE CambridgeBook.Book_Name = "{book_name}"
                       AND CambridgeBook.Test = "{book_test}"
                       AND CambridgeBook.Section = "{book_section}"
                       AND CambridgeBook.Task = {book_task}   
                    """)
        result = self.cursor.fetchone()
        self.connect.commit()
        return result[0]
    def get_words_belong_cambridgebook(self,list_cambridge_book = None):
        # user pick more than one book to learn vocabularis from books (ex: cam 10 and cam 11)
        print(list_cambridge_book[0])
        if len(list_cambridge_book) > 1:
            list_cambridge_book = tuple(list_cambridge_book)
            self.cursor.execute(f"SELECT Vocabulary.Word,Vocabulary.Type,Vocabulary.Spelling,Vocabulary.Cefr_Level,Vocabulary.Examples FROM Vocabulary WHERE Vocabulary.Vocabulary_Id IN (SELECT DISTINCT CambridgeBook_Link_Vocabulary.FK_Vocabulary_Id FROM CambridgeBook_Link_Vocabulary WHERE CambridgeBook_Link_Vocabulary.FK_CamBook_Id IN {list_cambridge_book})")
        else :
            self.cursor.execute(f"SELECT Vocabulary.Word,Vocabulary.Type,Vocabulary.Spelling,Vocabulary.Cefr_Level,Vocabulary.Examples FROM Vocabulary WHERE Vocabulary.Vocabulary_Id IN (SELECT DISTINCT CambridgeBook_Link_Vocabulary.FK_Vocabulary_Id FROM CambridgeBook_Link_Vocabulary WHERE CambridgeBook_Link_Vocabulary.FK_CamBook_Id IN ({list_cambridge_book[0]}))")
        #result = self.cursor.fetchall()
        return self.cursor.fetchall()
    def check_word_existence_in_table(self,name_table,word):
        self.cursor.execute(f"SELECT COUNT (Word) FROM {name_table} WHERE Word = '{word}';")
    # """.format(table="Vocabulary", word_test="entertainment"))
        result = self.cursor.fetchone()
        return result[0]
    def get_last_index_table(self,primary_key_name = None,name_table = None):
        self.cursor.execute(f"SELECT {primary_key_name} From {name_table} ORDER BY {primary_key_name} DESC LIMIT 1;")
        index_last = self.cursor.fetchone()
        print(index_last)
        if index_last:
            print(index_last[0])
            return index_last[0]
        else:
            return 0
    def delete_row(index = None):
        self.cursor.execute(f"DELETE FROM CambridgeBook_Link_Vocabulary WHERE id = {index}")
    def check_existence_of_value_in_Cambridge_Book_Link_Vocabular(self,book_name = None, book_test = None, book_section = None, book_task = None, word = None):
        self.cursor.execute(f"""SELECT CambridgeBook.CamBook_Id,Vocabulary.Vocabulary_Id
                       FROM CambridgeBook,Vocabulary
                       WHERE CambridgeBook.Book_Name = "{book_name}"
                       AND CambridgeBook.Test = "{book_test}"
                       AND CambridgeBook.Section = "{book_section}"
                       AND CambridgeBook.Task = {book_task}
                       AND Vocabulary.Word = "{word}" 
                       """)
        try:
            fk_cambook_id, fk_vocabulary_id = self.cursor.fetchone()
        except Exception as e:
            print(e)
            print("Error search")
            fk_cambook_id = 226
            fk_vocabulary_id = 549  # error code when meet word = "type"
        print(str(fk_cambook_id) + str(fk_vocabulary_id))
        self.cursor.execute(f"""SELECT 1
                                From CambridgeBook_Link_Vocabulary
                                Where CambridgeBook_Link_Vocabulary.Fk_CamBook_Id = {fk_cambook_id} AND CambridgeBook_Link_Vocabulary.FK_Vocabulary_Id = {fk_vocabulary_id}
                                """)
        is_exist = self.cursor.fetchone()
        #print(get_id_cam_voca)
        print("BOOL: " + str(bool(is_exist)))
        return  bool(is_exist)


    def insert_word_to_Cambridge_Book_Link_Vocabulary(self,book_name = None, book_test = None, book_section = None, book_task = None, word = None):
        new_index = self.get_last_index_table(primary_key_name = "Id",name_table = "CambridgeBook_Link_Vocabulary")+1
        self.cursor.execute(f"""INSERT INTO CambridgeBook_Link_Vocabulary(Id,FK_CamBook_Id,FK_Vocabulary_Id)
                       SELECT {new_index},CambridgeBook.CamBook_Id,Vocabulary.Vocabulary_Id
                       FROM CambridgeBook,Vocabulary
                       WHERE CambridgeBook.Book_Name = "{book_name}"
                       AND CambridgeBook.Test = "{book_test}"
                       AND CambridgeBook.Section = "{book_section}"
                       AND CambridgeBook.Task = {book_task}
                       AND Vocabulary.Word = "{word}" 
                       """)

        self.connect.commit()
# if __name__ == "__main__":
    #database_instance = Database_SQLite3("CambridgeBookDatabase.db")
    #database_instance.check_existence_of_value_in_Cambridge_Book_Link_Vocabular("Cambridge 18","Test 1","Reading",1,"small")
    # self,table_name,word,definitions,spelling,examples,CEFR_Level
    #database_instance.insert_each_word("Vocabulary","easy","hehehe","sda","adadas","dasdada")
    # result = database_instance.check_word_existence_in_table("Vocabulary","entertainment")
    #database_instance.insert_word_to_Cambridge_Book_Link_Vocabulary("Cambridge 10","Test 1","Reading",1,"easy")
# select word that inside Fk_Cambook_Id = 226
#     SELECT Vocabulary.Word
# From Vocabulary  
# JOIN CambridgeBook_Link_Vocabulary ON Vocabulary.Vocabulary_Id = CambridgeBook_Link_Vocabulary.FK_Vocabulary_Id
# WHERE CambridgeBook_Link_Vocabulary.Fk_CamBook_Id =226;