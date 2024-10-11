import os
import logging as log
import hashlib
import subprocess
import time

from time import strftime


def get_checksum(archivo, algoritmo="sha256"):
    # Crear un objeto hash usando el algoritmo especificado
    hash_func = hashlib.new(algoritmo)

    with open(archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_func.update(bloque)

    # Retornar el checksum en formato hexadecimal
    return hash_func.hexdigest()


def check_checksum(checksums):
    for file in checksums.keys():
        if get_checksum(file, "md5") != checksums[file]:
            log.info(f"El archivo {file} ha cambiado")
            return False

    return True


def git(task):
    folder = os.path.expanduser(task["folder"])
    files = [os.path.expanduser(file) for file in task["files"]]
    commit = strftime("%Y-%m-%d %H:%M:%S")

    if task["checksums"] is not None:
        if check_checksum(task["checksums"]):
            log.info("No hay cambios en los archivos")
            return task["checksums"]

    else:
        if not os.path.exists(folder):
            os.makedirs(folder)
        os.chdir(folder)

        # Verificar si el repositorio Git ya está inicializado
        if not os.path.exists(os.path.join(folder, ".git")):
            subprocess.run(["git", "init"], check=True)
            log.info(f"Repositorio Git inicializado")

    for file in files:
        file_name = os.path.basename(file)
        symlink_path = os.path.join(folder, file_name)

        # Crear el enlace simbólico solo si no existe
        if not os.path.exists(symlink_path):
            os.symlink(file, symlink_path)
            log.info(f"Enlace simbólico creado: {symlink_path}")

        # Agregar el enlace simbólico al área de preparación
        subprocess.run(["git", "add", symlink_path], check=True)

    # Hacer un commit con un mensaje
    log.info(f"Commit de los cambios: {commit}")
    subprocess.run(["git", "commit", "-m", commit], check=True)

    log.info(f"Cambios confirmados")

    # Generar checksum de archivos para poder determinar cuando cambian
    checksums = {}
    for file in files:
        checksums[file] = get_checksum(file, "md5")

    return checksums


def restore_git():
    pass


def backup():
    pass


def restore_backup():
    pass


def run(task):
    if task["mode"] == "git":
        try:
            checksum = git(task)
            return checksum

        except subprocess.CalledProcessError as e:
            log.error(f"Error to process: {e}")
            return None

    elif task["mode"] == "backup":
        pass

