import os
import glob

def rename_images(folder_path, prefix):
    """
    Renombra todas las imágenes en 'folder_path' con el prefijo dado ('prefix')
    y un índice incremental. Mantiene la extensión original del archivo.
    Ejemplo de resultado: prefix_1.jpg, prefix_2.png, ...
    """
    # Obtener la lista de archivos
    image_files = sorted(glob.glob(os.path.join(folder_path, "*")))

    # Contador para numerar los archivos
    i = 1

    for file_path in image_files:
        # Extraer la extensión
        extension = os.path.splitext(file_path)[1].lower()
        # Verificar si es un archivo de imagen
        if extension in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
            # Construir la nueva ruta
            new_name = f"{prefix}_{i}{extension}"
            new_path = os.path.join(folder_path, new_name)
            
            # Renombrar
            os.rename(file_path, new_path)
            print(f"Renombrado: {file_path} -> {new_path}")
            i += 1

# Rutas locales a tus carpetas en el repositorio clonado:
folder_clocks = r"C:\\Users\\Diego\\Documents\\Deep_learning\\Proyecto 1 - DAE + VAE\\(2)_Data\\motorcycles-and-clocks\\clocks" 
folder_motorcycles = r"C:\\Users\\Diego\\Documents\\Deep_learning\\Proyecto 1 - DAE + VAE\\(2)_Data\\motorcycles-and-clocks\\motorcycles"

# Llamar a la función para cada carpeta
rename_images(folder_clocks, "clock")
rename_images(folder_motorcycles, "motorcycle")
