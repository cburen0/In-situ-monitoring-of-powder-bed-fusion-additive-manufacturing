# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 11:11:09 2024

@author: Mumin
"""

import IPython as IP
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

IP.get_ipython().run_line_magic('reset', '-sf')

plt.close('all')

#%% Load Data

data = np.loadtxt('data-files/LV-data/LV-data_5.txt', delimiter = ',', skiprows = 23,)
print(data)

len(data)

copy()