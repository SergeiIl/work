"""# -*- coding: utf-8 -*-"""

import os
import glob
import pandas as pd
import geopandas as gpd


data_path = r"D:\PyCharm\project\qgis_python_sql\data\moscow"
files = glob.glob(os.path.join(data_path, '*.csv'))

apu_src = r"+proj=tmerc +lat_0=55.66666666667 +lon_0=37.5 +k=1 +x_0=12 +y_0=14 +ellps=bessel +towgs84=316.151,78.924,589.65,-1.57273,2.69209,2.34693,8.4507 +units=m +no_defs"
wgs = "EPSG:4326"
val = 4326

df = pd.concat((pd.read_csv(f, index_col=None, header=0) for f in files))

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.location_longitude, df.location_latitude), crs=wgs)

gdf.to_file('moscow.gpkg', driver='GPKG', layer='moscow')
