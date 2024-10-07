import os
import sys
import sqlite3
from PIL import Image


# Funcion para buscar iconos en base al numbre del archivo
def icons(app):
    default_icons = ["~/.local/share/icons/hicolor",
                     "/usr/share/icons/hicolor",
                     "/usr/share/pixmaps"]

    for icon in default_icons:
        for root, dirs, files in os.walk(icon):
            for file in files:
                if app in file:
                    image_path = os.path.join(root, file)
                    with Image.open(image_path) as img:
                        width, height = img.size
                        if width >= 48 and height >= 48:

                           return os.path.join(root, file)


def list_apps(files, level):
    work_folder = os.path.abspath(os.path.dirname(sys.argv[0]))
    config_folder = os.path.join(work_folder, 'config')

    conn = sqlite3.connect(f"{config_folder}/dotfiles.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT applications.name, config_paths.path, config_paths.level 
        FROM applications 
        JOIN config_paths 
        ON applications.id = config_paths.application_id
    """)
    results = cursor.fetchall()

    applications = {}

    for file in files:
        for result in results:
            if file in result[1] and result[2] >= level:
                if result[0] in applications:
                    applications[result[0]].append({"path": file, "level": result[2]})
                    break

                else:
                    applications[result[0]] = [{"path": file, "level": result[2]}]
                    break

    conn.close()

    return applications


# Función para escanear el directorio del usuario
def dotfiles():
    user_files = []
    user_folders = []
    config_files = []
    config_folders = []

    home_dir = os.path.expanduser('~')
    config_dir = os.path.join(home_dir, '.config')

    # Escanear el directorio del usuario
    for item in os.listdir(home_dir):
        if item.startswith('.'):
            value = os.path.join(home_dir, item)

            if os.path.isfile(value):
                user_files.append(value.replace(home_dir, '~'))

            elif os.path.isdir(value):
                user_folders.append(value.replace(home_dir, '~'))

    # Listar archivos y carpetas dentro de .config
    if os.path.exists(config_dir):
        for item in os.listdir(config_dir):
            item_path = os.path.join(config_dir, item)

            if os.path.isfile(item_path):
                config_files.append(item_path.replace(home_dir, '~'))

            elif os.path.isdir(item_path):
                config_folders.append(item_path.replace(home_dir, '~'))

    return user_files, user_folders, config_files, config_folders