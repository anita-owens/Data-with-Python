import pandas as pd
import os
# Give the location of your file -
#file_to_process = ('datasets/Dinner.xlsx')
print(os.getcwd())




def extract_from_csv(file_to_process): 
    extracted_data = pd.read_csv(file_to_process) 
    return extracted_data

extract_from_csv('/Users/anitaowens/Documents/GitHub/Forecasting-in-Python/datasets/creditunion.csv')



def transform_data(df):
       df['year'] = 1990
       df['date_string'] = df['year'].astype(str) + df['MONTH'].astype(str) + df['DAYMON']
       return df

out = initial_input
for func in [extract_from_csv, transform]:
    out = func(out)

transform(extracted_data)