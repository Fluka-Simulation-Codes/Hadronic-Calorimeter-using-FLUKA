import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

## para ejecutar este codigo necesitamos saber:
## 1) Cuantas carpetas "run" tiene la simulacion
## 2) direccion del Directorio de trabajo, donde se encuentran las carpetas "run"

run_inicial=1
run=5

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

C1_0,C2_0,C3_0,C4_0,C5_0,C6_0,C7_0,C8_0,C9_0,C10_0 = [],[],[],[],[],[],[],[],[],[]
C11_0,C12_0,C13_0,C14_0,C15_0,C16_0,C17_0,C18_0,C19_0,C20_0 = [],[],[],[],[],[],[],[],[],[]
C21_0,C22_0,C23_0,C24_0,C25_0,C26_0,C27_0,C28_0,C29_0,C30_0 = [],[],[],[],[],[],[],[],[],[]
C31_0,C32_0,C33_0,C34_0,C35_0,C36_0,C37_0,C38_0,C39_0,C40_0 = [],[],[],[],[],[],[],[],[],[]
C41_0,C42_0,C43_0,C44_0,C45_0,C46_0,C47_0 = [],[],[],[],[],[],[]

E_23 = [] #hcal_0 j=0


for j in range(0,56):
    for i in range(0,run-run_inicial+1):
        if j == 0:
            a = i*55+j
            L = []
            E_run=[]
            #print(g[a])
            with open(A[a],"r") as name:
                L.append(name.readlines())
            for x in range(439,len(L[0])): 
                    #print(x)
                if 'Binning' and 'CENT0.0' in L[0][x]:
                    #print(L[0][x])
                    C1_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.1'  in L[0][x]:
                    #print(L[0][x])
                    C2_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.2' in L[0][x]:
                    #print(L[0][x])
                    C3_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.3' in L[0][x]:
                    #print(L[0][x])
                    C4_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.4' in L[0][x]:
                    #print(L[0][x])
                    C5_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.5' in L[0][x]:
                    #print(L[0][x])
                    C6_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.6' in L[0][x]:
                    #print(L[0][x])
                    C7_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.7' in L[0][x]:
                    #print(L[0][x])
                    C8_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.8' in L[0][x]:
                    #print(L[0][x])
                    C9_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.9' in L[0][x]:
                    #print(L[0][x])
                    C10_0.append(float(L[0][x+1].lstrip().rstrip('\n')))

                    
                if 'Binning' and 'CENT0.10' in L[0][x]:
                    #print(L[0][x])
                    C11_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                  
                if 'Binning' and 'CENT0.11' in L[0][x]:
                    #print(L[0][x])
                    C12_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.12' in L[0][x]:
                    #print(L[0][x])
                    C13_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.13' in L[0][x]:
                    #print(L[0][x])
                    C14_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                       
                if 'Binning' and 'CENT0.14' in L[0][x]:
                    #print(L[0][x])
                    C15_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.15' in L[0][x]:
                    #print(L[k][0][x])
                    C16_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.16' in L[0][x]:
                    #print(L[k][0][x])
                    C17_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.17' in L[0][x]:
                    #print(L[0][x])
                    C18_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.18' in L[0][x]:
                    #print(L[k][0][x])
                    C19_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.19' in L[0][x]:
                    #print(L[k][0][x])
                    C20_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                        
                if 'Binning' and 'CENT0.20' in L[0][x]:
                    #print(L[k][0][x])
                    C21_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.21' in L[0][x]:
                    #print(L[k][0][x])
                    C22_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.22' in L[0][x]:
                    #print(L[k][0][x])
                    C23_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.23' in L[0][x]:
                    #print(L[k][0][x])
                    C24_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.24' in L[0][x]:
                    #print(L[k][0][x])
                    C25_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.25' in L[0][x]:
                    #print(L[k][0][x])
                    C26_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.26' in L[0][x]:
                    #print(L[0][x])
                    C27_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.27' in L[0][x]:
                    #print(L[k][0][x])
                    C28_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.28' in L[0][x]:
                    #print(L[k][0][x])
                    C29_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.29' in L[0][x]:
                    #print(L[0][x])
                    C30_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.30' in L[0][x]:
                    #print(L[k][0][x])
                    C31_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.31' in L[0][x]:
                    #print(L[k][0][x])
                    C32_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.32' in L[0][x]:
                    #print(L[0][x])
                    C33_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.33' in L[0][x]:
                    #print(L[k][0][x])
                    C34_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.34' in L[0][x]:
                    #print(L[k][0][x])
                    C35_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.35' in L[0][x]:
                    #print(L[k][0][x])
                    C36_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.36' in L[0][x]:
                    #print(L[k][0][x])
                    C37_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.37' in L[0][x]:
                    #print(L[k][0][x])
                    C38_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.38' in L[0][x]:
                    #print(L[k][0][x])
                    C39_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.39' in L[0][x]:
                    #print(L[k][0][x])
                    C40_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                    
                        
                if 'Binning' and 'CENT0.40' in L[0][x]:
                    #print(L[0][x])
                    C41_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.41' in L[0][x]:
                    #print(L[k][0][x])
                    C42_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.42' in L[0][x]:
                    #print(L[k][0][x])
                    C43_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.43' in L[0][x]:
                    #print(L[0][x])
                    C44_0.append(float(L[0][x+1].lstrip().rstrip('\n')))                        
                if 'Binning' and 'CENT0.44' in L[0][x]:
                    #print(L[k][0][x])
                    C45_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.45' in L[0][x]:
                    #print(L[k][0][x])
                    C46_0.append(float(L[0][x+1].lstrip().rstrip('\n')))
                if 'Binning' and 'CENT0.46' in L[0][x]:
                    #print(L[k][0][x])
                    C47_0.append(float(L[0][x+1].lstrip().rstrip('\n')))

E_23=[]

for j in range(0,78):
    for i in range(run-run_inicial+1):
        if j == 0:
            a = i*55+j
            L = []
            E_run = []
            print(A[a])
            with open(A[a],"r") as name:
                L.append(
                    name.readlines())
                for x in range(len(L[0])):
                    #print(x)
                    if 'Binning n:' in L[0][x] and 'Binning n:  153,' not in L[0][x]:
                        #print(L[0][x])
                        E_run.append(float(L[0][x+1].lstrip().rstrip('\n')))
                E_23.append(E_run)

# Número de capas
numero_sublistas = 47

# Inicializa una lista de sublistas vacías
H0 = [[] for _ in range(numero_sublistas)]

# Agrega los elementos a las sublistas en orden
for j in range(0,run-run_inicial+1):
    for i, dato in enumerate(E_23[j]):
        indice_sublista = i % numero_sublistas  # Calcula el índice de la sublista
        H0[indice_sublista].append(dato)

E_23= pd.DataFrame()
for i in range(1,48):
    E_23[f'C{i}_0'] = H0[i-1]

#archivo csv para capa a capa de plastico centellador
E_23.to_csv('Energy_Hcal0.csv',index = False )


# Calcular la suma de las columnas (capas) y crear un nuevo DataFrame
df_total_sum = pd.DataFrame(E_23.sum(axis=1), columns=['HCAL0'])

# Mostrar el nuevo DataFrame
print(df_total_sum)

# Guardar el nuevo DataFrame en un archivo CSV
df_total_sum.to_csv('Hcal0_Total.csv', index=False)

# Mensaje de confirmación
print("Archivo 'Hcal0_Total.csv' generado correctamente.")
