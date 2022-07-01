import geopandas as gpd
import matplotlib.pyplot as plt
import sqlite3 as sq
import pandas as pd
import time

# Загрузка данных из gpkg
start_time = time.time()
gpkg = gpd.read_file(r'all.gpkg', layer='all_obj')

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")
# Изменение формата на формат datatime
gpkg['created_at'] = pd.to_datetime(gpkg['created_at'])
# gpkg['week'] = gpkg['created_at'].dt.week
# gpkg['month'] = gpkg['created_at'].dt.month
# gpkg['year'] = gpkg['created_at'].dt.year

# Проверка уникальности значений
nunique = gpkg.nunique()

# Проверка пропущенных значений
isna = gpkg.isna().sum()

# График совершения событий во времени
gpkg['created_at'].hist(bins=50, figsize=(16, 6))
plt.title('Распределение кол-ва событий во времени')
plt.show()

end_time = time.time()
print(f"It took {end_time-start_time:.2f} seconds to compute")

