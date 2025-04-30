import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the LabVIEW file
filename = r"C:\Users\mwhetham\Desktop\Trigger (pulser) and Wave Signal (LDV) read from PXI\Wave signals (NEW)\ldv(89)-000-000-"
with open(filename, 'r') as file:
    lines = file.readlines()

# Find the header end
for i, line in enumerate(lines):
    if '***End_of_Header***' in line:
        data_start = i + 2  # Skip the header end line and empty row
        break

# Read the data into a dataframe, skipping bad rows
data = []
for line in lines[data_start:]:
    try:
        values = line.strip().split(',')
        if len(values) >= 2:
            data.append([float(values[0]), float(values[1])])
    except ValueError:
        continue  # Skip non-numeric rows

data = pd.DataFrame(data, columns=['Time', 'Signal'])

fs = 2500000000  # Sampling frequency (Hz)

time = data['Time'].values / fs  # Adjust time scale by dividing by sample rate
signal = data['Signal'].values  # Second column is the waveform

# Plot the waveform
plt.figure(figsize=(10, 5))
plt.plot(time, signal)
plt.ylim(bottom=-0.4, top=0.4)
plt.xlabel("Time (μs)")
plt.ylabel("Amplitude")
plt.title("89")
plt.legend()
plt.grid()
plt.show()
