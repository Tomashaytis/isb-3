import logging

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import asymmetric
from cryptography.hazmat.primitives import hashes, padding

logger = logging.getLogger()
logger.setLevel('INFO')


def asymmetric_decrypt(private_key, cipher_text: bytes) -> bytes:
    """
    The function decrypts an asymmetrical ciphertext using private key.

    :param private_key: private key of asymmetric encryption algorithm.
    :param cipher_text: ciphertext.
    :return: decrypted text.
    """
    text = private_key.decrypt(cipher_text,
                               asymmetric.padding.OAEP(mgf=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
                                                       algorithm=hashes.SHA256(),
                                                       label=None))
    logging.info(' Asymmetric decryption was successful')
    return text


def symmetric_decrypt(key: bytes, cipher_text: bytes) -> bytes:
    """
    The function decrypts a symmetrical ciphertext using symmetric key.

    :param key: symmetric key of symmetric encryption algorithm.
    :param cipher_text: ciphertext.
    :return: decrypted test.
    """
    cipher_text, iv = cipher_text[8:], cipher_text[:8]
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    text = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(64).unpadder()
    unpadded_text = unpadder.update(text) + unpadder.finalize()
    logging.info(' Symmetric decryption was successful')
    return unpadded_text
