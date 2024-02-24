from Database.Database import Database_SQLite3	 
from Web_Scrapping.Selenium.Selenium_Web_Scrapping import Scrapping_Word_Infor

if __name__ == "__main__":
	cambridge_book = "cam18_test1_reading_part_2"
	database_instance = Database_SQLite3("Database/CambridgeBookDatabase.db")
	scrap_instance = Scrapping_Word_Infor("Web_Scrapping/Selenium/chromedriver.exe")
	#list_words = ["peppermint","sprout","small", "best" ,"classic", "there" ,"crop", "electricity", "aubergine", "much","block", "environment", "soil"]
	with open(f"Data_after_handle/{cambridge_book}.txt",'r',encoding='utf-8') as outfile:
	 	list_words = outfile.read().split("\n")
	for word in list_words:
		if database_instance.check_word_existence_in_table("Vocabulary",word):
			if not database_instance.check_existence_of_value_in_Cambridge_Book_Link_Vocabular("Cambridge 18","Test 1","Reading",2,word): # if not existence
				database_instance.insert_word_to_Cambridge_Book_Link_Vocabulary("Cambridge 18","Test 1","Reading",2,word)
		else:
			type_word,spelling,CEFR_Level,definitions,examples = scrap_instance.scrap_word_by_selenium(word) # right now definitions just only one
			database_instance.insert_each_word(table_name = "Vocabulary",word = word,type_word = type_word,spelling = spelling,CEFR_Level = CEFR_Level,definitions = definitions,examples =examples)
			database_instance.insert_word_to_Cambridge_Book_Link_Vocabulary("Cambridge 18","Test 1","Reading",2,word)
		# should delete the last one of 
