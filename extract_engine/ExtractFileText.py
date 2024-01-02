from ExtractInterface import ExtractInterface
from WordModel import WordModel

class ExtractFileText(ExtractInterface):
	format_data = 'txt'
	@classmethod
	def parse(cls,path:str)->list[WordModel]:
		if not can_ingest(path):
			raise Exception("can not extract because different types")
		# else:
			# handle to create List[WordModel]

