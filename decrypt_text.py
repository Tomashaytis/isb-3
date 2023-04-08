import logging

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives import hashes, padding

logger = logging.getLogger()
logger.setLevel('INFO')


def asymmetric_decrypt(private_key, cipher_text: bytes) -> bytes:
    text = private_key.decrypt(cipher_text,
                               asymmetric.padding.OAEP(mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                                                       algorithm=hashes.SHA256(),
                                                       label=None))
    logging.info(' Asymmetric decrypt was successful')
    return text


def symmetric_decrypt(key: bytes, cipher_text: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    text = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(64).unpadder()
    unpadded_text = unpadder.update(text) + unpadder.finalize()
    logging.info(' Symmetric decrypt was successful')
    return unpadded_text
