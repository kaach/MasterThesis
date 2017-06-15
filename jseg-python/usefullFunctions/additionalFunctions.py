import os
import sys
import glob
import gdal
import ogr
import numpy 
from osgeo import osr, ogr
class additionalFunctions:
#Usage example rasterOrigin=(392089.5,6345184)
	# af.array2raster("U:\\DataSets\\LatvianStudySite\\TreeDelineation\\testArea.tif",rasterOrigin,0.5,-0.5,im,1,gdal.GDT_Float32,3059)
	def array2raster(self,newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array,bands,type,epsg):
		cols = array.shape[1]
		rows = array.shape[0]
		originX = rasterOrigin[0]
		originY = rasterOrigin[1]
		driver = gdal.GetDriverByName('GTiff')
		outRaster = driver.Create(newRasterfn, cols, rows, bands, type)
		outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
		if bands==1:
			print "Writing array to tiff"
			outband = outRaster.GetRasterBand(1)
			outband.WriteArray(array)
		else:
			for i in range(0, bands):
				temparr=array[:,:,i]
				outband=outRaster.GetRasterBand(i + 1)
				outband.WriteArray(temparr)
		outRasterSRS = osr.SpatialReference()
		outRasterSRS.ImportFromEPSG(epsg)
		outRaster.SetProjection(outRasterSRS.ExportToWkt())
		outband.FlushCache()