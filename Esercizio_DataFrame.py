import pandas as pd 
import numpy  as np 
import matplotlib.pyplot as plt


df_wine_red   = pd.read_csv("winequality-red.csv", sep=",")
df_wine_white = pd.read_csv("winequality-white.csv", sep=",")

print(df_wine_white.columns)
