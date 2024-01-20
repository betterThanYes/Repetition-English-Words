
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
import threading 
# This module is imported so that we can  
# play the converted audio 
  
# The text that you want to convert to audio 
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
# with open("../extract_engine/result_after_extract.txt",'r',encoding='utf-8') as outfile:
#         list_words = outfile.read().split("\n")
def split_list_into_parts(word_list, num_parts):
    # Calculate the approximate size of each part
    part_size = len(word_list) // num_parts
    remainder = len(word_list) % num_parts

    # Divide the list into parts
    parts = [word_list[i * part_size: (i + 1) * part_size] for i in range(num_parts)]

    # If there is a remainder, add the remaining elements to the last part
    if remainder:
        parts[-1].extend(word_list[-remainder:])

    return parts

# Example usage:
word_list = ["hello", "hi", "entertainment", "quite", "quit", "word", "words", "noise", "milk", "cow","paper"]
num_parts = 3

result = split_list_into_parts(word_list, num_parts)

def create_and_save_audio(list_of_words):
	print(list_of_words)
	for word in list_of_words:
		print(word)
		myobj = gTTS(text=word, lang='en', slow=False) 
		myobj.save("{word}.mp3".format(word = word)) 
	print("End")
for i in range(num_parts):
	# t1 = threading.Thread(target=create_and_save_audio,args=(result[0],))
	# t2 = threading.Thread(target=create_and_save_audio,args=(result[1],))
	# t3 = threading.Thread(target=create_and_save_audio,args=(result[2],))
	t1 = threading.Thread(target=create_and_save_audio(result[0]))
	t2 = threading.Thread(target=create_and_save_audio(result[1]))
	t3 = threading.Thread(target=create_and_save_audio(result[2]))
	t1.start()
	t2.start()
	t3.start()

t1.join()
t2.join()
t3.join()
print("All is done")

  
# Playing the converted file 
