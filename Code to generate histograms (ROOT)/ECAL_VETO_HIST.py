 
import ROOT
import numpy as np
import pandas as pd
import os
from array import array

# Leer el archivo CSV en un DataFrame de pandas
df_total_sum_ECAL = pd.read_csv('Ecal_Veto.csv')

# Guardar en un nuevo archivo CSV si es necesario
df_total_sum_ECAL.to_csv('ECAL_VETO_output.csv', index=False)

# Definir los nombres de los archivos CSV y ROOT
csv_file_name = "ECAL_VETO_output.csv"
root_file_name = "ECAL_VETO_output.root"

# Crear el archivo ROOT
root_file = ROOT.TFile(root_file_name, "RECREATE")

# Crear un TTree
tree = ROOT.TTree("ECAL_VETO_Tree", "Tree con datos del archivo CSV")

# Crear variables en ROOT para almacenar los valores de cada columna del CSV
col_4X_0 = array('f', [0])
col_36X_0 = array('f', [0])
col_40X_0 = array('f', [0])
col_VETO = array('f', [0])

# Asignar las ramas del TTree a las variables correspondientes
tree.Branch("4X_0", col_4X_0, "4X_0/F")
tree.Branch("36X_0", col_36X_0, "36X_0/F")
tree.Branch("40X_0", col_40X_0, "40X_0/F")
tree.Branch("VETO", col_VETO, "VETO/F")

# Llenar el TTree con los datos del DataFrame
for i, row in df_total_sum_ECAL.iterrows():
    col_4X_0[0] = row['4X_0']
    col_36X_0[0] = row['36X_0']
    col_40X_0[0] = row['40X_0']
    col_VETO[0] = row['VETO']
    tree.Fill()

# Escribir el TTree en el archivo ROOT
tree.Write()
root_file.Close()

# Función para calcular el ancho del bin y el número de bins
def calcular_bin_width(data):
    num_bins = int(np.sqrt(len(data)))
    bin_width = (data.max() - data.min()) / num_bins
    return bin_width, num_bins

# Calcular el ancho del bin y el número de bins para cada conjunto de datos
bin_width_4X_0, n_bins_4X_0 = calcular_bin_width(df_total_sum_ECAL['4X_0'])
bin_width_36X_0, n_bins_36X_0 = calcular_bin_width(df_total_sum_ECAL['36X_0'])
bin_width_40X_0, n_bins_40X_0 = calcular_bin_width(df_total_sum_ECAL['40X_0'])
bin_width_VETO, n_bins_VETO = calcular_bin_width(df_total_sum_ECAL['VETO'])

# Reabrir el archivo ROOT para acceder al TTree
root_file = ROOT.TFile(root_file_name)
tree = root_file.Get("ECAL_VETO_Tree")

# Crear histogramas con el número de bins y ancho calculado
Energy_4X_0 = ROOT.TH1F("Energy_4X_0", "Deposited Energy Preshower", n_bins_4X_0, 0, n_bins_4X_0 * bin_width_4X_0)
Energy_36X_0 = ROOT.TH1F("Energy_36X_0", "Deposited Energy Shower", n_bins_36X_0, 0, n_bins_36X_0 * bin_width_36X_0)
Energy_40X_0 = ROOT.TH1F("Energy_40X_0", "Deposited Energy Total ECAL", n_bins_40X_0, 0, n_bins_40X_0 * bin_width_40X_0)
Energy_VETO = ROOT.TH1F("Energy_VETO", "Deposited Energy VETO", n_bins_VETO, 0, n_bins_VETO * bin_width_VETO)

# Definir títulos de los ejes
# Definir títulos de los ejes
Energy_4X_0.SetXTitle("Energy in 4X_0 [GeV]")
Energy_4X_0.SetYTitle("Events")
Energy_36X_0.SetXTitle("Energy in 36X_0 [GeV]")
Energy_36X_0.SetYTitle("Events")
Energy_40X_0.SetXTitle("Energy in 40X_0 [GeV]")
Energy_40X_0.SetYTitle("Events")
Energy_VETO.SetXTitle("Energy in Veto [GeV]")
Energy_VETO.SetYTitle("Events")

# Llenar los histogramas con los datos del TTree
tree.Draw("4X_0 >> Energy_4X_0")
tree.Draw("36X_0 >> Energy_36X_0")
tree.Draw("40X_0 >> Energy_40X_0")
tree.Draw("VETO >> Energy_VETO")

# Dibujar cada histograma sin escala logarítmica y guardarlos como imágenes
canvas_4X_0 = ROOT.TCanvas("canvas_4X_0", "Canvas 4X_0", 800, 600)
# Activar la escala logarítmica en el eje Y
#canvas_4X_0.SetLogy()

Energy_4X_0.Draw()
canvas_4X_0.SaveAs("Deposited_Energy_4X0.png")

canvas_36X_0 = ROOT.TCanvas("canvas_36X_0", "Canvas 36X_0", 800, 600)
# Activar la escala logarítmica en el eje Y
#canvas_36X_0.SetLogy()

Energy_36X_0.Draw()
canvas_36X_0.SaveAs("Deposited_Energy_36X0.png")

canvas_40X_0 = ROOT.TCanvas("canvas_40X_0", "Canvas 40X_0", 800, 600)
# Activar la escala logarítmica en el eje Y
#canvas_40X_0.SetLogy()

Energy_40X_0.Draw()
canvas_40X_0.SaveAs("Deposited_Energy_40X0.png")

canvas_VETO = ROOT.TCanvas("canvas_VETO", "Canvas VETO", 800, 600)
# Activar la escala logarítmica en el eje Y
#canvas_VETO.SetLogy()

Energy_VETO.Draw()
canvas_VETO.SaveAs("Deposited_Energy_VETO.png")

# Cerrar el archivo ROOT
root_file.Close()

print(f"Histograms created with calculated bin width and number of bins.")

