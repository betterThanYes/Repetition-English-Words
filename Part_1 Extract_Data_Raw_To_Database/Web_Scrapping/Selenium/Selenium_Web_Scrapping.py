from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from Database_Test import Database_SQLite3
import json
import time
class Scrapping_Word_Infor:
	list_cefr = ["A1","A2","B1","B2","C1","C2"]
	def __init__(self,path_file_executable):
		self.service = Service(excutable_path = path_file_executable)
		self.option = Options()
		self.option.add_argument("--headless") # Runs Chrome in headless mode.
		self.driver = webdriver.Chrome(service = self.service,options = self.option)
	def scrap_word_by_selenium(self,word):
		print("word that need to scrap: " + word)
		self.driver.get(f"https://dictionary.cambridge.org/vi/dictionary/english/{word}")
		# examples = None
		# type_word = None
		# spelling = None
		# definition = None
		# cefr = None
		# #<div class="def-body ddef_b"><div class="examp dexamp"><span class="eg deg">She <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/drink" title="drinks" rel="">drinks</a> peppermint-flavoured <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/tea" title="tea" rel="">tea</a>.</span></div> </div>
		# try:
		# 	header =  WebDriverWait(self.driver,5).until(
		# 	EC.presence_of_element_located((By.XPATH, '//div[@class="def-body ddef_b"]')))
		# 	if header:
		# 		print("Exist header")
		# 	examples = WebDriverWait(header,5).until(
		# 	EC.presence_of_all_elements_located((By.XPATH, './/div[@class ="examp dexamp"]')))
		# except Exception as e:
		# 	try:
		# 		examples = WebDriverWait(self.driver,5).until(
		# 		EC.presence_of_all_elements_located((By.XPATH, '//ul[@class = "hul-u hul-u0 ca_b daccord_b lm-0"]/li[@class = "eg dexamp hax"]')))
		# 	except Exception as e:
		# 		print("Error examples : " + str(e))
		# try:
		# 	type_word = WebDriverWait(self.driver,10).until(
		# 		EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]')))
		# except Exception as e:
		# 	print("Error type_word : " + str(e))
		# 	type_word_string = "No type word"
		# try:
		# 	spelling = WebDriverWait(self.driver,10).until(
		# 		EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]//span[@class = "ipa dipa lpr-2 lpl-1"]')))
		# except Exception as e:
		# 	print("Error spelling : " + str(e))
		# 	spelling_string = "No spelling"	
		# try:
		# 	definition =  WebDriverWait(self.driver,10).until(
		# 		EC.presence_of_element_located((By.XPATH, '//div[@class = "def ddef_d db"]')))
		# 	#<div class="def ddef_d db">an <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/oval" title="oval" rel="">oval</a>, <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/purple" title="purple" rel="">purple</a> <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/vegetable" title="vegetable" rel="">vegetable</a> that is <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/white" title="white" rel="">white</a> inside and is usually <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/eaten" title="eaten" rel="">eaten</a> <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/cooked" title="cooked" rel="">cooked</a></div>
		# except Exception as e:
		# 	print("Error definition : " + str(e))
		# 	definition_string = "No definition"
		# try:
		# 	cefr = WebDriverWait(self.driver,5).until(
		# 		EC.presence_of_element_located((By.XPATH, '//span[@class="def-info ddef-info"]/span[contains(@class, "epp-xref dxre")]')))

		# #<span class="def-info ddef-info"><span class="epp-xref dxref B2">B2</span> </span>
		# except Exception as e:
		# 	print("Error cefr : " + str(e))
		# 	cefr_string = "No cefr"
		# if examples:
		# 	arr_examples = []
		# 	for example in examples:
		# 		print(example.text)
		# 		arr_examples.append(example.text)
		# 	json_string_examples = json.dumps(arr_examples)
		# else:
		# 	print("No examples")
		# 	json_string_examples = "No examples"
		# if type_word:
		# 	print(type_word.text)
		# 	type_word_string = type_word.text
		# else:
		# 	print("No type_word")
		# if cefr:
		# 	if cefr.text in self.list_cefr:
		# 		print(cefr.text)
		# 		cefr_string = cefr.text
		# else:
		# 	print("No cefr")
		# if spelling:
		# 	print(spelling.text)
		# 	spelling_string = spelling.text
		# else:
		# 	print("No spelling")
		# if definition:
		# 	print(definition.text)
		# 	definition_string = definition.text
		# else:
		# 	print("No definition")
		type_word_string = self.scrap_type_word_by_selenium(word)
		spelling_string  = self.scrap_spelling_by_selenium(word)
		cefr_string      = self.scrap_cefr_by_selenium(word)
		definition_string= self.scrap_definition_by_selenium(word)
		json_string_examples = self.scrap_examples_by_selenium(word)
		time.sleep(2)
		return type_word_string,spelling_string,cefr_string,definition_string,json_string_examples
	def scrap_type_word_by_selenium(self,word):
		#self.driver.get(f"https://dictionary.cambridge.org/vi/dictionary/english/{word}")   
		type_word = None
		try:
			type_word = WebDriverWait(self.driver,3).until(
				EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]')))
		except Exception as e:
			print("Error type_word : " + str(e))
			type_word_string = "No type word"
		if type_word:
			print(type_word.text)
			type_word_string = type_word.text
		else:
			print("No type_word")
		return type_word_string
	def scrap_examples_by_selenium(self,word):
		examples = None
		json_string_examples = None
		try:
			header =  WebDriverWait(self.driver,5).until(
			EC.presence_of_element_located((By.XPATH, '//div[@class="def-body ddef_b"]')))
			if header:
				print("Exist header")
			examples = WebDriverWait(header,5).until(
			EC.presence_of_all_elements_located((By.XPATH, './/div[@class ="examp dexamp"]')))
		except Exception as e:
			try:
				examples = WebDriverWait(self.driver,5).until(
				EC.presence_of_all_elements_located((By.XPATH, '//ul[@class = "hul-u hul-u0 ca_b daccord_b lm-0"]/li[@class = "eg dexamp hax"]')))
			except Exception as e:
				print("Error examples : " + str(e))
				json_string_examples = "No examples"
		if examples:
			arr_examples = []
			for example in examples:
				print(example.text)
				arr_examples.append(example.text)
			json_string_examples = json.dumps(arr_examples)
		return json_string_examples
	def scrap_spelling_by_selenium(self,word):
		spelling = None
		try:
			spelling = WebDriverWait(self.driver,5).until(
				EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]//span[@class = "ipa dipa lpr-2 lpl-1"]')))
		except Exception as e:
			print("Error spelling : " + str(e))
			spelling_string = "No spelling"
		if spelling:
			print(spelling.text)
			spelling_string = spelling.text
		else:
			print("No spelling")
		return spelling_string
	def scrap_cefr_by_selenium(self,word):
		cefr = None
		try:
			cefr = WebDriverWait(self.driver,5).until(
				EC.presence_of_element_located((By.XPATH, '//span[@class="def-info ddef-info"]/span[contains(@class, "epp-xref dxre")]')))
		#<span class="def-info ddef-info"><span class="epp-xref dxref B2">B2</span> </span>
		except Exception as e:
			print("Error cefr : " + str(e))
			cefr_string = "No cefr"
		if cefr:
			if cefr.text in self.list_cefr:
				print(cefr.text)
				cefr_string = cefr.text
		else:
			print("No cefr")
		return cefr_string
	def scrap_definition_by_selenium(self,word):
		definition = None
		try:
			definition =  WebDriverWait(self.driver,10).until(
				EC.presence_of_element_located((By.XPATH, '//div[@class = "def ddef_d db"]')))
			#<div class="def ddef_d db">an <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/oval" title="oval" rel="">oval</a>, <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/purple" title="purple" rel="">purple</a> <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/vegetable" title="vegetable" rel="">vegetable</a> that is <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/white" title="white" rel="">white</a> inside and is usually <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/eaten" title="eaten" rel="">eaten</a> <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/cooked" title="cooked" rel="">cooked</a></div>
		except Exception as e:
			print("Error definition : " + str(e))
			return  "No definition"
		if definition:
			print(definition.text)
			return definition.text

