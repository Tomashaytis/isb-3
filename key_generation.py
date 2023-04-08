import os
import logging
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key

logger = logging.getLogger()
logger.setLevel('INFO')


def generate_symmetric_key(length: int) -> bytes:
    key = os.urandom(length)
    logging.info(f' symmetric key generated')
    return key


def generate_asymmetric_keys() -> tuple:
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    logging.info(f' asymmetric keys generated')
    return private_key, public_key


def save_symmetric_key(key: bytes, file_name: str) -> None:
    try:
        with open(file_name, 'wb') as key_file:
            key_file.write(key)
        logging.info(f' symmetric key successfully saved to {file_name}')
    except OSError as err:
        logging.warning(f' symmetric key was not saved to file {file_name}\n{err}')


def save_asymmetric_keys(private_key, public_key, private_pem: str, public_pem: str) -> None:
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        logging.info(f' private key successfully saved to {private_pem}')
    except OSError as err:
        logging.warning(f' private key was not saved to file {private_pem}\n{err}')
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logging.info(f' public key successfully saved to {public_pem}')
    except OSError as err:
        logging.warning(f' public key was not saved to file {public_pem}\n{err}')


def load_symmetric_key(file_name: str) -> bytes:
    try:
        with open(file_name, mode='rb') as key_file:
            key = key_file.read()
        logging.info(f' symmetric key successfully loaded from {file_name}')
    except OSError as err:
        logging.warning(f' symmetric key was not loaded from file {file_name}\n{err}')
    return key


def load_private_key(private_pem: str):
    private_key = None
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        private_key = load_pem_private_key(private_bytes, password=None)
        logging.info(f' private key successfully loaded from {private_pem}')
    except OSError as err:
        logging.warning(f' private key was not loaded from file {private_pem}\n{err}')
    return private_key


def load_public_key(public_pem: str):
    public_key = None
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        public_key = load_pem_public_key(public_bytes)
        logging.info(f' public key successfully loaded from {public_pem}')
    except OSError as err:
        logging.warning(f' public key was not loaded from file {public_pem}\n{err}')
    return public_key

