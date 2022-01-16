
import sys
import os
import logging
import logging.handlers
sys.path.append('../')
from common.variables import LOGGING_LEVEL

# определить формат сообщений
syslog_format = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# подготовка файла для логирования(честно списано)
path = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(path, 'server.log')


# вывод в терминал c уровнем error
stream_log = logging.StreamHandler(sys.stderr)
stream_log.setLevel(logging.ERROR)
stream_log.setFormatter(syslog_format)

# вывод в файл все подряд
file_log = logging.handlers.TimedRotatingFileHandler(log_file, encoding='utf8', interval=1, when='midnight')
file_log.setFormatter(syslog_format)

# создаем регистр server
server_logger = logging.getLogger('server')
server_logger.addHandler(stream_log)
server_logger.addHandler(file_log)
server_logger.setLevel(LOGGING_LEVEL)

# локальный запуск
if __name__ == '__main__':
    server_logger.critical('Критическая ошибка')
    server_logger.error('Ошибка')
    server_logger.debug('Отладочная информация')
    server_logger.info('Информационное сообщение')
