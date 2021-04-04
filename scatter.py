import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt
# col = ['latitude', 'longitude', 'FIPS']
# col2 = ['FIPS Code', 'Percent of adults completing four years of college or higher, 1970', 'Percent of adults completing four years of college or higher, 1980', "Percent of adults with a bachelor's degree or higher, 1990",
#         "Percent of adults with a bachelor's degree or higher, 2000", "Percent of adults with a bachelor's degree or higher, 2015-19"]

# df = pd.read_csv('bffips.csv', usecols = col).groupby("FIPS").count()
# df2 = pd.read_csv('Educationn.csv')
# print(df2.describe())
# print(df2.columns)
# print(df.describe())
# # df2.iloc[:,-1] = df2.iloc[:,-1].astype('float')
# df3 = df.merge(df2, how= 'inner', left_on = 'FIPS', right_on = 'FIPS Code')
# df3["Average percent of bachelor's degree"] = df3[3:].sum(axis = 1)
# print(df3)
# plt.scatter(df3['Average_bachelors_education'], df3["latitude"])
# plt.show()

df3 = pd.read_csv('county_data.csv')
print(df3)

