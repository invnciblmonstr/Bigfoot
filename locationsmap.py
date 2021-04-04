import geopandas
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
world = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))
# print(world)

counties = pd.read_csv("bigfoot.csv", index_col=0).dropna(subset=['latitude', 'longitude'])
# print(counties)
counties = geopandas.GeoDataFrame(counties, crs="EPSG:4326",
                                geometry=geopandas.points_from_xy(counties.longitude, counties.latitude))
print(counties)
usa = world[world.iso_a3 =="USA"]
print(usa)
# usa_capitals = cities[cities.country.isin(samerica.name) & (cities.capital=="primary")]
# samerica_cities = cities[cities.country.isin(samerica.name) & (cities.capital!="primary") &
#                              (cities.population > 100000)].copy()
#
# def city_marker_size(df):
#     if df.population <= 250000:
#         return 10
#     elif 250000 < df.population < 10**6:
#         return 30
#     elif 10**6 < df.population < 2.5*10**6:
#         return 70
#     else:
#         return 100
#
# samerica_cities.loc[:,'marker_size'] = samerica_cities.apply(city_marker_size, axis=1)
#
fig, ax = plt.subplots(figsize=(8,14))

fig.set_facecolor('lightblue')
usa.plot(ax = ax, cmap='summer', alpha=.8, edgecolor='black')
#
# samerica.apply(lambda x: ax.annotate(text=x['name'].upper(), xy = x.geometry.centroid.coords[0], alpha=.5,
#                                      color='white', fontname='Silom', fontsize=16, ha = 'center'), axis=1)
#
# samerica_cities.plot(ax=ax, markersize=samerica_cities.marker_size, color='black', label='City')
counties.plot(ax=ax, markersize=15, marker="o", color="gold", label='Capital')

ax.set_title("Cities of South America", fontsize=22)

ax.legend()
ax.axis('off')
plt.show()
#
# fig.savefig('southamerica.png', dpi=128, bbox_inches='tight')
