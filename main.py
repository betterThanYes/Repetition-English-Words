#from extract_engine.WordController import WordController
if __name__ == "__main__":
    
        #list_word = extract_list_words_from_line()
        #list_word = 
        # for word in list_word:
        #     word_enough_info = WordModel()
        #     word = re_structure_word(word)
        #     word_enough_info = request_API_to_get_info(word)
        #     Database.saveDatabase(word_enough_info)
    try:
        with open("extract_engine/result_after_extract.txt",'r',encoding='utf-8') as outfile:
            list_words = outfile.read().split("\n")
            for word in list_words:
                print(word)
            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
