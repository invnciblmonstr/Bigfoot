import pandas as pd
import datetime
import streamlit as st
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
columns = 'latitude,longitude,date,classification,moon_phase'.split(',')
df = pd.read_csv('bigfoot.csv')
print(len(df[df['moon_phase'].notna()]))
data = df[columns]
data = data.dropna(subset=['latitude', 'longitude'])
data['date'] = data['date'].str.replace('/','-')
data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True)
data = data.set_index(data['date'])

for i in data['date']:
    if i.year> 2018:
        data.loc[i,'date'] = datetime.datetime(i.year-100, i.month, i.day)

data = data.set_index(data['date'])
data = data.sort_index()
data['1921':].resample('Y').count().max()
newdf = data['classification'].resample('Y').count().sort_values()
newdf['1921':].plot()
plt.show()


