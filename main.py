import os
import argparse
import json
from key_generation import generate_symmetric_key, generate_asymmetric_keys, save_asymmetric_keys, save_symmetric_key
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
        symmetric_key = generate_symmetric_key(args.generation)
        private_key, public_key = generate_asymmetric_keys()
        save_asymmetric_keys(private_key, public_key, settings['secret_key'], settings['public_key'])
    elif args.encryption is not None:
        pass
    else:
        pass
