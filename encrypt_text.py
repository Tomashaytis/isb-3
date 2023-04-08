from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def asymmetric_encrypt(public_key, text: bytes) -> bytes:
    cipher_text = public_key.encrypt(text,
                                     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                  algorithm=hashes.SHA256(), label=None))
    return cipher_text
