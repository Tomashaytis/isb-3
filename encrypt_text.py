import os
import logging

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logger = logging.getLogger()
logger.setLevel('INFO')


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    cipher_text = public_key.encrypt(text,
                                     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                  algorithm=hashes.SHA256(), label=None))
    logging.info(' asymmetric encrypt was successful')
    return cipher_text


def padding_text(text: bytes):
    padder = padding.ANSIX923(64).padder()
    padded_text = padder.update(text) + padder.finalize()
    return padded_text


def symmetric_encrypt(key: bytes, text: bytes) -> bytes:
    padded_text = padding_text(text)
    iv = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_text) + encryptor.finalize()
    logging.info(' symmetric encrypt was successful')
    return cipher_text
