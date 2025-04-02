import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

## para ejecutar este codigo necesitamos saber:
## 1) Cuantas carpetas "run" tiene la simulacion
## 2) direccion del Directorio de trabajo, donde se encuentran las carpetas "run"

#run inicial 
#run final
run_inicial=1
run=5

ruta1 = "./round1"
ruta2 = "./prueba/arca.institutosaphir.cl/index.php/s/Gq4pkbay8inGRpD/Trabajo_Pascal_Marcelo/NA64_runs/Ecal_Veto_Hcal_1E7/round2"

Cluster =ruta1+ruta2
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

# # ECAL Preshower contiene 37 capas
S1 , S2 , S3 , S4 , S5 , S6 , S7 , S8 , S9 , S10 = [] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[]
S11 , S12 , S13 , S14 , S15 , S16 , S17 , S18 , S19 , S20 = [] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[]
S21 , S22 , S23 , S24 , S25 , S26 , S27 , S28 , S29 , S30 = [] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[] ,[]
S31 , S32 , S33 , S34 , S35 , S36 , S37 = [] ,[] ,[] ,[] ,[] ,[] ,[]


for j in range(0, 56):
    for i in range(0, run - run_inicial + 1):  # números de run
        if j == 4:  # archivo .27
            a = i * 55 + j
            L = []
            # print(A[a])
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S1' in L[0][x]:
                    # print(L[k][0][x])
                    S1.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S2' in L[0][x]:
                    # print(L[k][0][x])
                    S2.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S3' in L[0][x]:
                    # print(L[k][0][x])
                    S3.append(float(L[0][x + 1].lstrip().rstrip('\n')))


        if j == 5:  # archivo .28
            a = i * 55 + j
            L = []
            # print(g[a])
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S4' in L[0][x]:
                    # print(L[k][0][x])
                    S4.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S5' in L[0][x]:
                    # print(L[k][0][x])
                    S5.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S6' in L[0][x]:
                    # print(L[k][0][x])
                    S6.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 6:  # archivo .29
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S7' in L[0][x]:
                    # print(L[k][0][x])
                    S7.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S8' in L[0][x]:
                    # print(L[k][0][x])
                    S8.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S9' in L[0][x]:
                    # print(L[k][0][x])
                    S9.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 7:  # archivo .30
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S10' in L[0][x]:
                    # print(L[k][0][x])
                    S10.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S11' in L[0][x]:
                    # print(L[k][0][x])
                    S11.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S12' in L[0][x]:
                    # print(L[k][0][x])
                    S12.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 8:  # archivo .31
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S13' in L[0][x]:
                    # print(L[k][0][x])
                    S13.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S14' in L[0][x]:
                    # print(L[k][0][x])
                    S14.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S15' in L[0][x]:
                    # print(L[k][0][x])
                    S15.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 9:  # archivo .32
            a = i * 55 + j
            L = []
            # print(A[a])
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S16' in L[0][x]:
                    # print(L[k][0][x])
                    S16.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S17' in L[0][x]:
                    # print(L[k][0][x])
                    S17.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S18' in L[0][x]:
                    # print(L[k][0][x])
                    S18.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 10:  # archivo .33
            a = i * 55 + j
            L = []
            # print(g[a])
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S19' in L[0][x]:
                    # print(L[k][0][x])
                    S19.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S20' in L[0][x]:
                    # print(L[k][0][x])
                    S20.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S21' in L[0][x]:
                    # print(L[k][0][x])
                    S21.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 11:  # archivo .34 
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S22' in L[0][x]:
                    # print(L[k][0][x])
                    S22.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S23' in L[0][x]:
                    # print(L[k][0][x])
                    S23.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S24' in L[0][x]:
                    # print(L[k][0][x])
                    S24.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 12:  # archivo .35
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S25' in L[0][x]:
                    # print(L[k][0][x])
                    S25.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S26' in L[0][x]:
                    # print(L[k][0][x])
                    S26.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S27' in L[0][x]:
                    # print(L[k][0][x])
                    S27.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 13:  # archivo .36
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S28' in L[0][x]:
                    # print(L[k][0][x])
                    S28.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S29' in L[0][x]:
                    # print(L[k][0][x])
                    S29.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S30' in L[0][x]:
                    # print(L[k][0][x])
                    S30.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 14:  # archivo .37
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S31' in L[0][x]:
                    # print(L[k][0][x])
                    S31.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S32' in L[0][x]:
                    # print(L[k][0][x])
                    S32.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S33' in L[0][x]:
                    # print(L[k][0][x])
                    S33.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 15:  # archivo .38
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                # print(x)
                if 'Binning' and 'S34' in L[0][x]:
                    # print(L[k][0][x])
                    S34.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S35' in L[0][x]:
                    # print(L[k][0][x])
                    S35.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S36' in L[0][x]:
                    # print(L[k][0][x])
                    S36.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 16:  # archivo .39
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(len(L[0])):
                # print(x)
                if 'Binning' in L[0][x]:
                    # print(L[k][0][x])
                    S37.append(float(L[0][x + 1].lstrip().rstrip('\n')))

