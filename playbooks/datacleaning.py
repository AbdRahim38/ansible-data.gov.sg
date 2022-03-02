#!/usr/bin/env python

import fnmatch
import os
import pandas as pd

# variable declaration
csv_files = []
my_path = '../data-download/'
my_path_result = '../results/'
grad_subttl = []
grad_ttl = 0
counter = 0

print(f'\n============================================================\n')
# scan directory for csv file listing
for file in os.listdir(my_path):
    if fnmatch.fnmatch(file, '*.csv'):
        the_file = my_path + file
        csv_files.append(the_file)
        dataframe = pd.read_csv(the_file)
        dataframe['graduates'] = dataframe['graduates'].str.replace(',', '').astype(float)
        my_datatable = dataframe[(dataframe.sex == "MF") & (dataframe.course == "Information Technology")]
        my_datatable.to_csv(my_path_result + 'datafile' + str(counter) + '.csv' , index=False)
        grad_subttl.append(my_datatable['graduates'].sum())
        print(f'REPORT FROM: {file}\n\n{my_datatable}\n')
        print(f'Graduates Sub-Total: {grad_subttl[counter]}\n')
        print(f'============================================================\n')
        grad_ttl += grad_subttl[counter]
        counter += 1

print(f'Graduates Total: {grad_ttl}\n')
