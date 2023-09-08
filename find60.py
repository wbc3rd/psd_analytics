#new console program that any lab can use
'''
import os
import mne

def port60():
    filePath = input('Please Enter Your Full File Path: ')
    rawFile = mne.io.read_raw_egi(filePath, preload=True)
    psdRaw = rawFile.compute_psd('welch')
    print("Percent 60Hz noise for entire session: ")
    for i in range(len(psdRaw.freqs)-1):
        total_60 = (float(psdRaw[i,61]) / psdRaw[i].sum()) * 100
        pretty60 = round(total_60, 2)
        print({i+1:pretty60})

port60()'''
# added feature
import os
import mne

#need to look at a lot of good sessions to get a good idea for the threshold
#algorithm to look at individual files and get an idea about 60Hz noise
# def port60():
#     filePath  = input('Please Enter Your Full File Path: ')
#     threshold = input('Please Enter a Threshold Value: ')
#     rawFile = mne.io.read_raw_egi(filePath, preload=True)
#     psdRaw = rawFile.compute_psd('welch')
#     print("60Hz noise for entire session over", threshold + '%')
#     for i in range(len(psdRaw.freqs)-1):
#         total_60 = (float(psdRaw[i,61]) / psdRaw[i].sum()) * 100
#         if total_60 > float(threshold):
#             pretty60 = round(total_60, 2)
#             print({i+1:pretty60})
#
# port60()

def port60_flex():
    filePath  = input('Please Enter Your Full File Path: ')
    singChan  = input('Single Channel (SC) or Full Channel (FC) mode: ')
    if singChan.lower() == 'sc':
        channel = input('Please enter a channel: ')
        correct = int(channel) - 1
        rawFile = mne.io.read_raw_egi(filePath, preload=True)
        psdRaw  = rawFile.compute_psd('welch')
        print('\n\n')
        print("60Hz noise for channel: ", channel)
        total_60 = (float(psdRaw[correct,61]) / psdRaw[correct].sum()) * 100
        pretty60 = round(total_60, 2)
        print({channel:pretty60})
    elif singChan.lower() == 'fc':
        threshold = input('Please Enter a Threshold Value: ')
        rawFile = mne.io.read_raw_egi(filePath, preload=True)
        psdRaw = rawFile.compute_psd('welch')
        print('\n\n')
        print("60Hz noise for entire session over", threshold + '%')
        for i in range(len(psdRaw.freqs)-1):
            total_60 = (float(psdRaw[i,61]) / psdRaw[i].sum()) * 100
            if total_60 > float(threshold):
                pretty60 = round(total_60, 2)
                print({i+1:pretty60})

port60_flex()
