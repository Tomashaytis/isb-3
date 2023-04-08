import logging

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger()
logger.setLevel('INFO')


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    cipher_text = public_key.encrypt(text,
                                     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                  algorithm=hashes.SHA256(), label=None))
    return cipher_text


def padding_text(block_length: int, text: bytes):
    padder = padding.ANSIX923(block_length).padder()
    padded_text = padder.update(text) + padder.finalize()
    return padded_text


def read_text(file_name: str) -> bytes:
    try:
        with open(file_name, mode='rb') as text_file:
            text = text_file.read()
        logging.info(f' text was successfully read from file {file_name}')
    except OSError as err:
        logging.warning(f' text was not read from file {file_name}\n{err}')
    return text


def write_text(text: bytes, file_name: str) -> bytes:
    try:
        with open(file_name, mode='wb') as text_file:
            text_file.write(text)
        logging.info(f' text was successfully written to file {file_name}')
    except OSError as err:
        logging.warning(f' text was not written to file {file_name}\n{err}')
    return text

