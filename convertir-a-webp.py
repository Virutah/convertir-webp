import os
from PIL import Image

# Rutas
carpeta_origen = r"D:/"
carpeta_destino = r"D:/"

# Extensiones comunes de imágenes
extensiones = ('.png', '.jpg', '.jpeg')

# Convertir las imágenes
for archivo in os.listdir(carpeta_origen):
    if archivo.lower().endswith(extensiones):
        ruta_original = os.path.join(carpeta_origen, archivo)
        nombre_sin_ext, _ = os.path.splitext(archivo)
        ruta_destino = os.path.join(carpeta_destino, nombre_sin_ext + ".webp")

        try:
            with Image.open(ruta_original) as img: # No errores
                img.save(ruta_destino, "WEBP", lossless=True)  # Mantiene transparencia
            print(f"CORRECTO Cambio correcto {archivo} convertido a {ruta_destino}") # Olee funciona
        except Exception as e:
            print(f"ERROR Error con {archivo}: {e}") # Vaya, no funciona