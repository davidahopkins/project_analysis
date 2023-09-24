#the following imports needed libraries 
import time
import math
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.stats import norm
#the following asks for user input on needed to select the correct actions
est_points = int(input("How many estimate points are there (i.e 1 or 3)?"))
file_path = input("What is the file path for the estimate?")
iterations = int(input('How many iterations?'))
bin_size = int(input('What is the bin size for the histogram?'))
start_time = time.perf_counter()
df = pd.read_excel(file_path) #creates the main dataframe
divisions = list(df['Division']) #create the list of divisions which is used to position the simulation data

#the following created the simulation table, it transposes the same data as df and drops the unneeded columns and headers
sim_data = pd.read_excel(file_path).set_index('Division') 
sim_data = sim_data.T
sim_data.drop('Division Code',axis=0,inplace=True)
sim_data.drop('As Estimated',axis=0,inplace=True)

#this begins the code for a single point estimate
if est_points == 1: 
    low_estimate = int(input('What is the percent below the estimate value for the low range?'))
    low_percent = (1-(low_estimate/100))
    high_estimate = int(input('What is the percent below the estimate value for the high range?'))
    high_percent = (1+(high_estimate/100))
    df.insert(2,'Low','')
    df['Low'] = df['As Estimated']*low_percent
    df['High'] = df['As Estimated']*high_percent
    #begins the code for developing the simulation using a normal distribution
    df['std_dev'] = df[['Low','As Estimated','High']].std(axis=1)
    df['Total'] = ''
    #df.to_excel('std_test.xlsx') #turn this line of code on or off to validate the standard deviation function
    for i in range(iterations):
        df['random_p'] = [random.uniform(0.0,1.0) for i in df.index]
        for index, row in df.iterrows():
            if df.loc[index, 'As Estimated'] == 0:
                df.loc[index,'Total'] = 0
            else:
                df.loc[index, 'Total'] = norm.ppf(df.loc[index,'random_p'], \
                                                loc=df.loc[index,'As Estimated'], \
                                                    scale=df.loc[index,'std_dev'])
        sim_data.loc[i+1,divisions[0]] = df.loc[0,'Total']
        sim_data.loc[i+1,divisions[1]] = df.loc[1,'Total']
        sim_data.loc[i+1,divisions[2]] = df.loc[2,'Total']
        sim_data.loc[i+1,divisions[3]] = df.loc[3,'Total']
        sim_data.loc[i+1,divisions[4]] = df.loc[4,'Total']
        sim_data.loc[i+1,divisions[5]] = df.loc[5,'Total']
        sim_data.loc[i+1,divisions[6]] = df.loc[6,'Total']
        sim_data.loc[i+1,divisions[7]] = df.loc[7,'Total']
        sim_data.loc[i+1,divisions[8]] = df.loc[8,'Total']
        sim_data.loc[i+1,divisions[9]] = df.loc[9,'Total']
        sim_data.loc[i+1,divisions[10]] = df.loc[10,'Total']
        sim_data.loc[i+1,divisions[11]] = df.loc[11,'Total']
        sim_data.loc[i+1,divisions[12]] = df.loc[12,'Total']
        sim_data.loc[i+1,divisions[13]] = df.loc[13,'Total']
        sim_data.loc[i+1,divisions[14]] = df.loc[14,'Total']
        sim_data.loc[i+1,divisions[15]] = df.loc[15,'Total']
        sim_data.loc[i+1,divisions[16]] = df.loc[16,'Total']
        sim_data.loc[i+1,divisions[17]] = df.loc[17,'Total']
        sim_data.loc[i+1,divisions[18]] = df.loc[18,'Total']
        sim_data.loc[i+1,divisions[19]] = df.loc[19,'Total']
        sim_data.loc[i+1,divisions[20]] = df.loc[20,'Total']
        sim_data.loc[i+1,divisions[21]] = df.loc[21,'Total']
        sim_data.loc[i+1,divisions[22]] = df.loc[22,'Total']
        sim_data.loc[i+1,divisions[23]] = df.loc[23,'Total']
        sim_data.loc[i+1,divisions[24]] = df.loc[24,'Total']
        sim_data.loc[i+1,divisions[25]] = df.loc[25,'Total']
        sim_data.loc[i+1,divisions[26]] = df.loc[26,'Total']
        sim_data.loc[i+1,divisions[27]] = df.loc[27,'Total']
        sim_data.loc[i+1,divisions[28]] = df.loc[28,'Total']
        sim_data.loc[i+1,divisions[29]] = df.loc[29,'Total']
        sim_data.loc[i+1,divisions[30]] = df.loc[30,'Total']
        sim_data.loc[i+1,divisions[31]] = df.loc[31,'Total']
        sim_data.loc[i+1,divisions[32]] = df.loc[32,'Total']
        sim_data.loc[i+1,divisions[33]] = df.loc[33,'Total']
    #begins the code for developing the simulation using a triangular distribution
