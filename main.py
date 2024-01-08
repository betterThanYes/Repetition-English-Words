#from extract_engine.WordController import WordController
from extract_engine.WordModel import WordModel
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
            list_word_after = []
            for word in list_words:
                print(word)
                word, spelling , definition, example, level = requestAPIWord(word)
                wordModel = WordModel(word, spelling , definition, example, level)
                list_word_after.append(wordModel)


            
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
