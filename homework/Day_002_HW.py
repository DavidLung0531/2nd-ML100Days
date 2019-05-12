# -*- coding: utf-8 -*-
"""
Created on Sun May 12 15:34:00 2019

@author: 煥其
"""

"""
"""
import os
import numpy as np
import pandas as pd

# 設定 data_path
dir_data = '../Data/'
f_app = os.path.join(dir_data, 'application_train.csv')
print('print of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app)

print(app_train.shape)
#print(app_train.size)

print(app_train.columns)
#print(app_train.columns[3])
#print(app_train.columns.tolist)

print(app_train.iloc[:7,:6])