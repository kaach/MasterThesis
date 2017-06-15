from qgis.analysis import QgsZonalStatistics

#specify polygon shapefile vector
folder = 'C:/School/MasterThesis/polyRegions/'
#pathes = ['polyCits/polyCits.shp','polyKoki/polyKoki.shp','polyLauks/polyLauks.shp','polyUdens/polyUdens.shp','polyZaliens/polyZaliens.shp']
pathes=['polyViss/polyViss.shp']
rasterFilePath = 'C:/School/3333-53_1.tif'
bands = ["R","G","B"]
for path in pathes:
    polygonLayer = QgsVectorLayer(folder+path, 'polygon', "ogr") 
    for i in range(1,4):
        zoneStat = QgsZonalStatistics (polygonLayer, rasterFilePath, bands[i-1], i,QgsZonalStatistics.Count | QgsZonalStatistics.Mean | QgsZonalStatistics.Median | QgsZonalStatistics.StDev)
        zoneStat.calculateStatistics(None)