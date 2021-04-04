# import plotly.figure_factory as ff
#
# import numpy as np
import pandas as pd
#
df = pd.read_csv('bffips.csv')
#
# print(df)
#
df2 = df.groupby('FIPS').size()
print(df2)
# # df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
# # df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
# # df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
# # df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']
#
# # colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
# #     "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
# #     "#08519c", "#0b4083", "#08306b"
# # ]
# # endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df2.index.tolist()[1:]
print(fips)
values = df2.values.tolist()[1:]
print(values)
#
# fig = ff.create_choropleth(
#     fips=fips, values=values, scope=['usa'],
#     # binning_endpoints=endpts, colorscale=colorscale,
#     show_state_data=True,
#     show_hover=True,
#     asp = 2.9,
#     title_text = 'Sightings Per County',
#     legend_title = 'Number of Sightings'
# )
# fig.layout.template = None
# fig.show()


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
# print(counties)
fipslst = []
for i in counties['features']:
    # print(i['properties'])
    fipslst.append(i['properties']['STATE'] + i['properties']['COUNTY'])
print(fipslst)
import numpy as np
df4 = pd.DataFrame({'Fips' : fipslst, 'count' : np.zeros(len(fipslst))})
# df4['count'] = pd.Series('0')
print(df4)
for i in df4.index:
    for j in df2.index:
        # print(i, j)
        if df4.iloc[i]['Fips'] == j:
            df4.iloc[i]['count'] = df2[j]
print(df4)
df4.to_csv('countysightings.csv')
# import pandas as pd
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
#                    dtype={"fips": str})
# print(counties)
import plotly.express as px

# df2['fips'] = df2.index
# print(df2)
# fig = px.choropleth(df2, geojson=counties, locations= fips, color=values,
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 62),
#                            scope="usa",
#                            labels={'latitude':'Number of sightings'}
#                           )
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()
