import numpy as np
import keras
from keras.models import load_model
import utilities
import imageprep

# Load pre-trained Model
emnist_model = load_model('keras_emnist.h5')

# Function to recognize words
def get_word(path_to_letters):
	# Dictionary to match predicted label with our class
	character_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C',
                 13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 25:'P',
                 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z', 36:'a', 37:'b', 38:'c',
                 39:'d', 40:'e', 41:'f', 42:'g', 43:'h', 44:'i', 45:'j', 46:'k', 47:'l', 48:'m', 49:'n', 50:'o', 51:'p',
                 52:'q', 53:'r', 54:'s', 55:'t', 56:'u', 57:'v', 58:'w', 59:'x', 60:'y', 61:'z'}
	predictionlist = []
	all_images = utilities.load_images_from_folder(path_to_letters)
	
	converted_list = []
	# Preparing the image extracted
	# Images are similar to trained images after this process
	for i in range(0,len(all_images)):
	    image = imageprep.image_prepare(all_images[i])
	    image = np.reshape(image,(28,28,1))
	    img = np.fliplr(image)
	    img = np.rot90(img)
	    converted_list.append(img)

	converted_images = np.asarray(converted_list)
	predictions = emnist_model.predict_classes(converted_images)
	word = []
	for i in range(0,len(predictions)):
	    temp = character_dict[int(predictions[i])]
	    word.append(temp)
	answer = ''.join([str(x) for x in word])
	return answer