class WordModel:
	def __init__(self,word:str,spelling:str,definitions:str,examples:str,cefr_level:str):
		self.word = word
		self.spelling = spelling
		self.definitions = definitions
		self.examples  = examples
		self.cefr_level = cefr_level
	def __str__(self):
		return f"""The word: {self.word} with the information : {self.spelling},
		{self.definitions},  {self.examples}, {self.cefr_level}"""