S38,S39,S40=[],[],[]
S41,S42,S43,S44,S45,S46,S47,S48,S49,S50=[],[],[],[],[],[],[],[],[],[]
S51,S52,S53,S54,S55,S56,S57,S58,S59,S60=[],[],[],[],[],[],[],[],[],[]
S61,S62,S63,S64,S65,S66,S67,S68,S69,S70=[],[],[],[],[],[],[],[],[],[]
S71,S72,S73,S74,S75,S76,S77,S78,S79,S80=[],[],[],[],[],[],[],[],[],[]
S81,S82,S83,S84,S85,S86,S87,S88,S89,S90=[],[],[],[],[],[],[],[],[],[]
S91,S92,S93,S94,S95,S96,S97,S98,S99,S100=[],[],[],[],[],[],[],[],[],[]
S101,S102,S103,S104,S105,S106,S107,S108,S109,S110=[],[],[],[],[],[],[],[],[],[]
S111,S112,S113,S114,S115,S116,S117,S118,S119,S120=[],[],[],[],[],[],[],[],[],[]
S121,S122,S123,S124,S125,S126,S127,S128,S129,S130=[],[],[],[],[],[],[],[],[],[]
S131,S132,S133,S134,S135,S136,S137,S138,S139,S140=[],[],[],[],[],[],[],[],[],[]
S141,S142,S143,S144,S145,S146,S147,S148,S149,S150=[],[],[],[],[],[],[],[],[],[]

for j in range(0, 56):
    for i in range(0, run):  # numeros de run
        if j == 17:  # archivo .40
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S38' in L[0][x]:
                    S38.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S39' in L[0][x]:
                    S39.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S40' in L[0][x]:
                    S40.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 18:  # archivo .41
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S41' in L[0][x]:
                    S41.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S42' in L[0][x]:
                    S42.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S43' in L[0][x]:
                    S43.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 19:  # archivo .42
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S44' in L[0][x]:
                    S44.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S45' in L[0][x]:
                    S45.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S46' in L[0][x]:
                    S46.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 20:  # archivo .43
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S47' in L[0][x]:
                    S47.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S48' in L[0][x]:
                    S48.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S49' in L[0][x]:
                    S49.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 21:  # archivo .44
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S50' in L[0][x]:
                    S50.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S51' in L[0][x]:
                    S51.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S52' in L[0][x]:
                    S52.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 22:  # archivo .45
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S53' in L[0][x]:
                    S53.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S54' in L[0][x]:
                    S54.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S55' in L[0][x]:
                    S55.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 23:  # archivo .46
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S56' in L[0][x]:
                    S56.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S57' in L[0][x]:
                    S57.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S58' in L[0][x]:
                    S58.append(float(L[0][x + 1].lstrip().rstrip('\n')))

for j in range(0, 56):
    for i in range(0, run):  # numeros de run
        if j == 24:  # archivo .47
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S59' in L[0][x]:
                    S59.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S60' in L[0][x]:
                    S60.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S61' in L[0][x]:
                    S61.append(float(L[0][x + 1].lstrip().rstrip('\n')))

        if j == 25:  # archivo .48
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' and 'S62' in L[0][x]:
                    S62.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S63' in L[0][x]:
                    S63.append(float(L[0][x + 1].lstrip().rstrip('\n')))
                if 'Binning' and 'S64' in L[0][x]:
                    S64.append(float(L[0][x + 1].lstrip().rstrip('\n')))

