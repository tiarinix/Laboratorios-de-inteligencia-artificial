import ee

# Inicializar la conexión con Earth Engine
try:
    ee.Initialize()
    print("Earth Engine Initialized Successfully!")
except Exception as e:
    print(f"Error initializing Earth Engine: {e}")
