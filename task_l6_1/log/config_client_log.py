
import sys
import os
import logging
sys.path.append('../')
from common.variables import LOGGING_LEVEL


# подготовка файла для логирования(честно списано)
path = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(path, 'client.log')


# определить формат сообщений
syslog_format = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# вывод в терминал c уровнем error
stream_log = logging.StreamHandler(sys.stderr)
stream_log.setLevel(logging.ERROR)
stream_log.setFormatter(syslog_format)

# вывод в файл все подряд
# file_log = logging.FileHandler('client.log', encoding='utf8')
file_log = logging.FileHandler(log_file, encoding='utf8')
file_log.setFormatter(syslog_format)

# создаем регистр clinet
client_logger = logging.getLogger('client')
client_logger.addHandler(stream_log)
client_logger.addHandler(file_log)
client_logger.setLevel(LOGGING_LEVEL)

# локальный запуск
if __name__ == '__main__':
    client_logger.critical('Критическая ошибка')
    client_logger.error('Ошибка')
    client_logger.debug('Отладочная информация')
    client_logger.info('Информационное сообщение')
