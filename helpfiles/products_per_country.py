
# coding: utf-8

# In[8]:


import pandas as pd
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.io import output_file, show, save
import os


# In[38]:


# import dataset Foodprices
print(os.getcwd())

os.chdir("../")
os.chdir("datasets/preprocessed datasets/Food prices")
df_foodprices = pd.read_csv('Food_prizes_Africa_processed.csv')
os.chdir("../../")

print(os.getcwd())


# # Producten per land

# In[42]:


# laat zien welke producten er in een bepaald land te koop zijn voor een bepaalde input_data
def products_country(input_data, country):
    products = []
    fp_country = input_data.loc[input_data['adm0_name'] == country]
    products_total = fp_country['cm_name']
    product_list = products_total.tolist()
    for item in product_list:
        if item not in products:
            products.append(item)
    return(products)
products_country(df_foodprices, 'Mali')

