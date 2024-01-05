from ExtractInterface import ExtractInterface
from WordModel import WordModel
import re
class ExtractFileText(ExtractInterface):
	format_data = 'txt'
	@classmethod
	def parse(cls,path:str)->list[WordModel]:
		if not cls.can_ingest(path):
			raise Exception("can not extract because different types")
		else:
			with open(path,'r',encoding='utf-8') as outfile:
				#content = content.replace("-","") outfile.read()
				cleaned_string = re.sub('[^a-zA-Z\\s-]', '', outfile.read())
				#print(cleaned_string)
				list_of_word = cleaned_string.split()
				print("List of word: " +cleaned_string)
				return list_of_word
