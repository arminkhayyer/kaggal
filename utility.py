import collections
import pandas as pd
import numpy as np

def cleanedCategoricalWithTooManyOptions(df, column, percentThreshold=.01):
    numEachOption = collections.Counter(df[column])
    percentEachOption = {key: value/len(df[column]) for key, value in numEachOption.items()}
    highlyOccuring= set()
    for key in percentEachOption:
        if percentEachOption[key] > percentThreshold:
            highlyOccuring.add(key)
    #print(highlyOccuring)
    return df[column].map(lambda x: x if x in highlyOccuring else 'other')
