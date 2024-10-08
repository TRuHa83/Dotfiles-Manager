import os
import hashlib
import subprocess

from time import strftime


def checksum(archivo, algoritmo="sha256"):
    # Crear un objeto hash usando el algoritmo especificado
    hash_func = hashlib.new(algoritmo)

    with open(archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_func.update(bloque)

    # Retornar el checksum en formato hexadecimal
    return hash_func.hexdigest()


def git(task):
    folder = os.path.expanduser(task["folder"])
    files = [os.path.expanduser(file) for file in task["files"]]
    commit = strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(folder):
        os.makedirs(folder)
    os.chdir(folder)

    # Verificar si el repositorio Git ya está inicializado
    if not os.path.exists(os.path.join(folder, ".git")):
        subprocess.run(["git", "init"], check=True)
        print(f"Repositorio Git inicializado en {folder}")

    # Comprueba si exsiste la key checksums en el diccionario
    if "checksums" in task:
        checksums = task["checksums"]
        # Verificar si los archivos han cambiado
        for file in files:
            if checksum(file, "md5") != checksums[file]:
                print(f"El archivo {file} ha cambiado")
                break
        else:
            print("No hay cambios en los archivos")
            return checksums

    for file in files:
        file_name = os.path.basename(file)
        symlink_path = os.path.join(folder, file_name)

        # Crear el enlace simbólico solo si no existe
        if not os.path.exists(symlink_path):
            os.symlink(file, symlink_path)
            print(f"Enlace simbólico creado: {symlink_path} -> {file}")

        # Agregar el enlace simbólico al área de preparación
        subprocess.run(["git", "add", symlink_path], check=True)

    # Hacer un commit con un mensaje
    subprocess.run(["git", "commit", "-m", commit], check=True)

    print(f"Cambios confirmados en {folder}")

    # Generar checksum de archivos para poder determinar cuando cambian
    checksums = {}
    for file in files:
        checksums[file] = checksum(file, "md5")

    return checksums


def restore_git():
    pass


def backup():
    pass


def restore_backup():
    pass
