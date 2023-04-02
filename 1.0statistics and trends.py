# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 02:52:21 2023

@author: Anns Tomy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_world_bank(file_name):
    df_world = pd.read_csv(file_name, skiprows=4, index_col=0)
    df_world = df_world.dropna(how='all').dropna(axis=1, how='all')
    df_world = df_world.drop(['Country Code', 'Indicator Code'], axis=1)
    df_world = df_world.rename(columns={'Indicator Name': 'Indicator'})
    # Add groupby function here
    groupby_indicator = df_world.groupby(['Indicator'])
    groupby_country = df_world.groupby(['Country Name'])
    df_world_t = df_world.T
    return df_world, df_world_t, groupby_indicator, groupby_country

def st_world(file_name, years, countries, col, val1):
    df_world_data = pd.read_csv(file_name, skiprows=4)
    df_world_data = df_world_data[df_world_data[col] == val1]
    df_world_data = df_world_data.loc[df_world_data['Country Name'].isin(countries), ['Country Name', 'Indicator Name'] + years].dropna()
    df_world_data = df_world_data.set_index(['Country Name', 'Indicator Name']).T
    return df_world_data

# Read in the data and groupby objects
df_world, df_world_t, groupby_indicator, groupby_country = read_world_bank('D:\API_19_DS2_en_csv_v2_5346672.csv')
print(df_world)

# Specify the years and countries
years = ['1960', '1961', '1962', '1963','1964','1965']
countries = ['India', 'United States', 'China','Aruba','India']

# Create the data frames
urban_pop = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Urban population (% of total population)')
population = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Population, total')
