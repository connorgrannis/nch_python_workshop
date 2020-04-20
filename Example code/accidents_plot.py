# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:04:41 2020

@author: rcf004
"""

import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats

#%%
accidents = pd.read_csv(r'C:\Users\rcf004\Documents\Python Scripts\US_Accidents_Dec19.csv')
accidents.dropna(subset=['Start_Lng', 'Start_Lat', 'Severity', 'Visibility(mi)'], inplace=True)

#%%
no_out = accidents[np.abs(stats.zscore(accidents['Visibility(mi)'].astype(int))) < 3]

#%%

df1 = no_out[no_out['Start_Time'].astype(str).str.contains('2016-')]
df2 = no_out[no_out['Start_Time'].astype(str).str.contains('2017-')]
df3 = no_out[no_out['Start_Time'].astype(str).str.contains('2018-')]
df4 = no_out[no_out['Start_Time'].astype(str).str.contains('2019-')]

#%%

a = 0.5
sz = (1, 10)
lw = 0
kwargs = {'marker': "."}
cmap = sns.cubehelix_palette(start=1.1, rot=0.9, gamma=1.7, hue=0.9, light=0.8, dark=0.4, as_cmap=True, reverse=True)

#%%

g1 = sns.scatterplot(x='Start_Lng', y='Start_Lat', 
                size='Severity', 
                hue='Visibility(mi)', 
                alpha=a, 
                sizes=sz,
                linewidth=0,
                data=df1, 
                palette=cmap,
                **kwargs)

g1.legend(loc='lower right', bbox_to_anchor=(1.25, 0.5), ncol=1, fontsize='x-small')
g1.axes.set_title('Car Accidents in 2016', fontsize=20)
g1.set_xlabel('Longitude', fontsize=10)
g1.set_ylabel('Latitude', fontsize=10)
g1.tick_params(labelsize=10)

#%%

g2 = sns.scatterplot(x='Start_Lng', y='Start_Lat',
                size='Severity',
                hue='Visibility(mi)',
                alpha=a,
                sizes=sz,
                linewidth=0,
                data=df2,
                palette=cmap,
                **kwargs)

g2.legend(loc='lower right', bbox_to_anchor=(1.25, 0.5), ncol=1, fontsize='x-small')
g2.axes.set_title('Car Accidents in 2017', fontsize=20)
g2.set_xlabel('Longitude', fontsize=10)
g2.set_ylabel('Latitude', fontsize=10)
g2.tick_params(labelsize=10)

#%%

g3 = sns.scatterplot(x='Start_Lng', y='Start_Lat',
                size='Severity',
                hue='Visibility(mi)',
                alpha=a,
                sizes=sz,
                linewidth=0,
                data=df3,
                palette=cmap,
                **kwargs)

g3.legend(loc='lower right', bbox_to_anchor=(1.25, 0.5), ncol=1, fontsize='x-small')
g3.axes.set_title('Car Accidents in 2018', fontsize=20)
g3.set_xlabel('Longitude', fontsize=10)
g3.set_ylabel('Latitude', fontsize=10)
g3.tick_params(labelsize=10)

#%%

g4 = sns.scatterplot(x='Start_Lng', y='Start_Lat', 
                size='Severity', 
                hue='Visibility(mi)', 
                alpha=a, 
                sizes=sz,
                linewidth=0,
                data=df4, 
                palette=cmap,
                **kwargs)

g4.legend(loc='lower right', bbox_to_anchor=(1.25, 0.5), ncol=1, fontsize='x-small')
g4.axes.set_title('Car Accidents in 2019', fontsize=20)
g4.set_xlabel('Longitude', fontsize=10)
g4.set_ylabel('Latitude', fontsize=10)
g4.tick_params(labelsize=10)
