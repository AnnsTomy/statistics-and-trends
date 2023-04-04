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

def statistics_data(file_name, years, col, val):
    df = pd.read_csv(file_name, skiprows=4)
    df = df[df[col] == val]
    df = df[['Indicator Name'] + years]
    df = df.dropna(how='any')
    df = df.set_index('Indicator Name').T
    return df

# Specify the years and countries
years = ['1990', '1994', '1998', '2002','2006','2010']
countries = ['Austria', 'United States', 'Belgium','Australia']

# Create the two data frames
mort_pop = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Mortality rate, under-5 (per 1,000 live births)')
population = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Population, total')
# Create the two data frames
urban_population_t = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Urban population (% of total population)')
electric_power_t = st_world('D:\API_19_DS2_en_csv_v2_5346672.csv', years, countries, 'Indicator Name', 'Electric power consumption (kWh per capita)')
united_states = statistics_data("D:\API_19_DS2_en_csv_v2_5346672.csv", ['1990', '1994', '1998', '2002','2006','2010'], "Country Name", "United States")


print(mort_pop)
print(population)
print(urban_population_t)
print(electric_power_t)
print("United States\n", united_states)


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

x=["Population, total","Urban population","Energy use (kg of oil equivalent per capita)","Cereal yield (kg per hectare)"]
united_states = united_states.loc[:,x ]

print(united_states.corr())

corr = united_states.corr()

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(corr, cmap='coolwarm')

# Add correlation numbers on the heatmap
for i in range(len(x)):
    for j in range(len(x)):
        text = ax.text(j, i, round(corr.iloc[i, j],2), ha="center", va="center", color="black")

# Set tick labels and rotate x-axis tick labels
ax.set_xticks(np.arange(len(x)))
ax.set_yticks(np.arange(len(x)))
ax.set_xticklabels(x, fontsize=10)
ax.set_yticklabels(x, fontsize=10)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Add colorbar
cbar = ax.figure.colorbar(im, ax=ax, shrink=0.8)

# Set title and show plot
plt.title('Correlation Heatmap for United States', fontsize=14)
fig.tight_layout()
plt.show()

