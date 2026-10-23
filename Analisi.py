import pandas as pd 
import numpy  as np 
import os
import matplotlib.pyplot as plt


df  = pd.read_csv("winequality-red.csv", sep=",")

#Presenza di duplicati e nulli 
print("Duplicati in df:", df.duplicated().sum())
df = df.drop_duplicates()
df = df.dropna()

#Stampo le colonne 

print(df.columns)
#Info sul DataFrame 
print("Prime 5 righe:")
print(df.head())

print("Ultime 5 righe:")
print(df.tail())

#Ordino il DataFrame in base a qualità 

df_quality = df.sort_values(
    by="quality",
    ascending=False
)

qualita_media = df.groupby("quality")["citric acid"].mean()
qualita_media = df.groupby("quality")["pH"].mean()
qualita_media = df.groupby("quality")["alcohol"].mean()

print(qualita_media)


