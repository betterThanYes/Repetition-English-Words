import genanki

class AnkiGenerator:

	def __init__(self,deck_name):
		self.note_model = genanki.Model(
    				1234567890,  # Unique ID for the model
    				'My Note Model',
    		fields=[
        		{'name': 'Definition'},
        		{'name': 'TypeOfWord'},
        		{'name': 'Word'},
        		{'name': 'Phonetic'},  # This field is for the local audio path
        		{'name': 'CEFR_Level'},
        		{'name': 'Example'},
        		{'name': 'Audio_Word'}
    			],
    		templates=[
        	{
            	'name': 'Card 1',
            	'qfmt': """
            	<style>
      			h1 {
        			color: rgb(173, 216, 230);
        			text-align: center;
        			margin-top: 0;
      			}

      			#main {
        			color: blue;
        			text-align: left;
      			}
    			</style>
    			<body>
    			<h1>No pain, No gain</h1>
    			<image src = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png" />
    			<div id="main">
      			<p>Suggest:</p>
      			<ul>
        				<li>Kind of Word : {{TypeOfWord}}</li>
        				<li>Definition : {{Definition}}</li>
      			</ul>
    			</div>
    			<h2>Guess the word</h2>
    			{{type:Word}}
    			</body>
            	"""
            	,'afmt': 
            	"""
            		{{FrontSide}}
            		</html><hr id="answer">
            		<div id="backside">
            		<ul>
        				Information of the word
        				<li>Phonetic: {{Phonetic}}</li>
        				<li>CEFR Level: {{CEFR_Level}} </li>
        				<li>Example: {{Example}}</li>
      				</ul>
      				{{Audio_Word}}
      				</div>

            	"""
            	  # You can customize this template as needed
        	}
    		]
		)
		self.my_deck = genanki.Deck(
    			deck_id = 987654321,  # Unique ID for the deck
    			name = "{deck}".format(deck = deck_name)

		)
		self.my_package = genanki.Package(self.my_deck)
	def create_note(self,definition,type_of_word,word,phonetic,cefr_level,example,audio_word):
		my_note = genanki.Note(
    		model=self.note_model,
    		#'My Custom Deck'  # Deck name (should be a string)
    		fields=[f'{definition}', f'{type_of_word}',f'{word}',f'{phonetic}',f'{cefr_level}',f'{example}',"[sound:{}]".format(audio_word)]
    		)	
		self.my_deck.add_note(my_note)
	def create_apkg_file(self,name):
		self.my_deck.write_to_file(name)
	def add_audio_file(self,audio_path = None):
		self.my_package.media_files.append(audio_path)

		# {'name': 'Definition'},
  #       		{'name': 'TypeOfWord'},
  #       		{'name': 'Word'},
  #       		{'name': 'Phonetic'},  # This field is for the local audio path
  #       		{'name': 'CEFR Level'},
  #       		{'name': 'Example'},
  #       		{'name': 'Audio_Word'}
list_dummy = [('def_word_1','type_word_1','word_1','phone_word_1','level_1','example_1','../music_image/love-us.mp3'),
  				('def_word_2','type_word_2','word_2','phone_word_2','level_2','example_2','../music_image/hello-au.mp3')
  			 ]
anki_test = AnkiGenerator("My Deck Test 1")
for word in list_dummy:
	anki_test.create_note(word[0],word[1],word[2],word[3],word[4],word[5],word[6].replace("../music_image/",""))
	anki_test.add_audio_file(audio_path = word[6])
anki_test.create_apkg_file('output.apkg')
anki_test.my_package.write_to_file('output.apkg')








