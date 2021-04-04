import pandas as pd
import datetime
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image, ImageColor
import numpy as np
import os
import geopandas
import matplotlib.colors as colors
from collections import Counter
df1 = pd.read_pickle('county_labels.pkl')


bf = pd.read_csv('bigfoot.csv')

counties = geopandas.read_file('cb_2018_us_county_5m.shp')
counties
not_needed = '02 15 78 72 60 66 69'

for i in not_needed.split():
    counties = counties[counties.STATEFP != i]
counties['fips'] = counties['STATEFP'].astype(str) + counties['COUNTYFP'].astype(str)
bigfoot_geo = geopandas.GeoDataFrame(bf, crs="EPSG:4326",
                                geometry=geopandas.points_from_xy(bf.longitude, bf.latitude))
from shapely.ops import cascaded_union
usa = geopandas.GeoSeries(cascaded_union(counties.geometry))
in_usa = [sighting.within(usa.geometry[0]) for sighting in bigfoot_geo.geometry]
bf = bf[in_usa]

for sighting in bf.index:
    is_in_county = [bf.geometry[sighting].within(poly) for poly in counties.geometry]
    county = str(counties[is_in_county].fips.values)
    bf.loc[sighting, 'county'] = counties[is_in_county].fips.values

sighting_by_county = Counter(bf.county)
counties['sightings'] = [sighting_by_county[county] for county in counties.fips]


fig, ax = plt.subplots(figsize=(18, 18))
counties.plot(ax=ax,column = 'sightings',cmap = 'Viridis', edgecolor='ghostwhite')
# bf.plot(ax=ax, color="black", markersize=6, marker='.', alpha=.7)
ax.axis('off')

plt.show()
