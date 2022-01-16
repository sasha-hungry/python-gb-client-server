"""Программа-сервер"""

import socket
import sys
import json
import logging
import log.config_server_log
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message, get_address_port

server_logger = logging.getLogger('server')

def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    server_logger.debug('разбор сообщения от клиента')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        server_logger.debug('сформирован ответ 200:OK')
        return {RESPONSE: 200}
    server_logger.debug('сформирован ответ об ошибке')
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    '''
    Загрузка параметров командной строки, если нет параметров,
    то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.0.100
    :return:
    '''
    address_port = get_address_port()
    listen_address = address_port[0]
    listen_port = address_port[1]
    server_logger.info(f'параметры подключения ip address сервера {listen_address}, tcp порт сервера {listen_port}')

    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_cient = get_message(client)
            server_logger.debug(f'получено сообщение от клиента {message_from_cient}')
            print(message_from_cient)
            # {'action': 'presence', 'time': 1573760672.167031,
            #'user': {'account_name': 'Guest'}}
            response = process_client_message(message_from_cient)
            send_message(client, response)
            server_logger.debug(f'отправлен ответ клиенту {response}')
            client.close()
        except (ValueError, json.JSONDecodeError):
            server_logger.error('некоректное сообщение от клиента')
            # print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
