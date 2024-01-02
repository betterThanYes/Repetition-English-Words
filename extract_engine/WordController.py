from WordModel import WordModel
from typing import List
from ExtractFileText import ExtractFileText
class WordController:
	word_model = []
	@classmethod
	def pick_strategy(cls,path):
		ext = path.split('.')[-1]
		if ext == "txt" :
			return ExtractFileText
		

	@classmethod
	def extract_each_word_from_file(cls, path)->list[WordModel]:
		 strategy = pick_strategy(path)
		 cls.word_model = strategy.parse(path)
		#cls.word_model = ExtractFileText.parse(path)
	@classmethod
	def request_API_get_Json(cls):
		pass
	@classmethod
	def request_by_chat_gpt(cls):
		pass
	def save_to_database(cls):
		pass
