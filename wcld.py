# import pandas as pd
# #
# # import streamlit as st
# #
# # pd.set_option('display.max_rows', 500)
# # pd.set_option('display.max_columns', 500)
# # pd.set_option('display.width', 1000)
# # columns = 'latitude,longitude,date,classification,moon_phase'.split(',')
# df = pd.read_pickle('county_labels.pkl')
# # # st.map(df)
# print(df)
# import plotly.figure_factory as ff
#
# # fips = ['06021', '06023', '06027',
# #         '06029', '06033', '06059',
# #         '06047', '06049', '06051',
# #         '06055', '06061']
# values = range(len(df))
#
# fig = ff.create_choropleth(fips=df[:1000]['fips'], values=values)
# fig.layout.template = None
# fig.show()

import pandas as pd
import datetime
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image, ImageColor
import numpy as np
import os
# df = pd.read_csv('bigfoot.csv')
text = open('obs.txt', 'r', encoding='utf-8', errors='ignore').read()
# print(df.index)

# df['observed'] = df['observed'].astype(str)
# for i in df.index:
#     # print(i)
#     # print(str(df.loc[i]['observed']))
#     text = text + " " + df.loc[i]['observed']
# with open('obs.txt', 'w',encoding='utf-8', errors='ignore') as file:
#     file.write(text)
mask_fname = np.array(Image.open('new.png'))



wc = WordCloud(background_color= 'white',
         mask = mask_fname,
         contour_width = 0,
         contour_color = 'black').generate(text)

image = wc.to_image()
image.show()
