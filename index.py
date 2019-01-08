import utilities
import paratoline as ptl
import linetoword as ltw
import wordtoletter as wtl
import recognize
import sys
import spellcheck

arg1 = sys.argv[1]
arg2 = sys.argv[2]

utilities.clear_folder('Output/')

# Erase the contents of the file to store our results
#open("C:/Users/thanga/Documents/Python/EMNIST_CNN_AUTOMATED/outputwords.txt","w").close()

pages = utilities.load_images_from_folder(arg1)

for k in range(0,len(pages)):
	# Clear all the folders to avoid overlap of new input
	utilities.clear_folder('Sentences/')
	utilities.clear_folder('Words/')
	utilities.clear_folder('Letters/')

	# Opening file in append + mode -> creates the file if it does'nt exist
	file = open("Output/page" + str(k) + ".txt","a+")

	# Segmenting a page into sentences
	ptl.para_to_line(pages[k])


	# Loading sentences from the folder
	sentences = []
	sentences = utilities.load_images_from_folder('Sentences/')
	no_of_words_per_sentence = []
	sentence_counter = 0
	word_counter = 0
	temp = []
	# To find no of words per sentence
	for i in range(0,len(sentences)):
		ltw.line_to_word(sentences[i])
		temp = utilities.load_images_from_folder('Words/')
		no_of_words_per_sentence.append(len(temp))
		temp = []
		utilities.clear_folder('Words/')

	for f in range(0,len(sentences)):
		ltw.line_to_word(sentences[f])


	# Loading words from the folder
	words = []
	words = utilities.load_images_from_folder('Words/')

	#print(words)
	# Segmenting words into letters
	# Recognize the individual letters and form words
	# Use a spell checker to correct the recognised words
	# Words are appended to the text file specified
	
	for j in range(0,len(words)):
		wtl.word_to_letter(words[j])
		recognized_word  = recognize.get_word('Letters/')
		#print(recognized_word)
		if arg2 == 'Yes':
			recognized_word = spellcheck.correct_spelling(recognized_word)
		file.write(recognized_word + "\t")
		word_counter+=1
		if word_counter == int(no_of_words_per_sentence[sentence_counter]):
			file.write("\n")
			word_counter = 0
			sentence_counter+=1
		
		utilities.clear_folder('Letters/')

