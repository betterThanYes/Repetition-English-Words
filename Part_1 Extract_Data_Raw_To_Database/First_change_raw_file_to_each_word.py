from Extract_Engine.WordController import extract_each_word_from_file,save_to_file_txt
import os

if __name__ == "__main__":
	cambridge_book_raw = "Cam18_Test_1_Reading_Part_2"
	cambridge_book_after_handle = "cam18_test1_reading_part_2"
	if not os.path.exists(f"Data_after_handle/{cambridge_book_after_handle}.txt"):
		words = extract_each_word_from_file("data_raw/{cambridge_book_raw}.txt")
		save_to_file_txt(f"Data_after_handle/{cambridge_book_after_handle}.txt",words)
