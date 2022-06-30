# test_data = gpkg.head(1000)
# test_data.plot()
# plt.show()

# conn = sq.connect(r'moscow.gpkg')
#
# sql_query = "SELECT * " \
#             "FROM moscow " \
#             "LIMIT 1000;"
# cur = conn.cursor()
# cur.execute(sql_query)
# result = cur.fetchall()
# gdf = gpd.GeoDataFrame(result)

# pd.read_sql(sql_query,conn)