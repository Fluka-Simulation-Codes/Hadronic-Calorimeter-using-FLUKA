# Objetivo del Documento

Este documento se publica con el propósito de compartir los códigos desarrollados para analizar la energía depositada en las simulaciones del Calorímetro Hadronico (HCAL) del experimento NA64, utilizando el software FLUKA.

# Descripción General

 Los códigos presentados aquí cumplen dos funciones principales: 

    Generación del Dataset de Energía Deposita por el HCAL
    FLUKA genera los resultados de las simulaciones en archivos con extensión .fort, los cuales contienen la información detallada de la energía depositada en las diferentes capas del calorímetro.

    Para procesar estos archivos, se desarrolló un código específico que:

        1. Lee los archivos *.fort* generados por FLUKA.

        2. Extrae la energía depositada en cada capa del calorímetro.

        3. Organiza esta información de forma estructurada para construir un dataset, donde cada evento de simulación queda representado por las energías depositadas capa a capa.

# Procesamiento de Datos para Análisis Posteriores

Una vez generado el dataset, este puede ser utilizado para realizar distintos tipos de análisis, como el estudio de la distribución de la energía, la eficiencia de detección por capas, y comparaciones entre simulaciones y datos experimentales.

# Importancia del Proceso

La correcta extracción y organización de la energía depositada en las capas del HCAL es un paso fundamental para poder interpretar y validar las simulaciones realizadas en FLUKA, permitiendo así un análisis detallado del desempeño del detector en diferentes condiciones.

Este trabajo es parte de mi tesis de Pregrado de Licenciatura en Física de la Universidad Andres Bello (Santiago)

Pascale.-
