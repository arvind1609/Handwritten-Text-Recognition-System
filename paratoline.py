import cv2
import os
import utilities
import numpy as np

def para_to_line(image_path):
	#import image
	image = cv2.imread(image_path)
	#cv2.imshow('orig',image)
	#cv2.waitKey(0)

	#grayscale
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#cv2.imshow('gray',gray)
	#cv2.waitKey(0)

	#binary
	ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
	#cv2.imshow('second',thresh)
	#cv2.waitKey(0)

	#dilation
	kernel = np.ones((5,100), np.uint8)
	img_dilation = cv2.dilate(thresh, kernel, iterations=1)
	#cv2.imshow('dilated',img_dilation)
	#cv2.waitKey(0)

	#find contours
	im2,ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	#sort contours
	sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
	count = len(utilities.load_images_from_folder('Sentences/'))

	for i, ctr in enumerate(sorted_ctrs):
	    # Get bounding box
	    x, y, w, h = cv2.boundingRect(ctr)

	    # Getting ROI
	    roi = image[y:y+h, x:x+w]
	    

	    # show ROI
	    #cv2.imshow('segment no:'+str(i),roi)
	    cv2.imwrite('Sentences/sentence'+ str(count)+ '.png',roi)
	    #cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2)
	    count = count + 1
	    #cv2.waitKey(0)

	#cv2.imshow('marked areas',image)
	#cv2.waitKey(0)

#para_to_line('C:/Users/thanga/Documents/Python/EMNIST_CNN_AUTOMATED/games.png')
#para_to_line('C:/Users/thanga/Documents/Python/EMNIST_CNN_AUTOMATED/meluha.png')