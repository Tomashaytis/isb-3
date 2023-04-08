import os


def generate_symmetric_key(length: int) -> bytes:
    return os.urandom(length)
