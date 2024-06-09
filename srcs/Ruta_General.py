import pandas as pd
import os

def leer_csv():
    # Obtén la ruta absoluta del directorio actual donde se ejecuta el script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construye la ruta al archivo CSV (asegúrate de incluir la extensión del archivo)
    csv_path = os.path.join(base_dir, "..", "data", "datos_MUSIC_3.csv")  # Asumiendo que el archivo es .csv
    print("Intentando abrir el archivo en:", csv_path)  # Esto imprimirá la ruta completa
    # Intenta leer el archivo CSV
    try:
        df = pd.read_csv(csv_path)
        #rint(df.head())  # Muestra las primeras líneas del DataFrame
    except Exception as e:
        print("Error al leer el archivo:", e)

if __name__ == "__main__":
    data=leer_csv()
    print(data.head())
