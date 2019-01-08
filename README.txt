Requirements (recommended):
•	Python 3.5
•	Tensorflow 1.8
•	Keras 2.1.6
•	Pillow(PIL), cv2, numpy, matplotlib, pandas, os, pyspellchecker

Description of files:
•	paratoline.py- Segment paragraph into lines and save it into the respective folder.
•	linetoword.py- Segment line into words and save it into the respective folder.
•	wordtoletter.py- Segment word into letters and save it into the respective folder.
•	imageprep.py- Pre-process the image before prediction.
•	recognize.py- Load the model and predict the label of the image.
•	utilities.py- Contains functions for file manipulation inside folders.
•	spellcheck.py- Correct the recognised word.
•	index.py- Main file which enables all the functionalities.
•	training_emnist.ipynb- Jupyter notebook file to train the dataset to your specification.
NOTE: Kernel sizes in paratoline.py, linetoword.py, wordtoletter.py need to be tuned based on user handwriting. If necessary, you can combine these files into a single function with kernel values as inputs. Change the path of the dataset in .ipynb before training.

How to run:
Go to the directory
“ python index.py <path of folder with images of documents> <spell-checker> “
Spell-checker takes values – ‘Yes’ or ‘No’
