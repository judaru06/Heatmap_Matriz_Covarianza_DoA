import re
import numpy as np
import pandas as pd
import h5py
import os
from scipy import stats

class ComplexMatrixParser:
    def __init__(self, expected_size=144):
        self.expected_size = expected_size

    def parse(self, matrix_str):
        matrix_str = matrix_str.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '')
        numbers = re.findall(r'[\+\-]?\d*\.?\d*e?[\+\-]?\d*[+-]\d*\.?\d*e?[\+\-]?\d*j', matrix_str)
        complex_numbers = [complex(num.replace('+-', '-').replace('++', '+').replace('-+', '-').replace('--', '+')) for num in numbers]

        if len(complex_numbers) != self.expected_size:
            print(f"Extracted numbers: {numbers}")
            print(f"Complex numbers: {complex_numbers}")
            raise ValueError(f"Expected {self.expected_size} complex numbers, but got {len(complex_numbers)}")

        return np.array(complex_numbers).reshape(12, 12)

class DataHandler:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)
        self.data['ang'] = self.data['ang'].apply(lambda x: float(re.sub(r'[^\d.-]', '', str(x))))
        self.parser = ComplexMatrixParser()

    def parse_matrices(self, column_name):
        self.data['parsed_matrices'] = self.data[column_name].apply(self.parser.parse)

    def get_real_imaginary_parts(self):
        real_parts = np.array([m.real for m in self.data['parsed_matrices']])
        imaginary_parts = np.array([m.imag for m in self.data['parsed_matrices']])
        return real_parts, imaginary_parts

    def get_ang_values(self):
        return self.data['ang'].values

    def save_to_hdf5(self, output_filepath):
        real_parts, imaginary_parts = self.get_real_imaginary_parts()
        ang_values = self.get_ang_values()

        with h5py.File(output_filepath, 'w') as f:
            f.create_dataset('ang', data=ang_values)
            f.create_dataset('real_parts', data=real_parts)
            f.create_dataset('imaginary_parts', data=imaginary_parts)

        print(f"Data successfully saved to {output_filepath}")

class HDF5DataHandler:
    def __init__(self, filepath):
        """
        Inicializamos la clase con la ruta al archivo HDF5.
        """
        self.filepath = filepath
        self.ang = None
        self.real_parts = None
        self.imaginary_parts = None

    def load_data(self):
        """
        Leemos los datos desde el archivo HDF5 y los almacena en atributos de la clase.
        """
        with h5py.File(self.filepath, 'r') as f:
            self.ang = f['ang'][:]
            self.real_parts = f['real_parts'][:]
            self.imaginary_parts = f['imaginary_parts'][:]

class StatisticsCalculator:
    def __init__(self, ang, real_parts, imaginary_parts):
        """
        Inicializamos la clase con los datos de 'ang', 'real_parts' e 'imaginary_parts'.
        """
        self.ang = ang
        self.real_parts = real_parts.flatten()
        self.imaginary_parts = imaginary_parts.flatten()

    def calculate_statistics(self, data):
        """
        Calculamos varias estadísticas descriptivas (media, mediana, moda, desviación estándar,
        varianza, mínimo, máximo y rango) para los datos de /content/music_data_1_angles.csv.
        """
        mean = np.mean(data)
        median = np.median(data)
        mode = stats.mode(data, axis=None)
        mode_value = mode.mode[0] if isinstance(mode.mode, np.ndarray) and mode.mode.size > 0 else mode.mode
        std = np.std(data)
        var = np.var(data)
        min_value = np.min(data)
        max_value = np.max(data)
        data_range = max_value - min_value
        return {
            'mean': mean,
            'median': median,
            'mode': mode_value,
            'std': std,
            'var': var,
            'min': min_value,
            'max': max_value,
            'range': data_range
        }

    def display_statistics(self, stats, name):
        """
        Mostramos las estadísticas calculadas para un conjunto de datos específico.
        """
        print(f"Estadísticos descriptivos para '{name}':")
        for key, value in stats.items():
            print(f"{key.capitalize()}: {value}")

    def calculate_and_display_all(self):
        """
        Calculamos y mostramos las estadísticas descriptivas para 'ang', 'real_parts' e 'imaginary_parts'.
        """
        ang_stats = self.calculate_statistics(self.ang)
        real_stats = self.calculate_statistics(self.real_parts)
        imag_stats = self.calculate_statistics(self.imaginary_parts)

        self.display_statistics(ang_stats, 'ang')
        print("\n")
        self.display_statistics(real_stats, 'real_parts')
        print("\n")
        self.display_statistics(imag_stats, 'imaginary_parts')

        return {
            'ang': ang_stats,
            'real_parts': real_stats,
            'imaginary_parts': imag_stats
        }

    def save_statistics_to_csv(self, stats_dict, output_csv_filepath):
        """
        Guardamos las estadísticas calculadas en un archivo CSV.
        """
        rows = []
        for key, stats in stats_dict.items():
            for stat_name, value in stats.items():
                rows.append({
                    'Statistic': stat_name,
                    'Value': value,
                    'Data Type': key
                })
        
        stats_df = pd.DataFrame(rows)
        stats_df.to_csv(output_csv_filepath, index=False)
        print(f"Statistics successfully saved to {output_csv_filepath}")

if __name__ == "__main__":
    # Obtener la ruta absoluta del directorio actual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_filepath = os.path.join(current_dir, '../data/music_data_1_angles.csv')
    output_filepath = os.path.join(current_dir, '../data/processed_data.h5')
    stats_csv_filepath = os.path.join(current_dir, '../results/statistics.csv')

    # Verificar si la ruta de salida existe, sino crearla
    output_dir = os.path.dirname(output_filepath)
    results_dir = os.path.dirname(stats_csv_filepath)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directory {output_dir} created.")
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f"Directory {results_dir} created.")

    # Verificar si el archivo de entrada existe
    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file {input_filepath} does not exist.")

    handler = DataHandler(input_filepath)
    handler.parse_matrices('Rx')  # Utiliza la columna 'Rx' que contiene las matrices complejas
    handler.save_to_hdf5(output_filepath)

    # Procesar y calcular estadísticas desde el archivo HDF5
    hdf5_handler = HDF5DataHandler(output_filepath)
    hdf5_handler.load_data()

    stats_calculator = StatisticsCalculator(hdf5_handler.ang, hdf5_handler.real_parts, hdf5_handler.imaginary_parts)
    all_stats = stats_calculator.calculate_and_display_all()
    stats_calculator.save_statistics_to_csv(all_stats, stats_csv_filepath)
