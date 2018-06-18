
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import os

print(os.getcwd())
# controleer altijd of je in de map helpfiles zit


# In[3]:


from select_df import select_df

df_foodprices = select_df(1, 'foodprices')
df_migration = select_df(1, 'migration_movements')
df_weather = select_df(1, 'temperature_and_precipitation')


# ## Normalize function

# In[17]:


# normaliseer de data van een speciefieke kolom naar waardes tussen 0 en 1.

def normalize(input_data, column):
    values = []
    
    for value in input_data[column]:
         values.append(value)
            
    Min = min(values)
    Max = max(values)
        
    output_data = []
    for value in input_data[column]:
        output_data.append((value - Min)/(Max - Min))
    
    input_data['Normalized_data'] = output_data
    
    return input_data


# # Plot migration movements

# In[22]:

# selecteer voor een #input_data de #origin vanaf #year1 tot en met #year2

def select_plot_migration_movements(input_data,origin, year1, year2):
    input_data = input_data.loc[input_data['Origin'] == origin]
    input_data = input_data.loc[(input_data['Timestamp'] > year1) & (input_data['Timestamp'] < year2)]
    return input_data


# checks if a product is in the foodprices dataset, if not, it returns a list of all available products in a given country
def check_product_in_foodprices(set_country, set_product, foodprices):
    
    set_product = '-' + set_product
    product_list = []
    for product in foodprices.loc[foodprices['adm0_name'] == set_country]['cm_name']:
        if '-' + product not in product_list:
            product_list.append('-' + product)

    d = {'Product_List' : product_list}

    df = pd.DataFrame(data=d)    
    
    if not set_product in product_list:
        print('Error, product not recognized. Choose a product from the list below')
        return df
    else:
        return 'Succesfully imported values!'

# # Plot temperature and precipitation

# In[21]:


# geeft voor een #input_data van een #country de pr en tas vanaf #year1 tot en met #year2

def select_plot_temperature_and_precipitation(input_data, country, year1, year2):
    saved_dict = {'Mauritania': 'MRT', 'Lesotho': 'LSO', 'Somalia': 'SOM', 'Nigeria': 'NGA', 'Tanzania': 'TZA', 'Zambia': 'ZMB', 'Burundi': 'BDI', 'Afghanistan': 'AFG', 'Mali': 'MLI', 'Niger': 'NER', 'Malawi': 'MWI', 'Congo': 'ZAR', 'Cabo Verde': 'CPV', 'Sudan': 'SDN', 'Pakistan': 'PAK', 'Burkina Faso': 'BFA', 'Rwanda': 'RWA', 'Kenya': 'KEN', 'Senegal': 'SEN', 'Cameroon': 'CMR', 'Sierra Leone': 'SLE', 'Iraq': 'IRQ', 'Uganda': 'UGA', 'Mozambique': 'MOZ', 'Zimbabwe': 'ZWE', 'Central African Republic': 'CAF', 'Ethiopia': 'ETH', 'Guinea': 'GIN', 'Liberia': 'LBR', 'Djibouti': 'DJI', 'Iran': 'IRN', 'Madagascar': 'MDG', 'Lebanon': 'LBN'}

    if country in saved_dict.keys():
        country = saved_dict[country]
    else:
        print("Please enter correct country name")
    
    input_data = pd.DataFrame(input_data.loc[input_data['country'] == country])
    input_data = input_data.loc[(input_data['year'] > year1 - 1) & (input_data['year'] < year2 + 1)]
    
#     maak van de jaren en maanden kommajaren
    YearMonth = []
    month = []
    for row in input_data['month']:
        month.append(str(row))
        
    count = 0
    for year in input_data['year']:
        year = int(year) + (int(month[count])  - 1)/ 12
        YearMonth.append(year)
        count += 1
    input_data['YearMonth'] = YearMonth
    input_data = input_data[['pr', 'tas', 'country', 'YearMonth']]
    return input_data

# werking
# select_plot_temperature_and_precipitation(df_weather, 'Mauritania', 1985, 2030)


# # Plot foodprices per market

# In[23]:


def select_plot_foodprices_per_market(input_data, country, product, year1, year2):
    input_data = input_data.loc[input_data['adm0_name'] == country]
    input_data = input_data.loc[input_data['cm_name'] == product]
    input_data = input_data.loc[(input_data['Year'] >= year1) & (input_data['Year'] < year2 + 1)]
    return input_data

# werking
# select_plot_foodprices_per_market(df_foodprices, 'Burkina Faso', 'Maize', 2004, 2004)


# In[25]:


# berekend de gemiddelde voedselprijzen van een product in een land

def select_plot_foodprices_average(input_data, country, product, year1, year2):
    input_data = select_plot_foodprices_per_market(input_data, country, product, year1, year2)
    
    country_list = []
    product_list = []
    average_price_list = []
    year_list = []
    
    for i in range(year1, year2 + 1):
        for j in range(12):
#             Selecteer een specifieke maand in een jaar
            output_data = input_data.loc[input_data['mp_year'] == i]
            output_data = output_data.loc[output_data['mp_month'] == j + 1]
#         maak een nieuwe rij wanneer er data beschikbaar is
            if len(output_data['mp_price']) > 0:
#                 year
                year_list.append(i + (j / 12))

#                 country
                country_list.append(country)

#                 product
                product_list.append(product)
#                 average data            
                average_price_list.append(sum(output_data['mp_price']) / len(output_data['mp_price']))

    
    output_data = pd.DataFrame()    
    output_data['country'] = country_list
    output_data['year'] = year_list
    output_data['product'] = product_list
    output_data['average_price'] = average_price_list
    return output_data

# werking
# select_plot_foodprices_average(df_foodprices, 'Burkina Faso', 'Maize', 2004, 2006)

def possible_range(data1, data2):
    # bepaal de range van dataset 1 (migration movements)
    min1 = float(data1.head(1))
    max1 = float(data1.tail(1))
    # bepaal de range van dataset 2 (foodprices average)
    min2 = float(data2.head(1))
    max2 = float(data2.tail(1))

    # bepaal de mogelijke combinatie range
    if min1 >= min2: year_min = int(np.ceil(min1))
    else: year_min = int(np.ceil(min2))
    if max1 <= max2: year_max = int(np.ceil(max1))
    else: year_max = int(np.ceil(max1))
        
    return(year_min, year_max)

# werking
# data1 = select_plot_migration_movements1(df_migration, 'Zimbabwe', 1990, 2018)['Timestamp']
# data2 = select_plot_foodprices_average(df_foodprices, 'Zimbabwe', 'Cowpeas', 1990, 2018)['year']
# possible_range(data1, data2)