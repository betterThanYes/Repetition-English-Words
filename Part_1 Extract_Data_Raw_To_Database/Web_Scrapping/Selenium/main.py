from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# link cambridge : https://dictionary.cambridge.org/vi/dictionary/english/
# link soccer : "https://www.adamchoi.co.uk/overs/detailed"
#website = f"https://dictionary.cambridge.org/vi/dictionary/english/{word}"
# way_to_find_mat_element = By.XPATH, value='//span[@class = "hw dhw"]'
if __name__ == "__main__":
	service = Service(excutable_path = "chromedriver.exe")
	option = Options()
	option.add_argument("--headless") # Runs Chrome in headless mode.

	driver = webdriver.Chrome(service = service,options = option)

	driver.get(f"https://dictionary.cambridge.org/vi/dictionary/english/resplendently")
	# / : chidrent , //tag[@class = "Value"]
	# Way 1 :
	# examples = driver.find_elements(By.XPATH, value='//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[@class = "examp dexamp"]')
	# print("Test 1")
	# type_word = driver.find_element(By.XPATH, value = '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]')
	# print("Test 2")
	# spelling = driver.find_element(By.XPATH,value = '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/span[2]/span[3]/span')
	# print("Test 3")
	# definition = driver.find_element(By.XPATH,value = '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div')
	# print("Test 4")
	# cefr = driver.find_element(By.XPATH,value = '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/span/span')
	# print("Test 5")
	# Way 2:
	try:
		examples = WebDriverWait(driver,10).until(
			EC.presence_of_all_elements_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/div[@class = "examp dexamp"]')))
	except Exception as e:
		print("Error: " + str(e))
		examples = ""
	try:
		type_word = WebDriverWait(driver,10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/div[2]')))
	except Exception as e:
		print("Error: " + str(e))
		type_word = ""
	try:
		spelling = WebDriverWait(driver,10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]//span[@class = "ipa dipa lpr-2 lpl-1"]')))
	except Exception as e:
		print("Error: " + str(e))
		spelling = ""	
	try:
		definition =  WebDriverWait(driver,10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/div')))
	except Exception as e:
		print("Error: " + str(e))
		definition = ""
	try:
		cefr = WebDriverWait(driver,10).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="page-content"]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[2]/span/span')))
	except Exception as e:
		print("Error cefr : " + str(e))
		cefr = ""
	if examples:
		for example in examples:
			print(example.text)
	else:
		print("No examples")
	if type_word:
		print(type_word.text)
	else:
		print("No type_word")
	if cefr:
		print(cefr.text)
	else:
		print("No cefr")
	if spelling:
		print(spelling.text)
	else:
		print("No spelling")
	if definition:
		print(definition.text)
	else:
		print("No definition")
	time.sleep(2)
	driver.quit()


# learn udemy 
# handle part 1 of  my project
# handle part 2 of my project
# package,