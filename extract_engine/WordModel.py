"""
	Define WordModel 
"""

class WordModel:
	def __init__(self,word:str,spelling:str,definition:str,vietnam_def:str,example:str,level:str):
		self.word = word
		self.spelling = spelling
		self.definition = definition
		self.vietnam_def  = vietnam_def
		self.example  = example
		self.level = level
	def __str__(self):
		return f"""The word: {self.word} with the information : {self.spelling},
		{self.definition}, {self.vietnam_def}, {self.example}, {self.level}"""
