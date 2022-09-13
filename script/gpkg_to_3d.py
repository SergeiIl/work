import geopandas as gpd
import matplotlib.pyplot as plt
import sqlite3 as sq
import pandas as pd
import time
import os
import numpy as np
import json
import shapely.wkt

# Загрузка данных из gpkg
gdf = gpd.read_file(r"C:\Users\il_sa\Desktop\test_for_3d_obj.gpkg", layer='total_building_pr')

for i in range(gdf.shape[0]):
    """
    Цикл создает геометрию в формате матрицы по каждому объекту.
    И делает 3д массив.
    """
    t = gdf.values[i][9]

    if t.geom_type == 'MultiPolygon':
        """Формируем лист из геометрий мультиполигона / создаются полигоны (имеют кольца)"""
        l = []
        for polygon in t.geoms:
            l.append(polygon)

        x_crd, y_crd = l[0].exterior.coords.xy  # вызвать геометрию из WKT и записать отдельно x и y

        t_np = np.transpose(np.vstack([x_crd, y_crd]))  # матрица координат объекта
        # t_np = np.array(list(zip(x_crd, y_crd))) # альтернативный вариант

        np_to_list = t_np.tolist()
        len(np_to_list)

        """Добавление координаты Z"""
        # z_crd = np.zeros(t_np.shape[0]).reshape(t_np.shape[0], 1)
        # ddd_np = np.hstack((t_np, z_crd))
        # print(ddd_np)

        """Визуализация полигонов"""
        # plt.title(gdf.T[i]["t_from_contents"])  # информация из колонки таблицы
        # plt.plot(t_np[:, 0], t_np[:, 1])
        # plt.show()