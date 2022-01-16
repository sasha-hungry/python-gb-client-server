"""Программа-клиент"""

import sys
import json
import socket
import time
import logging
import log.config_client_log
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.utils import get_message, send_message, get_address_port


client_logger = logging.getLogger('client')

def create_presence(account_name='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    client_logger.debug(f'сгенерирован запрос PRESENCE для username: {account_name}')
    return out


def process_ans(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            client_logger.debug(f'получен ответ {message[RESPONSE]}')
            return '200 : OK'
        client_logger.debug(f'получен ответ 400 : {message[ERROR]}')
        return f'400 : {message[ERROR]}'
    client_logger.debug(f'ответ не получен, генерация ValueError')
    raise ValueError


def main():
    '''Загружаем параметы коммандной строки'''
    # client.py -a 192.168.0.100 -p 6666 

    # Инициализация сокета и обмен
    address_port = get_address_port()
    server_address = address_port[0]
    server_port = address_port[1]
    client_logger.info(f'параметры подключения ip address сервера {server_address}, tcp порт сервера {server_port}')

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    client_logger.debug(f'отправлено сообщение {message_to_server} в сторону сервера')
    try:
        answer = process_ans(get_message(transport))
        client_logger.debug(f'получен и декодирован ответ от сервера')
        print(answer)
    except (ValueError, json.JSONDecodeError):
        client_logger.error(f'не удалось декодировать сообщение с сервера')
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
