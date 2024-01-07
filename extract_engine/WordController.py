from WordModel import WordModel
from typing import List
from ExtractFileText import ExtractFileText
import spacy

# # Example usage:
# plural_word = input("Enter a plural word: ")
# singular_word = convert_to_singular(plural_word)
# print(f"The singular form of {plural_word} is: {singular_word}")
# 'CC': Coordinating conjunction
# 'CD': Cardinal number
# 'DT': Determiner
# 'EX': Existential there
# 'FW': Foreign word
# 'IN': Preposition or subordinating conjunction
# 'JJ': Adjective
# 'JJR': Adjective, comparative
# 'JJS': Adjective, superlative
# 'LS': List item marker
# 'MD': Modal
# 'NN': Noun, singular or mass
# 'NNS': Noun, plural
# 'NNP': Proper noun, singular
# 'NNPS': Proper noun, plural
# 'PDT': Predeterminer
# 'POS': Possessive ending    // consider
# 'PRP': Personal pronoun
# 'PRP$': Possessive pronoun
# 'RB': Adverb
# 'RBR': Adverb, comparative
# 'RBS': Adverb, superlative
# 'RP': Particle
# 'SYM': Symbol
# 'TO': to
# 'UH': Interjection
# 'VB': Verb, base form
# 'VBD': Verb, past tense
# 'VBG': Verb, gerund or present participle
# 'VBN': Verb, past participle
# 'VBP': Verb, non-3rd person singular present
# 'VBZ': Verb, 3rd person singular present
# 'WDT': Wh-determiner
# 'WP': Wh-pronoun
# 'WP$': Possessive wh-pronoun
# 'WRB': Wh-adverb
CONSTANT_MAP = {
    "shouldn't": "should",
    "couldn't": "could",
    "didn't": "did",
    "doesn't": "does",
    "isn't": "is",
    "aren't": "are",
    "wasn't": "was",
    "weren't": "were",
    "haven't": "have",
    "hasn't": "has",
    "won't": "will",
    "wouldn't": "would",
    "don't": "do",
    "doesn't": "does",
    "didn't": "did",
    "can't": "can",
    "cannot": "can",
    "i'm": "i",
    "you're": "you",
    "he's": "he",
    "she's": "she",
    "it's": "it",
    "we're": "we",
    "they're": "they",
}
def convert_word_to_good_format(word,nlp):
	#Currently, I don't keep the irregular verb. I change all of verb to be verb base
    doc =nlp(word)
    match doc[0].tag_:
    	case 'NNS'|"NNPS":
    		#print("Noun: " + word)
    		return doc[0].lemma_
    	case 'VBG'| 'VBZ' | 'VBD'|'VBN'|'NNS'|"NNPS" :
    		#print("Ved -Ving : " +word)
    		return doc[0].lemma_
    	# case "PRP" | "MD":
    	# 	word = word.lower()
    	# 	if word in CONSTANT_MAP.keys():
    	# 		return word
    	# 	#print("PRP or MD: " + word +" " + CONSTANT_MAP[word])
    	# 	return CONSTANT_MAP[word]
    	case _ : 
    		#print("Other type:" + word)
    		return word

def  pick_strategy(path):
		ext = path.split('.')[-1]
		if ext == "txt" :
			return ExtractFileText
def extract_each_word_from_file(path)->list[str]:
		strategy = pick_strategy(path)
		list_words = strategy.parse(path)
		return re_format_list_words(list_words) # which is right format to request info by API
def request_API_get_Json():
	pass
def request_by_chat_gpt():
	pass
def save_to_database():
	pass
def re_format_list_words(words:list[str])->set[str]:
	# In comming update, I will update and make the re_format better
	nlp = spacy.load("en_core_web_sm")
	for i in range(len(words)):
		words[i] = convert_word_to_good_format(words[i],nlp)
	with open("result_after_extract.txt", "w") as file:
		for word in set(words):
			file.write(word + "\n")
	return set(words)
