"""Утилиты"""

import json
import sys
sys.path.append('../')
import logging
import log.config_client_log
from decos import log
from common.variables import MAX_PACKAGE_LENGTH, ENCODING, DEFAULT_PORT

logger = logging.getLogger('client')

@log
def get_address_port():
    '''
    Считывает параметры командной строки, если нет параметров 
    использует данные по умолчанию (localhost:7777).
    Пример команды запуска:
    server.py -a 192.168.0.100 -p 6666
    '''

    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = DEFAULT_PORT
        if port < 1024 or port > 65535:
            logger.error(f'не верный номер порта')
            raise ValueError
            
    except IndexError:
        logger.info('не указан обязательный параметр после -p')
        #print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        logger.error('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        #print('В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)


    try:
        if '-a' in sys.argv:
            address = sys.argv[sys.argv.index('-a') + 1]
        else:
            address = ''

    except IndexError:
        # print(
        #   'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        logger.error('не указан обязательный параметр после -a')
        sys.exit(1)
    
    address_port = [address, port]
    return address_port


def get_message(client):
    '''
    Утилита приёма и декодирования сообщения
    принимает байты выдаёт словарь, если приняточто-то другое отдаёт ошибку значения
    :param client:
    :return:
    '''

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    '''
    Утилита кодирования и отправки сообщения
    принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    '''

    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
