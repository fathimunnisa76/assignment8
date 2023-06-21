# -*- coding: utf-8 -*-
"""
Created on Tue May  2 18:47:17 2023

@author: HP
"""
import pandas as pd
df1=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\friends_names.csv",sep=",")
print(df1)

df2=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\familymember_names.txt",sep="*")
print(df2)

df3=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\python_assignments\VegFood_names.txt",sep="|")
print(df3)

df4=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\python_assignments\nonveg items.txt",sep="|")
print(df4)

df5=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\python_assignments\month name_season.txt",sep="&")
print(df5)

df6=pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Fathima\python_assignments\colour_names.txt",sep="^")
print(df6)