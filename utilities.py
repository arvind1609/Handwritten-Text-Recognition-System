import os


# Deletes all the files in the folder
# Input to clear_folder is the path of the folder
def clear_folder(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.png'):
            os.remove(folder + filename)
            #print(fname)
        elif filename.endswith('.txt'):
            os.remove(folder + filename)


# Loads all the .png files from the folder
# Input to load_images_from_folder is the path of the folder
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = os.path.join(folder,filename)
        if img is not None:
            images.append(img)
    return images


