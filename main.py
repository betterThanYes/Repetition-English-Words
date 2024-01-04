import necessary file

if __main__ == "__main__":
    with open (file_test, "r") as outfile:
        #list_of_each_wrod = extract_list_words_from_line()
        list_raw_words = SuitableClass.parse()
        for word in list_raw_words:
            word_enough_info = WordModel()
            word = re_structure_word(word)
            word_enough_info = request_API_to_get_info(word)
            Database.saveDatabase(word_enough_info)

