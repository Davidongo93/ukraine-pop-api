from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from app.data.dataSet import df 
# Separar las características (X) y la variable objetivo (y)
X = df[['area_km2', 'population_density']]
y = df['population']

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el modelo
model = RandomForestRegressor()

# Entrenar el modelo
model.fit(X_train, y_train)

# Evaluar el modelo (opcional)
score = model.score(X_test, y_test)
print(f"Score del modelo: {score}")

# Guardar el modelo en un archivo para usarlo en FastAPI
joblib.dump(model, "app/model/population_model.pkl")
