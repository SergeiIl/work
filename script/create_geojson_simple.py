"""# -*- coding: utf-8 -*-"""

import os
import glob

# Указываем путь, где расположены объединяемые файлы, создаем их список
data_path_simple = r"C:\Users\il_sa\Desktop\_IO_\start_file\coordinates\simple"
files_simple = glob.glob(os.path.join(data_path_simple, '*.json'))

# в начале координат должно быть 3 квадратных кавычки, потому добавляем две в start и end
text_start_simple = '{"type":"FeatureCollection","metadata":{"name":"IO","creator":"ILSA"},"features":[{"type":"Feature","id":0,"geometry":{"type":"Polygon","coordinates":['
text_end_simple = ']},"properties":{"description":"hello", "file_name":"test"}}]}'

for f in files_simple:
    with open(f) as fls:
        coord = fls.read()
        gjson = text_start_simple + coord + text_end_simple
        my_file = open(f.replace('json', 'geojson'), 'w')
        my_file.write(gjson)
        my_file.close()
