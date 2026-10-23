import pandas as pd 
import numpy  as np 
import matplotlib.pyplot as plt


cd_wine_red   = pd.read_csv("winequality-red.csv", sep=",")
cd_wine_white = pd.read_csv("winequality-white.csv", sep=",")

print(cd_wine_red["quality"])