import scipy.io as sio
from scipy import ndimage
import numpy
from PIL import Image

cits = numpy.array(Image.open('testData/GcitsRegion.tif'))
origIm = numpy.array(Image.open('C:\\School\\3333-53_1.tif'))

Image.fromarray(cits).show()



# for regionNr in numpy.unique((cits[numpy.nonzero(cits)])):


# citsRegion = sio.loadmat('testData/citsViss.mat')['cits']
# print(numpy.amax(citsRegion))
