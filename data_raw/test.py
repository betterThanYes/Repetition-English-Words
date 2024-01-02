import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

# Download NLTK data (you only need to do this once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Open the text file in read mode with UTF-8 encoding
with open('Cam18_Test_1_Reading_Part_1.txt', 'r', encoding='utf-8') as file:
    # Read the content of the text file
    content = file.read()

# Tokenize the text into sentences
sentences = sent_tokenize(content)

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Extract original (singular) nouns
original_nouns = []

for sentence in sentences:
    words = word_tokenize(sentence)
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    for word, pos in tagged_words:
        # Check if the word is a singular noun and lemmatize it
        if pos == 'NN':
            original_noun = lemmatizer.lemmatize(word, pos='n')
            original_nouns.append(original_noun)

# Print the original nouns
for noun in original_nouns:
    print(noun)