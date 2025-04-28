import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

## para ejecutar este codigo necesitamos saber:
## 1) Cuantas carpetas "run" tiene la simulacion
## 2) direccion del Directorio de trabajo, donde se encuentran las carpetas "run"

run_inicial=1
run=10

ruta1 = "/media/huawei/TOSHIBA EXT/NA64_runs/Ecal_Veto_Hcal_1E7/round1"
ruta2 = "/media/huawei/TOSHIBA EXT/NA64_runs/Ecal_Veto_Hcal_1E7/round2"



Cluster = ruta1 + ruta2
Cluster

A= []

for i in range(run_inicial, run+1):
    for j in range(23,78):
        if i < 1001:
            #print(i)
            a = ruta1 +"/run"+str(i)
            #print(a) 
            b = "/ex_NA64_%d001_fort.%d" % (i,j)
            print(a+b)
            if os.path.exists(a+b) == True:#comprobamos si existe la direccion creada
                A.append(a+b)
                
        if i > 1000:
            #print(i)
            a = ruta2 +"/run"+str(i)
            #print(a) 
            b = "/ex_NA64_%d001_fort.%d" % (i,j)
            #print(a+b)
            if os.path.exists(a+b) == True:#comprobamos si existe la direccion creada
                A.append(a+b)

A

C1_2,C2_2,C3_2,C4_2,C5_2,C6_2,C7_2,C8_2,C9_2,C10_2 = [],[],[],[],[],[],[],[],[],[]
C11_2,C12_2,C13_2,C14_2,C15_2,C16_2,C17_2,C18_2,C19_2,C20_2 = [],[],[],[],[],[],[],[],[],[]
C21_2,C22_2,C23_2,C24_2,C25_2,C26_2,C27_2,C28_2,C29_2,C30_2 = [],[],[],[],[],[],[],[],[],[]
C31_2,C32_2,C33_2,C34_2,C35_2,C36_2,C37_2,C38_2,C39_2,C40_2 = [],[],[],[],[],[],[],[],[],[]
C41_2,C42_2,C43_2,C44_2,C45_2,C46_2,C47_2= [],[],[],[],[],[],[]

E_26 = [] #hcal_2 j=3


