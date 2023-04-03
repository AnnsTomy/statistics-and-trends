# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:14:35 2023

@author: Anns Tomy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def st_world(file_name, years, countries, col, val1):
    df_world_data = pd.read_csv(file_name, skiprows=4)
    df_world_data = df_world_data[df_world_data[col] == val1]
    df_world_data = df_world_data.loc[df_world_data['Country Name'].isin(countries), ['Country Name', 'Indicator Name'] + years].dropna()
    df_world_data_t = df_world_data.set_index(['Country Name', 'Indicator Name']).T
    return df_world_data, df_world_data_t

# Specify the years and countries
years = ['1960', '1962', '1964', '1966','1968','1970']
countries = ['Austria', 'United States', 'Belgium','Australia']

# Create the two data frames
mort_pop = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Mortality rate, under-5 (per 1,000 live births)')
population = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Population, total')
# Create the two data frames
urban_population_t = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Urban population (% of total population)')
electric_power_t = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Electric power consumption (kWh per capita)')

print(mort_pop)
print(population)
print(urban_population_t)
print(electric_power_t)

# Plot the Mortality rate dataframe against years
ax = mort_pop[1].plot(figsize=(10,5), title='Mortality rate, under-5 (per 1,000 live births)')
ax.set_xlabel('Years')
ax.set_ylabel('Mortality rate')

# Plot the Population dataframe against years
ax = population[1].plot(figsize=(10,5), title='Population, total')
ax.set_xlabel('Years')
ax.set_ylabel('Population')

#plot the Urban population against years
urban_population_t[1].plot(kind='bar')

#plot the electric power consumption against years
electric_power_t[1].plot(kind='bar')
