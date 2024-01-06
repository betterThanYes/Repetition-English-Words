from WordModel import WordModel
from typing import List
from ExtractFileText import ExtractFileText
from pattern.en import lexeme
from pattern.en import pluralize, singularize
from textblob import TextBlob
import spacy
# def convert_to_singular(plural_word):
#     return singularize(plural_word)

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
		if words[i] == "consultancy":
			print("ASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS: " + words[i])
		words[i] = convert_word_to_good_format(words[i],nlp)
		if words[i] == "consultancy":
			print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB: " + words[i])
		#words[i] = TextBlob(words[i]).correct() # recorrect the word
		if words[i] == "consultancy":
			print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC: " + words[i])
	return set(words)

#extract_each_word_from_file()
test = extract_each_word_from_file("Cam18_Test_1_Reading_Part_1.txt")
print("clean word: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
for word in test:
	print(word)