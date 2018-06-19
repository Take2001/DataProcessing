import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.io import output_file, show, save
from bokeh.models import DataRange1d, PanTool, ResetTool, WheelZoomTool, HoverTool, LassoSelectTool, BoxSelectTool, SaveTool, Legend

os.chdir("../../")
os.chdir("helpfiles/select_df")

print(os.getcwd()) 
from select_df import select_df
from functies_voor_selectief_plotten import *

os.chdir("../")
os.chdir("plotted comparisons/html plots")

foodprices = select_df(2,'foodprices')
migration_movements = select_df(2,'migration_movements')
temperature_and_precipitation = select_df(2,'temperature_and_precipitation')

# set datasets you want to compare
dataset1 = 'foodprices'
dataset2 = 'migration_movements'

set_country = sys.argv[1]
set_product = sys.argv[2]
set_year1 = sys.argv[3]
set_year2 = sys.argv[4]

# create figure and it's layout
f = figure()
f = figure(plot_width=1000, plot_height=650)
f.background_fill_color="lightblue"
f.background_fill_alpha=0.1

if dataset1 == 'foodprices':
    x_as = normalize(select_plot_foodprices_average(foodprices, set_country, set_product, 1999, 2017), 'average_price')
    f.xaxis.axis_label="Price of {}".format(set_product)

elif dataset1 == 'migration_movements':
    x_as = normalize(select_plot_migration_movements1(migration_movements, set_country, 1999, 2017), 'Value')
    f.xaxis.axis_label="Amount of refugees in {}".format(set_country)


if dataset2 == 'foodprices':
    y_as = normalize(select_plot_foodprices_average(foodprices,set_country, set_product, 1999, 2017), 'average_price')
    f.yaxis.axis_label="Price of {}".format(set_product)

elif dataset2 == 'migration_movements':
    y_as = normalize(select_plot_migration_movements1(migration_movements, set_country, 1999, 2017), 'Value')
    f.yaxis.axis_label="Amount of refugees in {}".format(set_country)

output_file("compare_refugees_{}_and_price_of_{}.html".format(set_country, set_product))

# title
f.title.text="Correlation between refugees {} and price of {}".format(set_country, set_product)
f.title.text_font_size="25px"
f.title.align="center"

# toolbar
f.toolbar_location='above'

# manual legend to get it next to the plot, not over it

f.circle(x_as['Normalized_data'], y_as['Normalized_data'] , color='red')

save(f)


os.chdir("../../")
os.chdir("plot code/Compare data")
