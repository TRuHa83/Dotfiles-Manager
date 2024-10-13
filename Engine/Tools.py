import shutil
import hashlib


def get_checksum(archivo, algoritmo="md5"):
    hash_func = hashlib.new(algoritmo)

    with open(archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            hash_func.update(bloque)

    # Retornar el checksum en formato hexadecimal
    return hash_func.hexdigest()


def check_file(file, checksum):
    if get_checksum(file, "md5") != checksum:
        return True

    return False


def copy_file(source, destination):
    shutil.copy(source, destination)
