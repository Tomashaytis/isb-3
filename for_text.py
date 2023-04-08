import logging

logger = logging.getLogger()
logger.setLevel('INFO')


def read_text(file_name: str) -> bytes:
    try:
        with open(file_name, mode='rb') as text_file:
            text = text_file.read()
        logging.info(f' text was successfully read from file {file_name}')
    except OSError as err:
        logging.warning(f' text was not read from file {file_name}\n{err}')
    return text


def write_text(text: bytes, file_name: str) -> bytes:
    try:
        with open(file_name, mode='wb') as text_file:
            text_file.write(text)
        logging.info(f' text was successfully written to file {file_name}')
    except OSError as err:
        logging.warning(f' text was not written to file {file_name}\n{err}')
    return text