if __name__ == "__main__":
	print("Hello")
	word = "carrot"
	database_instance = Database_SQLite3("../../Database/CambridgeBookDatabase.db")
	scrap_instance = Scrapping_Word_Infor("chromedriver.exe")
	print(scrap_instance.scrap_word_by_selenium(word))

	#type_word,spelling,CEFR_Level,definitions,examples = scrap_instance.scrap_word_by_selenium(word) # right now definitions just only one
	#print(type_word,spelling,CEFR_Level,definitions,examples)
	# print(type(type_word))
	# print(type(spelling))
	# print(type(spelling))
	# print(type(definitions))
	# print(type(examples))
	# print(type(word))
	#database_instance.insert_each_word(table_name = "Vocabulary",word = word,type_word = type_word,spelling = spelling,CEFR_Level = CEFR_Level,definitions = definitions,examples =examples)
	
	# <ul class="hul-u hul-u0 ca_b daccord_b lm-0"><li class="eg dexamp hax">It's <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/rather" title="rather" rel="">rather</a>
	#  early to be <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/sow" 
	#  title="sowing" rel="">sowing</a> carrot <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/seed" title="seeds"
	#   rel="">seeds</a>, isn't it?</li><li class="eg dexamp hax">If you put carrot <a class="query" href="https://dictionary.cambridge.org/vi/dicti
	#   onary/english/tops" title="tops" rel="">tops</a> in <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/water" 
	#   title="water" rel="">water</a> they <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/start" title="start" rel
	#   ="">start</a> to <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/grow" title="grow" rel="">grow</a>.</li><li clas
	#   s="eg dexamp hax">The first <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/solid" title="solid" rel="">solid</a> 
	#   <a class="query" href="https://dictionary.cambridge.org/vi/dictionary/english/food" title="food" rel="">food</a> she gave her <a class="query" hr
	#   ef="https://dictionary.cambridge.org/vi/dictionary/english/baby" title="baby" rel="">baby</a> was <a class="query" href="https://dictionary.cambrid
	#   ge.org/vi/dictionary/english/mash" title="mashed" rel="">mashed</a> carrot.</li><li class="eg dexamp hax">We had carrot and <a class="query" href="
	#   https://dictionary.cambridge.org/vi/dictionary/english/coriander" title="coriander" rel="">coriander</a> <a class="query" href="https://dictionar
	#   y.cambridge.org/vi/dictionary/english/soup" title="soup" rel="">soup</a> for <a class="query" href="https://dictionary.cambridge.org
	#   /vi/dictionary/english/lunch" title="lunch" rel="">lunch</a>.</li></ul>