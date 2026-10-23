import pandas as pd 
import numpy as np 
import os
import matplotlib.pyplot as plt
import seaborn as sns

def grafico(x, y, titolo):
    # Definizione di x e y
    sns.barplot(x=x, y=y)

    plt.title(titolo)
    plt.xlabel(x.name)
    plt.ylabel(y.name)

    plt.xticks(x)
    plt.show()


while True:
    x = 0
    y = 0
    
    str = "" #stringa input
    titolo = ""
    csv = ""
    
    while  not os.path.exists(csv):
        csv = input("Inserisci nome del file da analizzare: ")
    
    df  = pd.read_csv(csv, sep=",")
    if "quality" in df:
        y = df["quality"]

    ### STAMPA INFO
    #Presenza di duplicati e nulli 
    print("Duplicati in df:", df.duplicated().sum())
    df = df.drop_duplicates()
    df = df.dropna()

    #Stampo le colonne 
    print(df.columns)

    #Info sul DataFrame 
    '''print("Prime 5 righe:")
    print(df.head())
    print("Ultime 5 righe:")
    print(df.tail())'''

    #Ordino il DataFrame in base a qualità 
    df_quality = df.sort_values(
        by="quality",
        ascending=False
    )

    #Qualità media
    qualita_media = df.groupby("quality")["citric acid"].mean()
    qualita_media = df.groupby("quality")["pH"].mean()
    qualita_media = df.groupby("quality")["alcohol"].mean()
    print(qualita_media)
    ###

    while True:
        #operazioni tra cui dimostrare grafico
        print("[s] stampa dataframe  [x] seleziona X  [y] seleziona Y  [t] seleziona titolo [i] Info grafico  [g] Mostra grafico  [X]  Scegli un altro file")
        match input("Inserire l'operazione da svolgere: ").lower():
            case 's':
                print(df)
            case 'x':
                while not str in df:
                    str = input("Inserisci colonna da selezionare per X: ")
                x = df[str]
            case 'y':
                while not str in df:
                    str = input("Inserisci colonna da selezionare per Y: ")
                y = df[str]
            case 't':
                titolo = input("Inserisci il titolo del grafico: ")
            case 'i':
                print("Titolo: ", titolo)
                print("Asse delle X: ", x.name)
                print("Asse delle Y: ", y.name)
            case 'g':

                grafico(x, y, titolo)
                pass
        str = ""