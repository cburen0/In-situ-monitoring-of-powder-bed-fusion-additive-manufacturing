# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:33:31 2024

@author: mumin
"""

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

directory = "C:/GitHub/In-situ-monitoring-of-powder-bed-fusion-additive-manufacturing/system_development/Orichalcum/v0.2/Software_design/v2-cover-control/Data Folder/"
print(Path.home())

max_frequencies = []


data_file = "Test  0_001.lvm"
file_path = Path(directory, data_file)

data = pd.read_csv(file_path, delimiter=',', skiprows=21, comment=';', header=0)

column_data = data.iloc[:,1]
           
fft_data = np.fft.fft(column_data)
sample_rate = 100
n = len(fft_data)
freqs = np.fft.fftfreq(n, d=sample_rate)

fft_magnitudes = np.abs(fft_data)

positive_freqs = freqs[:n // 2]
positive_magnitudes = fft_magnitudes[:n // 2]

#max_freq = positive_freqs[np.argmax(positive_magnitudes)]
#max_frequencies.append(max_freq)
#print(f'Frequencies = {max_freq}')

plt.figure(figsize=(10, 6))
plt.plot(positive_freqs, positive_magnitudes)
plt.title('FFT of Data Column')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()