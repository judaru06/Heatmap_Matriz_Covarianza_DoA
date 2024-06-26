import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from ast import literal_eval

script_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta del script actual
parent_dir = os.path.dirname(script_dir)  # Subir un nivel al directorio padre
srcs_dir = os.path.join(parent_dir, 'srcs')  # Ruta al directorio 'srcs'
sys.path.append(srcs_dir)

# Importar las funciones
from Data_Organization_Conversion import prepare_and_save
from Calculating_descriptive_statistics import process_data

class ComplexMatrixParser:
    def __init__(self, expected_size=144):
        self.expected_size = expected_size

    def parse(self, matrix_str):
        print("Parsing matrix...")
        matrix_str = matrix_str.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '')
        numbers = re.findall(r'[\+\-]?\d*\.?\d*e?[\+\-]?\d*[+-]\d*\.?\d*e?[\+\-]?\d*j', matrix_str)
        complex_numbers = [complex(num) for num in numbers]
        if len(complex_numbers) != self.expected_size:
            print(f"Extracted numbers: {numbers}")
            print(f"Complex numbers: {complex_numbers}")
            raise ValueError(f"Expected {self.expected_size} complex numbers, but got {len(complex_numbers)}")
        return np.array(complex_numbers).reshape(int(np.sqrt(self.expected_size)), int(np.sqrt(self.expected_size)))

class DataHandler:
    def __init__(self, filepath):
        print(f"Initializing DataHandler with file: {filepath}")
        self.data = pd.read_csv(filepath)
        self.parser = ComplexMatrixParser()

    def parse_matrices(self, column_name):
        print("Parsing matrices...")
        self.data['parsed_matrices'] = self.data[column_name].apply(self.parser.parse)

    def get_real_imaginary_parts(self):
        print("Getting real and imaginary parts...")
        real_parts = np.array([m.real for m in self.data['parsed_matrices']])
        imaginary_parts = np.array([m.imag for m in self.data['parsed_matrices']])
        return real_parts, imaginary_parts

    def get_ang_values(self):
        print("Getting angle values...")
        return self.data['ang'].values

class MatrixVisualizer:
    def __init__(self, save_path):
        self.save_path = save_path

    def plot_heatmaps(self, real_matrices, imag_matrices, ang_values, num_figures):
        sns.set(style="white")
        for i in range(num_figures):
            angle = str(ang_values[i]).replace('[', '_').replace(']', '').replace(' ', '').replace('\n', '')
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(real_matrices[i], ax=ax, cmap='gray', annot=False, cbar=False, square=True)
            plt.tight_layout()
            plt.savefig(os.path.join(self.save_path, f"heatmap_real_{i+1}_ang_{angle}.png"))
            plt.close()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(imag_matrices[i], ax=ax, cmap='gray', annot=False, cbar=False, square=True)
            plt.tight_layout()
            plt.savefig(os.path.join(self.save_path, f"heatmap_imaginary_{i+1}_ang_{angle}.png"))
            plt.close()

def main():
    print("Preparando y guardando los archivos CSV necesarios...")
    prepare_and_save()  # Esto preparará y guardará los archivos CSV necesarios

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Ajustar para acceder al directorio base del proyecto
    data_dir = os.path.join(base_dir, "data")
    results_dir = os.path.join(base_dir, "results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f"Directory {results_dir} created.")

    # Procesar y calcular estadísticas
    input_filepath = os.path.join(data_dir, 'music_data_1_angles.csv')
    output_filepath = os.path.join(data_dir, 'processed_data.h5')
    stats_csv_filepath = os.path.join(results_dir, 'statistics.csv')

    print("Procesando datos...")
    process_data(input_filepath, output_filepath, stats_csv_filepath)
    print("Datos procesados y estadísticas calculadas.")

    # Visualizar las matrices de datos
    print("Visualizando matrices de datos...")
    handlers = [DataHandler(os.path.join(data_dir, f'music_data_{i}_angles.csv')) for i in range(1, 6)]
    for i, handler in enumerate(handlers, start=1):
        print(f"Processing file music_data_{i}_angles.csv")
        handler.parse_matrices('Rx')
        real_parts, imaginary_parts = handler.get_real_imaginary_parts()
        ang_values = handler.get_ang_values()
        visualizer = MatrixVisualizer(os.path.join(results_dir, f"Angulo_{i}"))
        if not os.path.exists(visualizer.save_path):
            os.makedirs(visualizer.save_path)
            print(f"Directory {visualizer.save_path} created.")
        visualizer.plot_heatmaps(real_parts, imaginary_parts, ang_values, num_figures=min(8, len(ang_values)))
    print("Visualización completada.")

if __name__ == "__main__":
    main()