for j in range(0, 56):
    for i in range(0, run):  # números de run
        if j == 26:  # archivo .49
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S65' in L[0][x]:
                    S65.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S66' in L[0][x]:
                    S66.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S67' in L[0][x]:
                    S67.append(float(L[0][x + 1].strip()))

        if j == 27:  # archivo .50
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S68' in L[0][x]:
                    S68.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S69' in L[0][x]:
                    S69.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S70' in L[0][x]:
                    S70.append(float(L[0][x + 1].strip()))

        if j == 28:  # archivo .51
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S71' in L[0][x]:
                    S71.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S72' in L[0][x]:
                    S72.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S73' in L[0][x]:
                    S73.append(float(L[0][x + 1].strip()))

        if j == 29:  # archivo .52
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S74' in L[0][x]:
                    S74.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S75' in L[0][x]:
                    S75.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S76' in L[0][x]:
                    S76.append(float(L[0][x + 1].strip()))

        if j == 30:  # archivo .53
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S77' in L[0][x]:
                    S77.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S78' in L[0][x]:
                    S78.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S79' in L[0][x]:
                    S79.append(float(L[0][x + 1].strip()))

        if j == 31:  # archivo .54
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S80' in L[0][x]:
                    S80.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S81' in L[0][x]:
                    S81.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S82' in L[0][x]:
                    S82.append(float(L[0][x + 1].strip()))

        if j == 32:  # archivo .55
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S83' in L[0][x]:
                    S83.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S84' in L[0][x]:
                    S84.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S85' in L[0][x]:
                    S85.append(float(L[0][x + 1].strip()))

        if j == 33:  # archivo .56
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S86' in L[0][x]:
                    S86.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S87' in L[0][x]:
                    S87.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S88' in L[0][x]:
                    S88.append(float(L[0][x + 1].strip()))

        if j == 34:  # archivo .57
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S89' in L[0][x]:
                    S89.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S90' in L[0][x]:
                    S90.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S91' in L[0][x]:
                    S91.append(float(L[0][x + 1].strip()))

        if j == 35:  # archivo .58
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S92' in L[0][x]:
                    S92.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S93' in L[0][x]:
                    S93.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S94' in L[0][x]:
                    S94.append(float(L[0][x + 1].strip()))

        if j == 36:  # archivo .59
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S95' in L[0][x]:
                    S95.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S96' in L[0][x]:
                    S96.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S97' in L[0][x]:
                    S97.append(float(L[0][x + 1].strip()))

for j in range(0, 56):
    for i in range(0, run):  # números de run
        if j == 37:  # archivo .60
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S98' in L[0][x]:
                    S98.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S99' in L[0][x]:
                    S99.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S100' in L[0][x]:
                    S100.append(float(L[0][x + 1].strip()))

        if j == 38:  # archivo .61
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S101' in L[0][x]:
                    S101.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S102' in L[0][x]:
                    S102.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S103' in L[0][x]:
                    S103.append(float(L[0][x + 1].strip()))

        if j == 39:  # archivo .62
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S104' in L[0][x]:
                    S104.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S105' in L[0][x]:
                    S105.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S106' in L[0][x]:
                    S106.append(float(L[0][x + 1].strip()))

        if j == 40:  # archivo .63
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S107' in L[0][x]:
                    S107.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S108' in L[0][x]:
                    S108.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S109' in L[0][x]:
                    S109.append(float(L[0][x + 1].strip()))

        if j == 41:  # archivo .64
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S110' in L[0][x]:
                    S110.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S111' in L[0][x]:
                    S111.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S112' in L[0][x]:
                    S112.append(float(L[0][x + 1].strip()))

        if j == 42:  # archivo .65
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S113' in L[0][x]:
                    S113.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S114' in L[0][x]:
                    S114.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S115' in L[0][x]:
                    S115.append(float(L[0][x + 1].strip()))

for j in range(0, 56):
    for i in range(0, run):  # números de run
        if j == 43:  # archivo .66
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S116' in L[0][x]:
                    S116.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S117' in L[0][x]:
                    S117.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S118' in L[0][x]:
                    S118.append(float(L[0][x + 1].strip()))

        if j == 44:  # archivo .67
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S119' in L[0][x]:
                    S119.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S120' in L[0][x]:
                    S120.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S121' in L[0][x]:
                    S121.append(float(L[0][x + 1].strip()))

        if j == 45:  # archivo .68
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S122' in L[0][x]:
                    S122.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S123' in L[0][x]:
                    S123.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S124' in L[0][x]:
                    S124.append(float(L[0][x + 1].strip()))

        if j == 46:  # archivo .69
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S125' in L[0][x]:
                    S125.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S126' in L[0][x]:
                    S126.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S127' in L[0][x]:
                    S127.append(float(L[0][x + 1].strip()))

        if j == 47:  # archivo .70
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S128' in L[0][x]:
                    S128.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S129' in L[0][x]:
                    S129.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S130' in L[0][x]:
                    S130.append(float(L[0][x + 1].strip()))

        if j == 48:  # archivo .71
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S131' in L[0][x]:
                    S131.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S132' in L[0][x]:
                    S132.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S133' in L[0][x]:
                    S133.append(float(L[0][x + 1].strip()))

