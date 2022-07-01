"""# -*- coding: utf-8 -*-"""

import os
import glob
import pandas as pd
import geopandas as gpd

# Указываем путь, где расположены объединяемые файлы, создаем их список
data_path = r"D:\PyCharm\project\qgis_python_sql\data\moscow"
files = glob.glob(os.path.join(data_path, '*.csv'))

# Параметры проекций для работы
apu_src = r"+proj=tmerc +lat_0=55.66666666667 +lon_0=37.5 +k=1 +x_0=12 +y_0=14 +ellps=bessel +towgs84=316.151,78.924," \
          r"589.65,-1.57273,2.69209,2.34693,8.4507 +units=m +no_defs "
wgs = "EPSG:4326"
val = 4326

# Генератор, который объединяет все csv файлы в один датафрейм
df = pd.concat((pd.read_csv(f, index_col=None, header=0) for f in files))

# Преобразуем датафрейм в геодатафрейм
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.location_longitude, df.location_latitude), crs=wgs)

# Сохраняем в gpkg
gdf.to_file('all.gpkg', driver='GPKG', layer='all')

# Сохраняем в GeoJSON
# gdf.to_file('dataframe.geojson', driver='GeoJSON')