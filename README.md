# Heatmap_Matriz_Covarianza_DoA
Creación de mapas de calor en escala de grises para la estimación del DoA
# SCIENTIFIC COMPUTING

Std. Juan David Rojas Usuga

## Descripción General del Proyecto

Este proyecto tiene como objetivo analizar matrices complejas extraídas de señales RF utilizando diferentes ángulos. Se realizan varios análisis estadísticos y visualizaciones para comprender mejor los datos. El proyecto está organizado en varias carpetas que contienen scripts y datos necesarios para ejecutar los análisis.

## Configuración del Proyecto

1. **Clonar el Repositorio**:
   ```bash
   git clone <URL del repositorio>
   cd <nombre del repositorio>

2. Instalar Dependencias:
Se requiere Python 3.x. Para instalar las dependencias, ejecute:
   ```bash
      pip install -r requirements.txt

## La estructura del repositorio es el siguiente:
   ```bash
         C:.
         | .gitignore
         | output.txt
         | README.md
         | requirements.txt
         |
         +---data
         | datos_MUSIC_3.csv
         | music_data_1_angles.csv
         | music_data_2_angles.csv
         | music_data_3_angles.csv
         | music_data_4_angles.csv
         | music_data_5_angles.csv
         |
         +---results
         |
         +---srcs
         | Calculating_descriptive_statistics.py
         | Data_Organization_Conversion.py
         | Heatmap_Matriz_Covarianza_DoA.py
         |
         ---test
         Test_Heatmap_Matriz_Covarianza_DoA.py
## Ejecución de los Análisis
   Codigo de ejemplo:
   test/Test_Heatmap_Matriz_Covarianza_DoA.py
