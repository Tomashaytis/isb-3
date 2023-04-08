from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


def asymmetric_decrypt(private_key, cipher_text: bytes) -> bytes:
    text = private_key.decrypt(cipher_text,
                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                            label=None))
    return text
