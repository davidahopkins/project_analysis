#import required packages

import numpy as np
import pandas as pd
import os
import time
import glob
from openpyxl import Workbook

#create user inputs for script
dir_path = input('what is the file path?')

save_to_current = input('do you want to save output to another location? [y/n]?')
if save_to_current == 'n':
    save_path = dir_path
else:
    save_path = input('what is the file path to save to?')

project_number = str(input('what is the project #?'))

#start the timer
start = time.perf_counter()

#create a blank list for file names
file_name = []

#loop through directory and list all file names
for (root, dirs, file) in os.walk(dir_path):
    for f in file:
        file_name.append(f)

#loop through the directory and list all file paths
file_path = [os.path.join(dirpath, f) for (dirpath, dirnames, filenames) in os.walk(dir_path) for f in filenames]

#create list length
count = len(file_name)

#create dictionary from the list of file names and paths
file_dict = {file_name[i]: file_path[i] for i in range(len(file_name))}

#create dataframe from dictionary
df = pd.DataFrame(list(zip(file_name, file_path)), columns=['Name', 'Path'])

#create columns for dataframe
df.insert(0,'Date','')
df.insert(1,'Document Type','')
df['Name Match'] = ''
df['Error Checking'] = ''
df['Document'] = ''
df['Author'] = ''
df['Amount'] = ''

#loop rhrough data and create hyperlinks and error checking of dataframe
for i in range(count):
    j =+ i+1
    df.loc[i,'Document'] = '=HYPERLINK(E{}, D{})'.format(j+1,j+1)
    df.loc[i,'Name Match'] = '=TRIM(RIGHT(SUBSTITUTE(E{},"\\",REPT(" ",255)),255))'.format(j+1,j+1)
    df.loc[i, 'Error Checking'] = '=D{}=F{}'.format(j+1,j+1)

#export dataframe to excel
df.to_excel(save_path+'\\'+project_number+'.Document Log.xlsx')

#stop the timer
stop = time.perf_counter()
print(f'A total of {count} documents were listed in {stop - start:0.2f} seconds')