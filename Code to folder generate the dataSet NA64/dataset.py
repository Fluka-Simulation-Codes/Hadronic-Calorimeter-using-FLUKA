import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#leer el archivo csv HCAL0 (suma capas)
df_total_sum_hcal0 = pd.read_csv('Hcal0_Total.csv')
# Muestra las primeras filas del DataFrame
df_total_sum_hcal0

#lee el archivo csv Hcal1 (suma capas)
df_total_sum_hcal1 = pd.read_csv('Hcal1_Total.csv')
# Muestra las primeras filas del DataFrame
df_total_sum_hcal0

#lee el archivo csv Hcal2 (suma capas)
df_total_sum_hcal2 = pd.read_csv('Hcal2_Total.csv')
# Muestra las primeras filas del DataFrame
df_total_sum_hcal2

#suma TOTAL hcal
df_HCAL = pd.concat([df_total_sum_hcal0, df_total_sum_hcal1, df_total_sum_hcal2], axis=1)
#sumar las columnas a lo largo hcal
df_HCAL['total_sum_HCAL'] = df_HCAL.sum(axis=1)

print(df_HCAL)

df_total_sum_ECAL = pd.read_csv('Ecal_Veto.csv')

df_total_sum_ECAL

print(df_total_sum_ECAL)

# Concatenar df_total_sum_ECAL y df_HCAL por filas
NA64 = pd.concat([df_total_sum_ECAL, df_HCAL], axis=0)

# Mostrar el DataFrame combinado
print(NA64)