for j in range(0,56):
    for i in range(0,run-run_inicial+1):
        if j == 3:
            a = i*55+j
            L = []
            E_run=[]
            #print(g[a])
            with open(A[a],"r") as name:
                L.append(name.readlines())
            for x in range(439,len(L[0])): 
                if 'Binning' and 'CENT2.0' in L[0][x]:
                    #print(L[0][x])
                    C1_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.1' in L[0][x]:
                        #print(L[0][x])
                    C2_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.2' in L[0][x]:
                    #print(L[0][x])
                    C3_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.3' in L[0][x]:
                    #print(L[0][x])
                    C4_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.4' in L[0][x]:
                    #print(L[0][x])
                    C5_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.5' in L[0][x]:
                    #print(L[0][x])
                    C6_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.6' in L[0][x]:
                    #print(L[0][x])
                    C7_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.7' in L[0][x]:
                    #print(L[0][x])
                    C8_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.8' in L[0][x]:
                    #print(L[0][x])
                    C9_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.9' in L[0][x]:
                    #print(L[0][x])
                    C10_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.10' in L[0][x]:
                    #print(L[0][x])
                    C11_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.11' in L[0][x]:
                    #print(L[0][x])
                    C12_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.12' in L[0][x]:
                    #print(L[0][x])
                    C13_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.13' in L[0][x]:
                   #print(L[0][x])
                    C14_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                        
                        
                        
                if 'Binning' and 'CENT2.14' in L[0][x]:
                    #print(L[0][x])
                    C15_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.15' in L[0][x]:
                    #print(L[k][0][x])
                    C16_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.16' in L[0][x]:
                    #print(L[k][0][x])
                    C17_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.17' in L[0][x]:
                    #print(L[0][x])
                    C18_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.18' in L[0][x]:
                    #print(L[k][0][x])
                    C19_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.19' in L[0][x]:
                    #print(L[k][0][x])
                    C20_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.20' in L[0][x]:
                    #print(L[k][0][x])
                    C21_2.append(float(L[0][x+1].lstrip().rstrip('\n')))    
                if 'Binning' and 'CENT2.21' in L[0][x]:
                    #print(L[k][0][x])
                    C22_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.22' in L[0][x]:
                    #print(L[k][0][x])
                    C23_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.23' in L[0][x]:
                    #print(L[k][0][x])
                    C24_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.24' in L[0][x]:
                    #print(L[k][0][x])
                    C25_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.25' in L[0][x]:
                    #print(L[k][0][x])
                    C26_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                        
                        
                if 'Binning' and 'CENT2.26' in L[0][x]:
                    #print(L[0][x])
                    C27_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.27' in L[0][x]:
                    #print(L[k][0][x])
                    C28_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.28' in L[0][x]:
                    #print(L[k][0][x])
                    C29_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.29' in L[0][x]:
                    #print(L[0][x])
                    C30_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.30' in L[0][x]:
                    #print(L[k][0][x])
                    C31_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.31' in L[0][x]:
                    #print(L[k][0][x])
                    C32_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.32' in L[0][x]:
                    #print(L[0][x])
                    C33_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.33' in L[0][x]:
                    #print(L[k][0][x])
                    C34_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.34' in L[0][x]:
                    #print(L[k][0][x])
                    C35_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.35' in L[0][x]:
                    #print(L[k][0][x])
                    C36_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.36' in L[0][x]:
                    #print(L[k][0][x])
                    C37_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.37' in L[0][x]:
                    #print(L[k][0][x])
                    C38_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.38' in L[0][x]:
                    #print(L[k][0][x])
                    C39_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.39' in L[0][x]:
                    #print(L[k][0][x])
                    C40_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                        
                        
                        
                if 'Binning' and 'CENT2.40' in L[0][x]:
                    #print(L[0][x])
                    C41_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.41' in L[0][x]:
                    #print(L[k][0][x])
                    C42_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.42' in L[0][x]:
                    #print(L[k][0][x])
                    C43_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.43' in L[0][x]:
                    #print(L[0][x])
                    C44_2.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT2.44' in L[0][x]:
                    #print(L[k][0][x])
                    C45_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.45' in L[0][x]:
                    #print(L[k][0][x])
                    C46_2.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT2.46' in L[0][x]:
                    #print(L[k][0][x])
                    C47_2.append(float(L[0][x+1].lstrip().rstrip('\n')))


for j in range(0,78):
    for i in range(run-run_inicial+1):
        if j == 3:
            a = i*55+j
            L = []
            E_run = []
            print(A[a])
            with open(A[a],"r") as name:
                L.append(
                    name.readlines())
                for x in range(len(L[0])):
                    #print(x)
                    if 'Binning n:' in L[0][x] and 'Binning n:  155,' not in L[0][x]:
                        #print(L[0][x])
                        E_run.append(float(L[0][x+1].lstrip().rstrip('\n')))
                E_26.append(E_run)

# Número de capas
numero_sublistas = 47

# Inicializa una lista de sublistas vacías
H2 = [[] for _ in range(numero_sublistas)]

# Agrega los elementos a las sublistas en orden
for j in range(0,run-run_inicial+1):
    for i, dato in enumerate(E_26[j]):
        indice_sublista = i % numero_sublistas  # Calcula el índice de la sublista
        H2[indice_sublista].append(dato)

E_26= pd.DataFrame()
for i in range(1,48):
    E_26[f'C{i}_2'] = H2[i-1]

E_26.to_csv('Energy_Hcal2.csv',index = False )
# Suponiendo que E_26 es tu DataFrame original

# Calcular la suma de las columnas (capas) y crear un nuevo DataFrame
df_total_sum = pd.DataFrame(E_26.sum(axis=1), columns=['HCAL2'])

# Mostrar el nuevo DataFrame
print(df_total_sum)

# Guardar el nuevo DataFrame en un archivo CSV
df_total_sum.to_csv('Hcal2_Total.csv', index=False)

# Mensaje de confirmación
print("Archivo 'Hcal2_Total.csv' generado correctamente.")
