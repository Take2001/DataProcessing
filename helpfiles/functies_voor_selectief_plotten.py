# selecteer voor een #input_data de #country_of_residence vanuit een bepaalde #origin vanaf #year1 tot en met #year2

def select_plot_migration_movements(input_data, country_of_residence, origin, year1, year2):
    input_data = input_data.loc[input_data['Country of residence'] == country_of_residence]
    if input_data.empty == True:
        return('Error: Country of residence: {} is not included in DataFrame!'.format(country_of_residence))
    input_data = input_data.loc[input_data['Origin'] == origin]
    if input_data.empty == True:
        return('Error: Origin: {} is not included in DataFrame!'.format(country_of_residence))
    input_data = input_data.loc[(input_data['YearMonth'] > year1) & (input_data['YearMonth'] < year2 + 1)]
    return input_data

select_plot_migration_movements(df_migration, 'Netherlands', 'Zimbabwe', 2000, 2012)


# # Plot temperature and precipitation

# In[19]:


# geeft voor een #input_data van een #country de pr en tas vanaf #year1 tot en met #year2

def select_plot_temperature_and_precipitation(input_data, country, year1, year2):
    saved_dict = {'Mauritania': 'MRT', 'Lesotho': 'LSO', 'Somalia': 'SOM', 'Nigeria': 'NGA', 'Tanzania': 'TZA', 'Zambia': 'ZMB', 'Burundi': 'BDI', 'Afghanistan': 'AFG', 'Mali': 'MLI', 'Niger': 'NER', 'Malawi': 'MWI', 'Congo': 'ZAR', 'Cabo Verde': 'CPV', 'Sudan': 'SDN', 'Pakistan': 'PAK', 'Burkina Baso': 'BFA', 'Rwanda': 'RWA', 'Kenya': 'KEN', 'Senegal': 'SEN', 'Cameroon': 'CMR', 'Sierra Leone': 'SLE', 'Iraq': 'IRQ', 'Uganda': 'UGA', 'Mozambique': 'MOZ', 'Zimbabwe': 'ZWE', 'Central African Republic': 'CAF', 'Ethiopia': 'ETH', 'Guinea': 'GIN', 'Liberia': 'LBR', 'Djibouti': 'DJI', 'Iran': 'IRN', 'Madagascar': 'MDG', 'Lebanon': 'LBN'}

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

select_plot_temperature_and_precipitation(df_weather, 'Mali', 1990, 2030)


# # Plot foodprices per market

# In[20]:


def select_plot_foodprices_per_market(input_data, country, product, year1, year2):
    input_data = input_data.loc[input_data['adm0_name'] == country]
    input_data = input_data.loc[input_data['cm_name'] == product]
    input_data = input_data.loc[(input_data['Year'] >= year1) & (input_data['Year'] < year2 + 1)]
    return input_data

select_plot_foodprices_per_market(df_foodprices, 'Burkina Faso', 'Maize', 2004, 2004)


# In[21]:


# 

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
            else:
                print('ERROR: Geen data beschikbaar over het jaar', i + j/12)
    
    output_data = pd.DataFrame()    
    output_data['country'] = country_list
    output_data['year'] = year_list
    output_data['product'] = product_list
    output_data['average_price'] = average_price_list
    return output_data

select_plot_foodprices_average(df_foodprices, 'Burkina Faso', 'Maize', 2004, 2006)    


# # Plot functies

# In[22]:


from bokeh.plotting import figure
from bokeh.io import output_file, show, save
import pandas

def plot_line_difference(country, product, year1, year2):
    # Make sure x and y are of the same length.
    x1 = select_plot_foodprices_average(df_foodprices, country, product, 2004, 2014)['year'] 
    y1 = select_plot_foodprices_average(df_foodprices, country, product, 2004, 2014)['average_price']  

    x2 = select_plot_temperature_and_precipitation(df_weather, country, 2004, 2014)['YearMonth']    
    y2 = select_plot_temperature_and_precipitation(df_weather, country, 2004, 2014)['tas']    

#     output_file("Line.html")

    f = figure(plot_width=1500, plot_height=600)

    # Plot the line
    f.line(x1, y1, color='red')
    f.line(x2, y2, color='blue')

    show(f)

plot_line_difference('Mali', 'Maize', 2002, 2010)

