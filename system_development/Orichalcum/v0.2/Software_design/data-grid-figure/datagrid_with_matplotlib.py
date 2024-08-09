# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:17:08 2024

@author: mumin
"""

import numpy as np 
import matplotlib.pyplot as plt 
  
data = np.random.random((10, 10)) 
plt.imshow( data ) 
  
plt.title( "Data Grid" )

plt.show() 