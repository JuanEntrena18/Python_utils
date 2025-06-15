import os

# Configuración
directorio = "./"  # Cambia esto si necesitas otro directorio
nombre_base = "razer_kishiV3"

# Obtener lista de archivos .jpg
archivos = [f for f in os.listdir(directorio) if f.lower().endswith(".jpg")]

# Ordenar archivos para que la numeración sea consistente
archivos.sort()

# Renombrar archivos
for i, archivo in enumerate(archivos, start=1):
    extension = os.path.splitext(archivo)[1]  # Mantener la extensión original
    nuevo_nombre = f"{nombre_base}_{i}{extension}"
    os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_nombre))

print("Renombrado completado.")
