
import sys
import logging
import log.config_server_log
import log.config_client_log
import traceback
import inspect

# метод определения модуля, источника запуска  - списал.
# Метод find () возвращает индекс первого вхождения искомой подстроки,
# если он найден в данной строке.
# Если его не найдено, - возвращает -1.
# os.path.split(sys.argv[0])[1]
if sys.argv[0].find('client') == -1:
    logger = logging.getLogger('server')
else:
    logger = logging.getLogger('client')

def log(func_to_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        """Обертка"""
        ret = func_to_log(*args, **kwargs)
        logger.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}. Вызов из'
                     f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}')
        return ret
    return log_saver

