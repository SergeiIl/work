"""# -*- coding: utf-8 -*-"""

import os
import glob

# Указываем путь, где расположены объединяемые файлы, создаем их список
data_path_multi = r"C:\Users\il_sa\Desktop\_IO_\start_file\coordinates\multi"
files_multi = glob.glob(os.path.join(data_path_multi, '*.json'))

text_start_multi = '{"type":"FeatureCollection","metadata":{"name":"IO","creator":"ILSA"},"features":[{"type":"Feature","id":0,"geometry":{"type":"Polygon","coordinates":'
text_end_multi = '},"properties":{"description":"hello", "file_name":"test"}}]}'

for f in files_multi:
    with open(f) as fls:
        coord = fls.read()
        gjson = text_start_multi + coord + text_end_multi
        my_file = open(f.replace('json', 'geojson'), 'w')
        my_file.write(gjson)
        my_file.close()