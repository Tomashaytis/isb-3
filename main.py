import os
import argparse
import json
import logging

from key_generation import generate_symmetric_key, generate_asymmetric_keys, save_symmetric_key, save_asymmetric_keys, \
    load_symmetric_key, load_private_key, load_public_key
from encrypt_text import asymmetric_encrypt, symmetric_encrypt
from decrypt_text import asymmetric_decrypt
from for_text import write_text, read_text

SETTINGS_FILE = os.path.join('files', 'settings.json')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=int, help='Запускает режим генерации ключей (Введите длину '
                                                              'симметричного ключа (4 - 56 байт))')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
    args = parser.parse_args()
    with open(SETTINGS_FILE) as json_file:
        settings = json.load(json_file)
    if args.generation is not None:
        length = args.generation
        if 4 <= length <= 56:
            symmetric_key = generate_symmetric_key(length)
            private_key, public_key = generate_asymmetric_keys()
            save_asymmetric_keys(private_key, public_key, settings['secret_key'], settings['public_key'])
            cipher_symmetric_key = asymmetric_encrypt(public_key, symmetric_key)
            save_symmetric_key(cipher_symmetric_key, settings['symmetric_key'])
        else:
            logging.warning(' symmetric key must be between 4 and 56 bytes long')
    elif args.encryption is not None:
        cipher_key = load_symmetric_key(settings['symmetric_key'])
        private_key = load_private_key(settings['secret_key'])
        symmetric_key = asymmetric_decrypt(private_key, cipher_key)
        text = read_text(settings['initial_file'])
        cipher_text = symmetric_encrypt(symmetric_key, text)
        write_text(cipher_text, settings['encrypted_file'])
    else:
        pass
