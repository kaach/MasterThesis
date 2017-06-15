import os
import glob
import csv

folder = 'C:\\School\\MasterThesis\\Tensorflow\\image_retraining\\dalaParaugaDatu\\udens\\'
fileName = 'udens.csv'
for file in glob.glob(folder + '*.jpg'):
    regionNr = os.path.splitext(os.path.basename(file))[0]
    with open(fileName, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([regionNr])
