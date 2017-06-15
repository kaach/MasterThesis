import os
import glob

folder = 'C:\\Users\\katrina.zvaigzne\\OneDrive\\MasterThesis\\jseg-python\\visiRegioni\\test\\'
for file in glob.glob(folder + '*.jpg'):
    regionNr = os.path.splitext(os.path.basename(file))[0]
    if len(regionNr) < 5:
        newName = (5 - len(regionNr)) * '0' + regionNr + '.jpg'
        os.rename(file, folder + newName)
