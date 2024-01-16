#from extract_engine.WordController import WordController
#from  WordController request_API_get_Json
#from Database
from database.database import Database_SQLite3
from request_chatgpt.InitClient import Client_ChatGPT 
from request_chatgpt.ExtractResponse import Extract_Response
import time
from request_chatgpt.requestAudio import *
import sqlite3
# from request_chatgpt.retryRequest import *

API_KEY = "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"
MODEL = "gpt-3.5-turbo"

def retryRequest(list_words, client_chatGpt, database) :

    print("Retry request ")
    name_table = 'words'
    list_words_wrong = []

    for num in range(0,3) :
        for word in list_words:
            try:
                responseFromGPT = client_chatGpt.get_response_from_prompt(word)
                extractFromRespone = Extract_Response(responseFromGPT)
                word, definition , phonetic, CEFR_level , example = extractFromRespone.extract()
                audio = getAudioByWord(word)

                if type(definition) is list :
                    definition  = ', '.join(definition)

            
                print("Definition:", definition)
                print("Word:", word)
                print("Phonetic:", phonetic)
                print("CEFR Level:", CEFR_level)
                print("Example:", example)
                print("Audio:", audio)

                # dummy data 
                database.insert_each_word(table_name= name_table, word= word, definition = definition,
                        spelling=phonetic, example=example, http_audio= audio)
                # database.insert_each_word(table_name= name_table, word= 'gr', definition=definition,
                #            spelling=phonetic, example=example, http_audio='https')
            except Exception as e:
                if word not in list_words_wrong :
                    list_words_wrong.append(word)
                    saveWordToTextFile(word)
                print(f"error occurred: {e} Extract next word ")                
            time.sleep(10)

        list_words = list_words_wrong
    return 


def saveWordToTextFile(word) :
    with open('wrong_text.txt', 'a', encoding="utf-8") as wf:
        wf.write(word + '\n')
        
if __name__ == "__main__":
    try:
        database = Database_SQLite3("share_database/word.db")
        name_table = 'words'

        database.create_table(name_table) 
        client_chatGpt  = Client_ChatGPT(API_KEY, MODEL)
        client = client_chatGpt.set_API_key()

        with open("extract_engine/result_after_extract.txt",'r',encoding='utf-8') as outfile:
            list_words = outfile.read().split("\n")

            # list_words = ["hello", "like","environment"]
            list_words_wrong = []

            for word in list_words:
                try:
                    responseFromGPT = client_chatGpt.get_response_from_prompt(word)
                    extractFromRespone = Extract_Response(responseFromGPT)
                    word, definition , phonetic, CEFR_level , example = extractFromRespone.extract()
                    audio = getAudioByWord(word)

                    if type(definition) is list :
                        definition  = ', '.join(definition)

                    print("Definition:", definition)
                    print("Word:", word)
                    print("Phonetic:", phonetic)
                    print("CEFR Level:", CEFR_level)
                    print("Example:", example)
                    print("Audio:", audio)

                    # dummy data 
                    database.insert_each_word(table_name= name_table, word= word, definition = definition,
                            spelling=phonetic, example=example, http_audio= audio)
                    # database.insert_each_word(table_name= name_table, word= 'gr', definition=definition,
                    #            spelling=phonetic, example=example, http_audio='https')
                except Exception as e:
                    if word not in list_words_wrong :
                        list_words_wrong.append(word)
                        saveWordToTextFile(word)
                    print(f"error occurred: {e} Extract next word ")                
                time.sleep(10)

            # if len(list_words_wrong) > 0 :
            #     retryRequest(list_words_wrong,client_chatGpt,database)
        database.close_database()       
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
