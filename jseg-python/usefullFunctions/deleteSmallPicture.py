import os
import glob

from PIL import Image

folder = 'C:\\Users\\katrina.zvaigzne\\OneDrive\\MasterThesis\\jseg-knn\\paraugaDati\\cits\\'
for file in glob.glob(folder + '*.jpg'):
    with Image.open(file) as image:
        x, y = image.size
    if x * y < 80:
        os.remove(file)
