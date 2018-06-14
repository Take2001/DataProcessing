
# coding: utf-8

# In[19]:


#aantal mappen terug naar DataProcessing #de dataset die je wil importeren 

def select_df(folders_up, dataset):
    import os
    import pandas as pd
    import numpy as np
    
    if dataset == 'foodprices':
        for i in range(folders_up):
            os.chdir("../")
        os.chdir("datasets/preprocessed datasets/Food prices")
        raw_data = pd.read_csv('Food_prizes_Africa_processed.csv')
        df = pd.DataFrame(raw_data)
        print('Succesfully imported foodprices!')   
        
    elif dataset == 'migration_movements':
        for i in range(folders_up):
            os.chdir("../")                   
        os.chdir("datasets/preprocessed datasets/Migration movements")
        raw_data = pd.read_csv('data_africa.csv')
        df = pd.DataFrame(raw_data)
        print('Succesfully imported migration_movements!')    
                                    
    elif dataset == 'temperature_and_precipitation':
        for i in range(folders_up):
            os.chdir("../")        
        os.chdir("datasets/preprocessed datasets/Temperature and precipitation")
        raw_data = pd.read_csv('tas_pr_1991_2015_AC.csv')
        df = pd.DataFrame(raw_data)
        print('succesfully imported temperature_and_precipitation!')
        
    else:
        return('Error: -- {} -- is geen beschikbare dataset. Kies uit: foodprices, migration_movements of temperature_and_precipitation'.format(dataset))
    
    if folders_up < 3:    
        for i in range(3 - folders_up ):
            os.chdir("../")
    return df

# werking
# select_df(1, 'migration_movements')