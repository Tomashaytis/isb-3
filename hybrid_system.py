import argparse
import logging

from symmetric_encryption import generate_symmetric_key, symmetric_encrypt, symmetric_decrypt
from asymmetric_encryption import generate_asymmetric_keys, asymmetric_encrypt, asymmetric_decrypt
from system_functions import load_settings, byte_write_text, byte_read_text, save_symmetric_key, save_asymmetric_keys, \
    load_symmetric_key, load_private_key

SETTINGS_FILE = 'files/settings.json'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str, help='Позволяет использовать собственный json-файл с указанием '
                                                             'необходимых путей для работы системы '
                                                             '(Введите путь к файлу)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', type=int, help='Запускает режим генерации ключей (Введите длину '
                                                              'симметричного ключа (4 - 56 байт))')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
    args = parser.parse_args()
    settings = load_settings(args.settings) if args.settings else load_settings(SETTINGS_FILE)
    if settings:
        if args.generation:
            length = args.generation
            if 4 <= length <= 56:
                symmetric_key = generate_symmetric_key(length)
                private_key, public_key = generate_asymmetric_keys()
                save_asymmetric_keys(private_key, public_key, settings['secret_key'], settings['public_key'])
                cipher_symmetric_key = asymmetric_encrypt(public_key, symmetric_key)
                save_symmetric_key(cipher_symmetric_key, settings['symmetric_key'])
            else:
                logging.warning(' Symmetric key must be between 4 and 56 bytes long')
        elif args.encryption:
            private_key = load_private_key(settings['secret_key'])
            cipher_key = load_symmetric_key(settings['symmetric_key'])
            symmetric_key = asymmetric_decrypt(private_key, cipher_key)
            text = byte_read_text(settings['initial_file'])
            cipher_text = symmetric_encrypt(symmetric_key, text)
            byte_write_text(cipher_text, settings['encrypted_file'])
        else:
            private_key = load_private_key(settings['secret_key'])
            cipher_key = load_symmetric_key(settings['symmetric_key'])
            symmetric_key = asymmetric_decrypt(private_key, cipher_key)
            cipher_text = byte_read_text(settings['encrypted_file'])
            text = symmetric_decrypt(symmetric_key, cipher_text)
            byte_write_text(text, settings['decrypted_file'])
