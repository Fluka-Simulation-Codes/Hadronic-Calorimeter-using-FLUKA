import pandas as pd
import ROOT
import csv
from array import array

# Factor de corrección
sampling_fraction = 9

# Leer archivos CSV
df_total_sum_hcal0 = pd.read_csv('Hcal0_Total.csv')
df_total_sum_hcal1 = pd.read_csv('Hcal1_Total.csv')
df_total_sum_hcal2 = pd.read_csv('Hcal2_Total.csv')

# Renombrar columnas para evitar conflictos al concatenar
df_total_sum_hcal0.columns = ['HCAL0']
df_total_sum_hcal1.columns = ['HCAL1']
df_total_sum_hcal2.columns = ['HCAL2']

# Concatenar y sumar columnas
df_HCAL = pd.concat([df_total_sum_hcal0, df_total_sum_hcal1, df_total_sum_hcal2], axis=1)
df_HCAL['total_sum_HCAL'] = df_HCAL.sum(axis=1)

# Aplicar factor de corrección
df_HCAL = df_HCAL * sampling_fraction

# Guardar como CSV
df_HCAL.to_csv('HCAL_output.csv', index=False)

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('HCAL_output.csv')

# Crear archivo ROOT
root_file = ROOT.TFile("HCAL_output.root", "RECREATE")
tree = ROOT.TTree("HCAL_Tree", "Tree con datos del archivo CSV de HCAL")

# Crear variables en ROOT
col_HCAL0, col_HCAL1, col_HCAL2, col_total_sum_HCAL = [array('f', [0]) for _ in range(4)]
tree.Branch("HCAL0", col_HCAL0, "HCAL0/F")
tree.Branch("HCAL1", col_HCAL1, "HCAL1/F")
tree.Branch("HCAL2", col_HCAL2, "HCAL2/F")
tree.Branch("total_sum_HCAL", col_total_sum_HCAL, "total_sum_HCAL/F")

# Llenar el TTree
for _, row in df.iterrows():
    col_HCAL0[0], col_HCAL1[0], col_HCAL2[0], col_total_sum_HCAL[0] = row
    tree.Fill()

# Escribir TTree
tree.Write()

# Crear histogramas
num_bins = 50
min_range, max_range = 0, 100  # Establecer rango fijo

Energy_HCAL0 = ROOT.TH1F("Energy_HCAL0", "Energy Distribution in HCAL0", num_bins, min_range, max_range)
Energy_HCAL1 = ROOT.TH1F("Energy_HCAL1", "Energy Distribution in HCAL1", num_bins, min_range, max_range)
Energy_HCAL2 = ROOT.TH1F("Energy_HCAL2", "Energy Distribution in HCAL2", num_bins, min_range, max_range)
Energy_total_sum = ROOT.TH1F("Energy_total_sum", "Total Energy Distribution in HCAL", num_bins, min_range, max_range)

# Llenar histogramas
tree.Draw("HCAL0 >> Energy_HCAL0")
tree.Draw("HCAL1 >> Energy_HCAL1")
tree.Draw("HCAL2 >> Energy_HCAL2")
tree.Draw("total_sum_HCAL >> Energy_total_sum")

# Guardar histogramas como imágenes
for canvas, hist, name in [
    ("canvas_HCAL0", Energy_HCAL0, "Deposited_Energy_HCAL0_log.png"),
    ("canvas_HCAL1", Energy_HCAL1, "Deposited_Energy_HCAL1_log.png"),
    ("canvas_HCAL2", Energy_HCAL2, "Deposited_Energy_HCAL2_log.png"),
    ("canvas_total_sum", Energy_total_sum, "Deposited_Energy_Total_HCAL_log.png"),
]:
    c = ROOT.TCanvas(canvas, canvas, 800, 600)
    c.SetLogy()
    hist.Draw()
    c.SaveAs(name)

# Cerrar archivo ROOT
root_file.Close()

print("Histogramas guardados exitosamente en escala logarítmica.")


