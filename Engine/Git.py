import os
import logging as log
import subprocess

from time import strftime
from Engine.Tools import get_checksum, check_file, copy_file


def git_init(folder):
    if not os.path.exists(folder):
        log.info("Creado directorio para el repositorio")
        os.makedirs(folder)

    # Verificar si el repositorio Git ya está inicializado
    if not os.path.exists(os.path.join(folder, ".git")):
        subprocess.run(["git", "init"], check=True)
        log.debug(f"Repositorio Git inicializado")


def git_add(file):
    log.debug(f"Agregando al área de preparación")
    subprocess.run(["git", "add", file], check=True)


def git_commit(commit):
    subprocess.run(["git", "commit", "-m", commit], check=True)


def new_git(folder, files, commit):
    log.debug("No se ha inicializado el repositorio Git")
    git_init(folder)

    checksums = {}
    for file in files:  # Generar checksum de archivos
        log.info(f"Procesando archivo: {file}")

        # Generar checksum de archivos
        checksums[file] = get_checksum(file)
        log.debug(f"Generando checksum: {checksums[file]}")

        # Copiar archivos al repositorio Git
        git_path = os.path.join(folder, os.path.basename(file))
        log.info(f"Copiar archivo al repositorio")
        copy_file(file, git_path)

        # Agregar archivos al área de preparación
        git_add(git_path)

    # Realizar commit de los cambios
    log.info("Finalizando tareas")
    git_commit(commit)

    return checksums


def modify_git(folder, checksums, commit):
    log.debug("Repositorio Git ya inicializado")
    files = list(checksums.keys())
    modify = False
    for file in files:
        log.info(f"Verificando archivo: {file}")
        if check_file(file, checksums[file]):
            log.info(f"Archivo modificado")
            modify = True

            log.debug(f"Actualizar archivo al repositorio")
            git_path = os.path.join(folder, os.path.basename(file))
            copy_file(file, git_path)

            # Agregar archivos al área de preparación
            log.debug(f"Agregando archivo al área de preparación")
            git_add(git_path)

            checksums[file] = get_checksum(file)
            log.debug(f"Checksum actualizando: {checksums[file]}")

        else:
            log.info(f"Sin cambios")

    if modify:
        log.info("Realizando cambios en el repositorio")
        git_commit(commit)

    return checksums


def run(task):
    folder = os.path.expanduser(task["folder"])
    files = [os.path.expanduser(file) for file in task["files"]]
    commit = strftime("%Y-%m-%d %H:%M:%S")
    checksums = task["checksums"]

    os.chdir(folder)
    try:
        if task["checksums"] is None:
            checksums = new_git(folder, files, commit)

        else:
            checksums = modify_git(folder, checksums, commit)

        return checksums

    except subprocess.CalledProcessError as e:
        log.error(f"Error durante el proceso: {e}")
        return None
