# Assign geographical coordinates to image
# V21.04.
import gdal
import osr
from additionalFunctions import additionalFunctions

af = additionalFunctions()
origPath = 'C:\School\\3333-53_1.tif'
imPath = 'C:\School\MasterThesis\python\paraugaDatiRegion\\'
names = ['citsRegion.tif', 'lauksRegion.tif', 'udensRegion.tif', 'zaliensRegion.tif', 'kokiRegion.tif']
for n in names:
    imd = gdal.Open(imPath + n)
    imb = imd.GetRasterBand(1)
    im = imb.ReadAsArray()
    imd1 = gdal.Open(origPath)  # Open TIFF
    geot = imd1.GetGeoTransform()  # GeoTrans data
    # print(geot)
    Projection = osr.SpatialReference()
    Projection.ImportFromWkt(imd1.GetProjectionRef())
    EPSG = (Projection.GetAttrValue("AUTHORITY", 1))  # Get EPSG
    rasterOrigin = [geot[0], geot[3]]
    af.array2raster(imPath + 'G' + n, rasterOrigin, geot[1], geot[5], im, 1, gdal.GDT_UInt16, 3059)
