import geopandas as gpd
import matplotlib.pyplot as plt
import sqlite3 as sq
import pandas as pd

gpkg = gpd.read_file(r'moscow.gpkg', layer='moscow').head(1000)
gpkg['created_at'] = pd.to_datetime(gpkg['created_at'])