if est_points == 3:
    #begins the code for developing the simulation using a normal distribution
    sim_data.drop('Low',axis=0,inplace=True)
    sim_data.drop('High',axis=0,inplace=True)
    df['std_dev'] = df[['Low','As Estimated','High']].std(axis=1)
    df['Total'] = ''
    #df.to_excel('std_test.xlsx') #turn this line of code on or off to validate the standard deviation function
    for i in range(iterations):
        df['random_p'] = [random.uniform(0.0,1.0) for i in df.index]
        for index, row in df.iterrows():
            if df.loc[index, 'As Estimated'] == 0:
                df.loc[index,'Total'] = 0
            else:
                df.loc[index, 'Total'] = norm.ppf(df.loc[index,'random_p'], \
                                                loc=df.loc[index,'As Estimated'], \
                                                    scale=df.loc[index,'std_dev'])
        sim_data.loc[i+1,divisions[0]] = df.loc[0,'Total']
        sim_data.loc[i+1,divisions[1]] = df.loc[1,'Total']
        sim_data.loc[i+1,divisions[2]] = df.loc[2,'Total']
        sim_data.loc[i+1,divisions[3]] = df.loc[3,'Total']
        sim_data.loc[i+1,divisions[4]] = df.loc[4,'Total']
        sim_data.loc[i+1,divisions[5]] = df.loc[5,'Total']
        sim_data.loc[i+1,divisions[6]] = df.loc[6,'Total']
        sim_data.loc[i+1,divisions[7]] = df.loc[7,'Total']
        sim_data.loc[i+1,divisions[8]] = df.loc[8,'Total']
        sim_data.loc[i+1,divisions[9]] = df.loc[9,'Total']
        sim_data.loc[i+1,divisions[10]] = df.loc[10,'Total']
        sim_data.loc[i+1,divisions[11]] = df.loc[11,'Total']
        sim_data.loc[i+1,divisions[12]] = df.loc[12,'Total']
        sim_data.loc[i+1,divisions[13]] = df.loc[13,'Total']
        sim_data.loc[i+1,divisions[14]] = df.loc[14,'Total']
        sim_data.loc[i+1,divisions[15]] = df.loc[15,'Total']
        sim_data.loc[i+1,divisions[16]] = df.loc[16,'Total']
        sim_data.loc[i+1,divisions[17]] = df.loc[17,'Total']
        sim_data.loc[i+1,divisions[18]] = df.loc[18,'Total']
        sim_data.loc[i+1,divisions[19]] = df.loc[19,'Total']
        sim_data.loc[i+1,divisions[20]] = df.loc[20,'Total']
        sim_data.loc[i+1,divisions[21]] = df.loc[21,'Total']
        sim_data.loc[i+1,divisions[22]] = df.loc[22,'Total']
        sim_data.loc[i+1,divisions[23]] = df.loc[23,'Total']
        sim_data.loc[i+1,divisions[24]] = df.loc[24,'Total']
        sim_data.loc[i+1,divisions[25]] = df.loc[25,'Total']
        sim_data.loc[i+1,divisions[26]] = df.loc[26,'Total']
        sim_data.loc[i+1,divisions[27]] = df.loc[27,'Total']
        sim_data.loc[i+1,divisions[28]] = df.loc[28,'Total']
        sim_data.loc[i+1,divisions[29]] = df.loc[29,'Total']
        sim_data.loc[i+1,divisions[30]] = df.loc[30,'Total']
        sim_data.loc[i+1,divisions[31]] = df.loc[31,'Total']
        sim_data.loc[i+1,divisions[32]] = df.loc[32,'Total']
        sim_data.loc[i+1,divisions[33]] = df.loc[33,'Total']

sim_data  = sim_data.loc[:,(sim_data !=0).any(axis=0)]
sim_data['Total'] = sim_data.sum(axis=1)
sim_data.to_excel('raw_sim_data.xlsx')

five_below_ave = sim_data['Total'].mean() * 0.95
five_abv_ave =  sim_data['Total'].mean() * 1.05
ten_above_ave = sim_data['Total'].mean() * 1.1
three_qtr = sim_data['Total'].quantile(0.75)
nine_five = sim_data['Total'].quantile(0.95)

results = pd.DataFrame()
results['description']=''
results['result']=''

results.loc[1,'description'] = 'Average Value'
results.loc[2,'description'] = '75th Percentile'
results.loc[3,'description'] = '95th Percentile'
results.loc[4,'description'] = 'Percent Above: {:.2f}'.format(five_below_ave)
results.loc[5,'description'] = 'Percent Above: {:.2f}'.format(five_abv_ave)
results.loc[6,'description'] = 'Percent Above: {:.2f}'.format(ten_above_ave)

results.loc[1,'result'] = sim_data['Total'].mean().round(2)
results.loc[2,'result'] = three_qtr
results.loc[3,'result'] = nine_five
results.loc[4,'result'] = sum(sim_data['Total'] > five_below_ave)/iterations
results.loc[5,'result'] = sum(sim_data['Total'] > five_abv_ave)/iterations
results.loc[6,'result'] = sum(sim_data['Total'] > ten_above_ave)/iterations

results.to_excel('sim_results.xlsx')
plot_data = sim_data['Total']
plot_mean = plot_data.mean()

sns.histplot(plot_data, stat="count" ,bins=bin_size, kde=True, color="b")

plt.savefig('simulation_histogram', dpi=600)

stop_time = time.perf_counter()
total_time = stop_time - start_time
print(total_time)