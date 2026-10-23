import pandas as pd 
import numpy  as np 
import os
import matplotlib.pyplot as plt


df  = pd.read_csv("winequality-red.csv", sep=",")

#Esplorazione# 
#print(df_wine_red.columns)

print(df.isnull().sum())

print("Duplicati cd_df:", df.duplicated().sum())











'''
while True:
    
    while  not os.path.exists(csv):
        
        csv = input("Inserisci nome del file da analizzare: ")
    
    df  = pd.read_csv(csv, sep=",")


    while True:
        #operazioni tra cui dimostrare grafico
        pass
'''