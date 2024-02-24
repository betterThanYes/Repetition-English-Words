from abc import ABC,abstractmethod
from typing import List
class ExtractInterface(ABC):
	format_data  = ""
	@classmethod
	def can_ingest(cls,path:str) ->bool:
		ext = path.split('.')[-1]
		return ext == cls.format_data
	@classmethod
	@abstractmethod
	def parse(cls,path:str)->List[str]:
		pass
	