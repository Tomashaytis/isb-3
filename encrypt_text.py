import os
import logging

from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logger = logging.getLogger()
logger.setLevel('INFO')


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    cipher_text = public_key.encrypt(text,
                                     asymmetric.padding.OAEP(mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                                                             algorithm=hashes.SHA256(), label=None))
    logging.info(' Asymmetric encrypt was successful')
    return cipher_text


def symmetric_encrypt(key: bytes, text: bytes) -> bytes:
    padder = padding.ANSIX923(64).padder()
    padded_text = padder.update(text) + padder.finalize()
    iv = os.urandom(8)
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_text) + encryptor.finalize()
    logging.info(' Symmetric encrypt was successful')
    return iv + cipher_text
