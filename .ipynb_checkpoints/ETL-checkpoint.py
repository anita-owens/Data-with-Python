import pandas as pd
import os
from datetime import datetime
import glob
import time
import pathlib


##If user should pick a file
def intro():
    csv_files_list = glob.glob('datasets/*.csv')
    csv_files = []
    for file in csv_files_list:
        csv_files.append(file.replace('datasets/', ''))
    print('Hello. Your datasets folder contains the following files: ' + str(csv_files))
    print('\nEnter the csv file name from the list output that you wish to load: ')
    file_to_process = input()
    print('The file you have chosen is: ' + file_to_process)
    time.sleep(2)
    file_to_read = 'datasets/' + file_to_process + ('.csv')
    return file_to_read


# +
def extract_from_csv(): 
    fname = intro()
    if pathlib.Path(fname).is_file(): # Check if file exists
        print('Getting ready to preview file')
        time.sleep(2)
        extracted_data = pd.read_csv(fname, skiprows=0)
        #print(extracted_data.head(3))
        return extracted_data
    #else:
    #    print('No such file exists at this time')

#extract_from_csv()


# -

'''
#Declare file outright to load
file_to_process = 'datasets/onebike_datetimes.csv'

def extract_from_csv(): 
    extracted_data = pd.read_csv(file_to_process) 
    return extracted_data '''


def transform_data():
    rows = extract_from_csv()
    df = pd.DataFrame(rows)
    return df

def load_data():
    data = transform_data()
    nrows = data.shape[0]
    ncols = data.shape[1]
    print("Finished at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))

load_data()
