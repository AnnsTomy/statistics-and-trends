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

# Transpose dataframe
mort_pop_t = mort_pop[1].transpose()

ax = mort_pop_t.plot(figsize=(20,10))
ax.set_xlabel('Country')
ax.set_ylabel('Mortality rate')
ax.set_title('Mortality rate, under-5 (per 1,000 live births)')


# Transpose dataframe
population_t = population[1].transpose()

ax = population_t.plot(figsize=(20,15))
ax.set_xlabel('Country')
ax.set_ylabel('Mortality rate')
ax.set_title('Mortality rate, under-5 (per 1,000 live births)')


urban_population_t[1].plot(kind='bar')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Urban population of different countries')
plt.xlabel("Years")
plt.ylabel('Urban population (% of total population)')
plt.show()

electric_power_t[1].plot(kind='bar')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.title('Electric power consumption (kWh per capita) of different countries')
plt.xlabel("Years")
plt.ylabel('Electric power consumption (kWh per capita)')
plt.show()
