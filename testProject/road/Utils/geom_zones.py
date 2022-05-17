

# from django.contrib.gis.geos import GEOSGeometry 
# Tehran = GEOSGeometry(srid=4326,geo_input=)

import shapefile
sf = shapefile.Reader("road/Utils/gadm40_IRN_shp.zip")
TEHRAN_GEOM = ...
TOLL_1 = ...