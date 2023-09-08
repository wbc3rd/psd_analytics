#script for decomposing signals
#looks at amplitude (dB) for frequency bins
#do the imports
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import mne
%matplotlib qt

filePath = 'C:\\Users\\Owner\\Desktop\\cobraEEG_set\\austin_1_20221213_024114.mff'

def freqDecomp(filePath):
    #read in the raw file
    rawFile = mne.io.read_raw_egi(filePath, preload=True)

    #create a copy of the raw data
    filterSet = rawFile.copy()

    #get values for welch psd on raw data
    psdRaw = rawFile.compute_psd('welch')

    #get values for welch psd on filtered data
    psdFilt = filterSet.compute_psd('welch')

    #do a pie chart for the raw file psd
    labels = psdRaw.freqs
    sizes = psdRaw[54].reshape(129, )
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', normalize=True)
    fig1.suptitle("Channel 55 Frequency Bin Components Raw PSD")

    #do a pie chart for the filtered file psd
    labels = psdFilt.freqs
    sizes = psdFilt[54].reshape(129, )

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', normalize=True)
    fig1.suptitle("Channel 55 Frequency Bin Components Filt PSD")
