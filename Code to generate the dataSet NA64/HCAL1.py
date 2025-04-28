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


C1_1,C2_1,C3_1,C4_1,C5_1,C6_1,C7_1,C8_1,C9_1,C10_1 = [],[],[],[],[],[],[],[],[],[]
C11_1,C12_1,C13_1,C14_1,C15_1,C16_1,C17_1,C18_1,C19_1,C20_1 = [],[],[],[],[],[],[],[],[],[]
C21_1,C22_1,C23_1,C24_1,C25_1,C26_1,C27_1,C28_1,C29_1,C30_1 = [],[],[],[],[],[],[],[],[],[]
C31_1,C32_1,C33_1,C34_1,C35_1,C36_1,C37_1,C38_1,C39_1,C40_1 = [],[],[],[],[],[],[],[],[],[]
C41_1,C42_1,C43_1,C44_1,C45_1,C46_1,C47_1 = [],[],[],[],[],[],[]

E_25 = [] #hcal_1 j=2


for j in range(0,56):
    for i in range(0,run-run_inicial+1):
        if j == 2:
            a = i*55+j
            L = []
            E_run=[]
            #print(g[a])
            with open(A[a],"r") as name:
                L.append(name.readlines())
            for x in range(439,len(L[0])): 
                    #print(x)
                if 'Binning' and 'CENT1.0' in L[0][x]:
                    #print(L[0][x])
                    C1_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.1'  in L[0][x]:
                    #print(L[0][x])
                    C2_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.2' in L[0][x]:
                    #print(L[0][x])
                    C3_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.3' in L[0][x]:
                    #print(L[0][x])
                    C4_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.4' in L[0][x]:
                    #print(L[0][x])
                    C5_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.5' in L[0][x]:
                    #print(L[0][x])
                    C6_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.6' in L[0][x]:
                    #print(L[0][x])
                    C7_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.7' in L[0][x]:
                    #print(L[0][x])
                    C8_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.8' in L[0][x]:
                    #print(L[0][x])
                    C9_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.9' in L[0][x]:
                    #print(L[0][x])
                    C10_1.append(float(L[0][x+1].lstrip().rstrip('\n')))

                    
                if 'Binning' and 'CENT1.10' in L[0][x]:
                    #print(L[0][x])
                    C11_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                  
                if 'Binning' and 'CENT1.11' in L[0][x]:
                    #print(L[0][x])
                    C12_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.12' in L[0][x]:
                    #print(L[0][x])
                    C13_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.13' in L[0][x]:
                    #print(L[0][x])
                    C14_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                       
                if 'Binning' and 'CENT1.14' in L[0][x]:
                    #print(L[0][x])
                    C15_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.15' in L[0][x]:
                    #print(L[k][0][x])
                    C16_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.16' in L[0][x]:
                    #print(L[k][0][x])
                    C17_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.17' in L[0][x]:
                    #print(L[0][x])
                    C18_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.18' in L[0][x]:
                    #print(L[k][0][x])
                    C19_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.19' in L[0][x]:
                    #print(L[k][0][x])
                    C20_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                        
                if 'Binning' and 'CENT1.20' in L[0][x]:
                    #print(L[k][0][x])
                    C21_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.21' in L[0][x]:
                    #print(L[k][0][x])
                    C22_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.22' in L[0][x]:
                    #print(L[k][0][x])
                    C23_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.23' in L[0][x]:
                    #print(L[k][0][x])
                    C24_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.24' in L[0][x]:
                    #print(L[k][0][x])
                    C25_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.25' in L[0][x]:
                    #print(L[k][0][x])
                    C26_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.26' in L[0][x]:
                    #print(L[0][x])
                    C27_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.27' in L[0][x]:
                    #print(L[k][0][x])
                    C28_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.28' in L[0][x]:
                    #print(L[k][0][x])
                    C29_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.29' in L[0][x]:
                    #print(L[0][x])
                    C30_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.30' in L[0][x]:
                    #print(L[k][0][x])
                    C31_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.31' in L[0][x]:
                    #print(L[k][0][x])
                    C32_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.32' in L[0][x]:
                    #print(L[0][x])
                    C33_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.33' in L[0][x]:
                    #print(L[k][0][x])
                    C34_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.34' in L[0][x]:
                    #print(L[k][0][x])
                    C35_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.35' in L[0][x]:
                    #print(L[k][0][x])
                    C36_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.36' in L[0][x]:
                    #print(L[k][0][x])
                    C37_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.37' in L[0][x]:
                    #print(L[k][0][x])
                    C38_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.38' in L[0][x]:
                    #print(L[k][0][x])
                    C39_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.39' in L[0][x]:
                    #print(L[k][0][x])
                    C40_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                    
                        
                if 'Binning' and 'CENT1.40' in L[0][x]:
                    #print(L[0][x])
                    C41_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.41' in L[0][x]:
                    #print(L[k][0][x])
                    C42_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.42' in L[0][x]:
                    #print(L[k][0][x])
                    C43_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.43' in L[0][x]:
                    #print(L[0][x])
                    C44_1.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT1.44' in L[0][x]:
                    #print(L[k][0][x])
                    C45_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.45' in L[0][x]:
                    #print(L[k][0][x])
                    C46_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT1.46' in L[0][x]:
                    #print(L[k][0][x])
                    C47_1.append(float(L[0][x+1].lstrip().rstrip('\n')))
                

E_25=[]

for j in range(0,78):
    for i in range(run-run_inicial+1):
        if j == 2:
            a = i*55+j
            L = []
            E_run = []
            print(A[a])
            with open(A[a],"r") as name:
                L.append(
                    name.readlines())
                for x in range(len(L[0])):
                    #print(x)
                    if 'Binning n:' in L[0][x] and 'Binning n:  154,' not in L[0][x]:
                        #print(L[0][x])
                        E_run.append(float(L[0][x+1].lstrip().rstrip('\n')))
                E_25.append(E_run)

# Número de capas
numero_sublistas = 47

# Inicializa una lista de sublistas vacías
H1 = [[] for _ in range(numero_sublistas)]

# Agrega los elementos a las sublistas en orden
for j in range(0,run-run_inicial+1):
    for i, dato in enumerate(E_25[j]):
        indice_sublista = i % numero_sublistas  # Calcula el índice de la sublista
        H1[indice_sublista].append(dato)

E_25= pd.DataFrame()
for i in range(1,48):
    E_25[f'C{i}_1'] = H1[i-1]

E_25.to_csv('Energy_Hcal1.csv',index = False )

# Suponiendo que E_25 es tu DataFrame original

# Calcular la suma de las columnas (capas) y crear un nuevo DataFrame
df_total_sum = pd.DataFrame(E_25.sum(axis=1), columns=['HCAL1'])

# Mostrar el nuevo DataFrame
print(df_total_sum)

# Guardar el nuevo DataFrame en un archivo CSV
df_total_sum.to_csv('Hcal1_Total.csv', index=False)

# Mensaje de confirmación
print("Archivo 'Hcal1_Total.csv' generado correctamente.")
