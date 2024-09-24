from fastapi import FastAPI
from typing import Dict
import joblib
import numpy as np

# Inicializar la aplicación FastAPI
app = FastAPI()

# Cargar el modelo de machine learning previamente entrenado
# En app/main.py
model = joblib.load("app/model/population_model.pkl")  # Cambia la ruta aquí


# Datos de población de los oblasts originales
oblasts_population = {
    "Donets'k": 4387702,
    "Dnipropetrovs'k": 3258705,
    'Kiev City': 2900920,
    'Kharkiv': 2720342,
    "L'viv": 2535476,
    'Odessa': 2387282,
    "Luhans'k": 2263676,
    'Crimea': 1963770,
    'Zaporizhzhya': 1755663,
    'Kiev': 1731673,
    'Vinnytsya': 1604270,
    'Poltava': 1440684,
    "Ivano-Frankivs'k": 1382721,
    "Khmel'nyts'kyy": 1296103,
    'Transcarpathia': 1259497,
    'Zhytomyr': 1249225,
    'Cherkasy': 1246166,
    'Rivne': 1162049,
    'Mykolayiv': 1159634,
    'Sumy': 1115051,
    "Ternopil'": 1066523,
    'Kherson': 1063803,
    'Chernihiv': 1047023,
    'Volyn': 1042855,
    'Kirovohrad': 974724,
    'Chernivtsi': 910001,
    'Sevastopol': 509992,
}

# Ruta principal que retorna el diccionario con los datos de población originales
@app.get("/oblasts_population")
def get_oblasts_population() -> Dict[str, int]:
    return oblasts_population

# Ruta para obtener la población predicha por el modelo de machine learning
@app.get("/predicted_population")
def get_predicted_population() -> Dict[str, float]:
    # Crear una lista con las características de cada oblast (en el mismo orden)
    input_data = np.array([
        [26517, 165], [31923, 102], [839, 3457], [31415, 86], [21833, 116], [33310, 72],
        [26684, 85], [27000, 73], [27183, 65], [28131, 61], [26513, 60], [28748, 50],
        [13928, 100], [20629, 90], [12777, 92], [29832, 82], [20900, 60], [20047, 59],
        [24598, 47], [23834, 46], [13852, 78], [28461, 41], [31900, 33], [20143, 52],
        [23923, 40], [13090, 70], [1079, 480]
    ])

    # Predecir la población usando el modelo
    predicted_values = model.predict(input_data).tolist()  # Convertimos la salida a lista
    
    # Formatear las predicciones en el mismo formato que oblasts_population
    predicted_population = {oblast: predicted_values[i] for i, oblast in enumerate(oblasts_population)}
    
    return predicted_population
