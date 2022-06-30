import geopandas as gpd
import matplotlib.pyplot as plt

gpkg = gpd.read_file(r'moscow.gpkg', layer='moscow')
test_data = gpkg.head(1000)
test_data.plot()
plt.show()