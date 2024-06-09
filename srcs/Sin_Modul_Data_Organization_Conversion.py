import ast
import os
import pandas as pd

def leer_csv():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "..", "data", "datos_MUSIC_3.csv")
    print("Intentando abrir el archivo en:", csv_path)
    try:
        data = pd.read_csv(csv_path)
        print(data.head())
        return data
    except Exception as e:
        print("Error al leer el archivo:", e)
        return None

def count_angles(angle_string):
    try:
        angle_list = ast.literal_eval(angle_string.replace("\n", ","))
        return len(angle_list)
    except:
        return 0

def main():
    data = leer_csv()
    if data is not None:
        data['angle_count'] = data['ang'].apply(count_angles)
        grouped_data = {n: data[data['angle_count'] == n] for n in range(1, 6)}

        for n in grouped_data:
            grouped_data[n].drop(columns=['angle_count'], inplace=True)

        # Define la carpeta 'data' en el mismo nivel que la carpeta 'srcs' para guardar los archivos
        data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
        
        # Guarda cada grupo en un archivo CSV en la carpeta 'data'
        for n in range(1, 6):
            filename = os.path.join(data_dir, f'music_data_{n}_angles.csv')
            grouped_data[n].to_csv(filename, index=False)
        print("Archivos guardados en:", data_dir)

if __name__ == "__main__":
    main()