import collections
import pandas as pd
import numpy as np

def cleanedCategoricalWithTooManyOptions(df, column, percentThreshold=.01, highlyOccuring=set()):
    if len(highlyOccuring) == 0:
        #print("len(highlyOccuring)==0")
        numEachOption = collections.Counter(df[column])
        percentEachOption = {key: value/len(df[column]) for key, value in numEachOption.items()}
        for key in percentEachOption:
            if percentEachOption[key] > percentThreshold:
                highlyOccuring.add(key)
    return df[column].map(lambda x: x if x in highlyOccuring else 'other')

def categoricalWithTooManyOptions(df, column, percentThreshold=.01):
    highlyOccuring = set()
    df[column].fillna('nane', inplace=True)
    numEachOption = collections.Counter(df[column])
    percentEachOption = {key: value/len(df[column]) for key, value in numEachOption.items()}
    for key in percentEachOption:
        if percentEachOption[key] > percentThreshold:
            highlyOccuring.add(key)
    return highlyOccuring

def cleanOptions(df, column, highlyOccuring):
    df[column] = df[column].map(lambda x: x if x in highlyOccuring else 'other')

def cleanNumericColumn(df, columns, createFlag):
    for column in columns:
        if createFlag:
            df["%s_isnane"%column] = df[column].isna()
        df[column] = df[column].fillna(df[column].mean())
