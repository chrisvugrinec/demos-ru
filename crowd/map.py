import numpy as np
import geopandas as gpd
from shapely.geometry import LineString

gdf = gpd.read_file('data/edges.shp') 

gdf = gpd.GeoDataFrame(gdf)

pt = list(gdf.geometry)

ptx = [list(x.coords) for x in pt]

pt_array = np.concatenate(ptx)
# print(pt_array)

# TO DO convert array to repast4py network