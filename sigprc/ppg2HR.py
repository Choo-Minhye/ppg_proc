# import heartpy as hp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal


data_path = 'ppgdata.xlsx'
ppg_data = pd.read_excel(data_path, usecols = [1]).values
timer = pd.read_excel(data_path, usecols = [0]).values
sampling_rate = 30

#and visualise
plt.figure(figsize=(12,4))
ppg_data_ = ppg_data.reshape((ppg_data.size,))
plt.plot(ppg_data_)

peaks, properties = signal.find_peaks(ppg_data_, height=720 )
plt.plot(peaks, ppg_data_[peaks], "o")
plt.show()
bpm_list = []
for i in range(peaks.size - 1) :
    BPM=(sampling_rate/(peaks[i+1]-peaks[i]))*60
    if BPM < 120 and BPM > 40 :
        bpm_list.append(BPM)

REAL_bpm =  sum(bpm_list) /  len(bpm_list)

print(REAL_bpm)
# wd, m = hp.process(ppg_data_, sample_rate = 30.0)

# hp.plotter(wd, m)

# for measure in m.keys() :
#     print('%s: %f' %(measure, m[measure]))