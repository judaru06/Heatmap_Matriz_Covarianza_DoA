import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from ast import literal_eval
from Data_Organization_Conversion import prepare_and_save  # Asegúrate de que el nombre de archivo e importación sean correctos

class ComplexMatrixParser:
    def __init__(self, expected_size=144):
        self.expected_size = expected_size

    def parse(self, matrix_str):
        matrix_str = matrix_str.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '')
        numbers = re.findall(r'[\+\-]?\d*\.?\d*e?[\+\-]?\d*[+-]\d*\.?\d*e?[\+\-]?\d*j', matrix_str)
        complex_numbers = [complex(num.replace('+-', '-').replace('++', '+').replace('-+', '-').replace('--', '+')) for num in numbers]
        if len(complex_numbers) != self.expected_size:
            raise ValueError(f"Expected {self.expected_size} complex numbers, but got {len(complex_numbers)}")
        return np.array(complex_numbers).reshape(int(np.sqrt(self.expected_size)), int(np.sqrt(self.expected_size)))

class DataHandler:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)
        self.parser = ComplexMatrixParser()

    def parse_matrices(self, column_name):
        self.data['parsed_matrices'] = self.data[column_name].apply(self.parser.parse)

    def get_real_imaginary_parts(self):
        real_parts = np.array([m.real for m in self.data['parsed_matrices']])
        imaginary_parts = np.array([m.imag for m in self.data['parsed_matrices']])
        return real_parts, imaginary_parts

    def get_ang_values(self):
        return self.data['ang'].values

class MatrixVisualizer:
    def __init__(self, save_path):
        self.save_path = save_path

    def plot_heatmaps(self, real_matrices, imag_matrices, ang_values, num_figures):
        sns.set(style="white")
        for i in range(num_figures):
            # Limpiar el valor del ángulo para usarlo en el nombre del archivo
            angle = str(ang_values[i]).replace('[', '').replace(']', '').replace(' ', '').replace('\n', '')
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
    prepare_and_save()  # Esto preparará y guardará los archivos CSV necesarios

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "..", "data")
    results_dir = os.path.join(base_dir, "..", "results")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    handlers = [DataHandler(os.path.join(data_dir, f'music_data_{i}_angles.csv')) for i in range(1, 6)]
    for i, handler in enumerate(handlers, start=1):
        handler.parse_matrices('Rx')
        real_parts, imaginary_parts = handler.get_real_imaginary_parts()
        ang_values = handler.get_ang_values()
        visualizer = MatrixVisualizer(os.path.join(results_dir, f"Angulo_{i}"))
        if not os.path.exists(visualizer.save_path):
            os.makedirs(visualizer.save_path)
        visualizer.plot_heatmaps(real_parts, imaginary_parts, ang_values, num_figures=min(8, len(ang_values)))

if __name__ == "__main__":
    main()