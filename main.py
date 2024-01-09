#from extract_engine.WordController import WordController
#from  WordController request_API_get_Json
#from Database
from database.database import Database_SQLite3
from request_chatgpt.InitClient import Client_ChatGPT 
from request_chatgpt.ExtractResponse import Extract_Response

import sqlite3

API_KEY = "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"
MODEL = "gpt-3.5-turbo"


if __name__ == "__main__":
    try:
        database = Database_SQLite3("share_database/word.db")
        name_table = 'words'
        #list_word = extract_list_words_from_line()
        #list_word = 
        # for word in list_word:
        #     word_enough_info = WordModel()
        #     word = re_structure_word(word)
        #     word_enough_info = request_API_to_get_info(word)
        #     Database.saveDatabase(word_enough_info)
        database.create_table(name_table) 
        client_chatGpt  = Client_ChatGPT(API_KEY, MODEL)
        client = client_chatGpt.set_API_key()

        with open("extract_engine/result_after_extract.txt",'r',encoding='utf-8') as outfile:
            list_words = outfile.read().split("\n")
            for word in list_words:
                responseFromGPT = client_chatGpt.get_response_from_prompt(word)
                extractFromRespone = Extract_Response(responseFromGPT)
                word1, definition , phonetic, CEFR_level , example = extractFromRespone.extract()

                print("Definition:", definition)
                print("Word:", word1)
                print("Phonetic:", phonetic)
                print("CEFR Level:", CEFR_level)
                print("Example:", example)
                # word = request_API_get_Json(word)
                #Database.save_word_to_data(word)
                #c.execute("INSERT INTO words VALUES()")

                # dummy data 
                database.insert_each_word(table_name= name_table, word= word, definition= ', '.join(definition),
                           spelling=phonetic, example=example, http_audio='https')
                # database.insert_each_word(table_name= name_table, word= 'gr', definition=definition,
                #            spelling=phonetic, example=example, http_audio='https')
        database.close_database()       
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