for j in range(0, 56):
    for i in range(0, run):  # números de run
        if j == 49:  # archivo .72
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S134' in L[0][x]:
                    S134.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S135' in L[0][x]:
                    S135.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S136' in L[0][x]:
                    S136.append(float(L[0][x + 1].strip()))

        if j == 50:  # archivo .73
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S137' in L[0][x]:
                    S137.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S138' in L[0][x]:
                    S138.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S139' in L[0][x]:
                    S139.append(float(L[0][x + 1].strip()))

        if j == 51:  # archivo .74
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S140' in L[0][x]:
                    S140.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S141' in L[0][x]:
                    S141.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S142' in L[0][x]:
                    S142.append(float(L[0][x + 1].strip()))

        if j == 52:  # archivo .75
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S143' in L[0][x]:
                    S143.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S144' in L[0][x]:
                    S144.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S145' in L[0][x]:
                    S145.append(float(L[0][x + 1].strip()))

        if j == 53:  # archivo .76
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(35, len(L[0])):
                if 'Binning' in L[0][x] and 'S146' in L[0][x]:
                    S146.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S147' in L[0][x]:
                    S147.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S148' in L[0][x]:
                    S148.append(float(L[0][x + 1].strip()))

        if j == 54:  # archivo .77
            a = i * 55 + j
            L = []
            with open(A[a], "r") as name:
                L.append(name.readlines())
            for x in range(24, len(L[0])):
                if 'Binning' in L[0][x] and 'S149' in L[0][x]:
                    S149.append(float(L[0][x + 1].strip()))
                if 'Binning' in L[0][x] and 'S150' in L[0][x]:
                    S150.append(float(L[0][x + 1].strip()))


df = pd.DataFrame()
df['s1'] = S1
df['s2'] = S2
df['s3'] = S3
df['s4'] = S4
df['s5'] = S5
df['s6'] = S6
df['s7'] = S7
df['s8'] = S8
df['s9'] = S9
df['s10'] = S10
df['s11'] = S11
df['s12'] = S12
df['s13'] = S13
df['s14'] = S14
df['s15'] = S15
df['s16'] = S16
df['s17'] = S17
df['s18'] = S18
df['s19'] = S19
df['s20'] = S20
df['s21'] = S21
df['s22'] = S22
df['s23'] = S23
df['s24'] = S24
df['s25'] = S25
df['s26'] = S26
df['s27'] = S27
df['s28'] = S28
df['s29'] = S29
df['s30'] = S30
df['s31'] = S31
df['s32'] = S32
df['s33'] = S33
df['s34'] = S34
df['s35'] = S35
df['s36'] = S36
df['s37'] = S37

dk = pd.DataFrame()
dk['s38'] = S38
dk['s39'] = S39
dk['s40'] = S40
dk['s41'] = S41
dk['s42'] = S42
dk['s43'] = S43
dk['s44'] = S44
dk['s45'] = S45
dk['s46'] = S46
dk['s47'] = S47
dk['s48'] = S48
dk['s49'] = S49
dk['s50'] = S50
dk['s51'] = S51
dk['s52'] = S52
dk['s53'] = S53
dk['s54'] = S54
dk['s55'] = S55
dk['s56'] = S56
dk['s57'] = S57
dk['s58'] = S58
dk['s59'] = S59
dk['s60'] = S60
dk['s61'] = S61
dk['s62'] = S62
dk['s63'] = S63
dk['s64'] = S64
dk['s65'] = S65
dk['s66'] = S66
dk['s67'] = S67
dk['s68'] = S68
dk['s69'] = S69
dk['s70'] = S70
dk['s71'] = S71
dk['s72'] = S72
dk['s73'] = S73
dk['s74'] = S74
dk['s75'] = S75
dk['s76'] = S76
dk['s77'] = S77
dk['s78'] = S78
dk['s79'] = S79

