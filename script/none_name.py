import pandas as pd
import os
import glob

data_path = r"D:\PyCharm\project\qgis_python_sql\data\moscow"
# data_path_eda = r"D:\PyCharm\project\qgis_python_sql\data\moscow\eda-cities"
files_moscow = glob.glob(os.path.join(data_path, '*.csv'))
# files_eda = glob.glob(os.path.join(data_path_eda, '*.csv'))
#all_files = []

# for filename in files_moscow:
#     all_files.append(filename)
#
# for filename in files_eda:
#     all_files.append(filename)

dfm = []

for filename in files_moscow:
    df = pd.read_csv(filename, index_col=None, header=0)
    dfm.append(df)

frame = pd.concat(dfm, axis=0, ignore_index=True)


frame.to_json('temp.json', orient='records', lines=True)