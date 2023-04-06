import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('errormeasurement.csv')

print(df.to_string())

xmean = pd.mean(df.loc["x"])