dm = pd.DataFrame()
dm['s80'] = S80
dm['s81'] = S81
dm['s82'] = S82
dm['s83'] = S83
dm['s84'] = S84
dm['s85'] = S85
dm['s86'] = S86
dm['s87'] = S87
dm['s88'] = S88
dm['s89'] = S89
dm['s90'] = S90
dm['s91'] = S91
dm['s92'] = S92
dm['s93'] = S93
dm['s94'] = S94
dm['s95'] = S95
dm['s96'] = S96
dm['s97'] = S97
dm['s98'] = S98
dm['s99'] = S99
dm['s100'] = S100
dm['s101'] = S101
dm['s102'] = S102
dm['s103'] = S103
dm['s104'] = S104
dm['s105'] = S105
dm['s106'] = S106
dm['s107'] = S107
dm['s108'] = S108
dm['s109'] = S109

dn = pd.DataFrame()
dn['s110'] = S110
dn['s111'] = S111
dn['s112'] = S112
dn['s113'] = S113
dn['s114'] = S114
dn['s115'] = S115
dn['s116'] = S116
dn['s117'] = S117
dn['s118'] = S118
dn['s119'] = S119
dn['s120'] = S120
dn['s121'] = S121
dn['s122'] = S122
dn['s123'] = S123
dn['s124'] = S124
dn['s125'] = S125
dn['s126'] = S126
dn['s127'] = S127
dn['s128'] = S128
dn['s129'] = S129
dn['s130'] = S130
dn['s131'] = S131
dn['s132'] = S132
dn['s133'] = S133
dn['s134'] = S134
dn['s135'] = S135
dn['s136'] = S136
dn['s137'] = S137
dn['s138'] = S138
dn['s139'] = S139

dl = pd.DataFrame()
dl['s140'] = S140
dl['s141'] = S141
dl['s142'] = S142
dl['s143'] = S143
dl['s144'] = S144
dl['s145'] = S145
dl['s146'] = S146
dl['s147'] = S147
dl['s148'] = S148
dl['s149'] = S149
dl['s150'] = S150

Ecal = [dk, dm, dn, dl]

E_1_16 = pd.concat(Ecal,axis=1)

Ecal = pd.DataFrame()
Ecal = pd.concat([df, E_1_16], axis=1)

Ecal

# Guardar el DataFrame ECAL en un archivo CSV
# Entrega capa a capa
Ecal.to_csv('Ecal.csv', index=False)

##Veto
## para ejecutar este codigo necesitamos saber:
## 1) Cuantas carpetas "run" tiene la simulacion
## 2) direccion del Directorio de trabajo, donde se encuentran las carpetas "run"


run_inicial=1
run=5

ruta1 = "./round1"
ruta2 = "./prueba/arca.institutosaphir.cl/index.php/s/Gq4pkbay8inGRpD/Trabajo_Pascal_Marcelo/NA64_runs/Ecal_Veto_Hcal_1E7/round2"

Cluster =ruta1+ruta2
Cluster


for i in range(run_inicial,run + 1):
    for j in range(23,78):
        if i < 10:
            #print(i)
            a = ruta1 +"/run"+str(i)
            #print(a) 
            b = "/ex_NA64_%d001_fort.%d" % (i,j)
            print(a+b)
            if os.path.exists(a+b) == True:#comprobamos si existe la direccion creada
                A.append(a+b)
                
        if i > 9:
            #print(i)
            a = ruta2 +"/run"+str(i)
            #print(a) 
            b = "/ex_NA64_%d001_fort.%d" % (i,j)
            #print(a+b)
            if os.path.exists(a+b) == True:#comprobamos si existe la direccion creada
                A.append(a+b)

A

V = []

for j in range(0,56):
    for i in range(0,run-run_inicial +1):
        if j == 1:
            a = i*55+j
            L = []
            E_run=[]
            #print(g[a])
            with open(A[a],"r") as name:
                L.append(name.readlines())
            for x in range(16,len(L[0])): 
                if 'Binning' and 'Veto' in L[0][x]:
                    #print(L[0][x])
                    V.append(float(L[0][x+1].lstrip().rstrip('\n')))          



# DataFrames vacíos
Ecal = pd.DataFrame()
HCAL = pd.DataFrame()
NA64 = pd.DataFrame()

# Calcular las sumas
sum_E_1_16 = df.sum(axis=1)
sum_E_17_150 = df.sum(axis=1)

# Asignar valores a ECAL
Ecal['4X_0'] = sum_E_1_16
Ecal['36X_0'] = sum_E_17_150 
Ecal['40X_0'] = Ecal['4X_0'] + Ecal['36X_0']
Ecal['VETO'] = V  # Asignar el valor de E_24 a la columna 'VETO'

Ecal

#Entrega capa total
Ecal.to_csv('Ecal_Veto.csv', index=False)



