
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
  
# The text that you want to convert to audio 
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
with open("../extract_engine/result_after_extract.txt",'r',encoding='utf-8') as outfile:
        list_words = outfile.read().split("\n")
for word in list_words:
	myobj = gTTS(text=word, lang='en', slow=False) 
	myobj.save("{word}.mp3".format(word = word)) 
  
# Playing the converted file 
