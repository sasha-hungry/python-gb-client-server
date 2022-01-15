"""Unit-тесты сервера"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from server import process_client_message

class TestServer(unittest.TestCase):
    '''
    В сервере только 1 функция для тестирования
    '''
    err_dict = {RESPONSE: 400, ERROR: 'Bad Request'}
    ok_dict = {RESPONSE: 200}

    def test_no_action(self):
        """Ошибка если нет действия"""
        test = process_client_message({TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, self.err_dict)

    def test_wrong_action(self):
        """Ошибка если неизвестное действие"""
        test = process_client_message({ACTION: 'Some other action', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, self.err_dict)

    def test_no_time(self):
        """Ошибка, если  запрос не содержит штампа времени"""
        test = process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, self.err_dict)

    def test_no_user(self):
        """Ошибка - нет пользователя"""
        test = process_client_message({ACTION: PRESENCE, TIME: '1.1'})
        self.assertEqual(test, self.err_dict)

    def test_unknown_user(self):
        """Ошибка - не Guest"""
        test = process_client_message({ACTION: PRESENCE, TIME: 'Some_Time_Stamp', USER: {ACCOUNT_NAME: 'Some_User_Name'}})
        self.assertEqual(test, self.err_dict)
# нет проверки формата времени, проходят и числа и строки


    def test_ok_check(self):
        """Корректный запрос"""
        test = process_client_message({ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
        self.assertEqual(test, self.ok_dict)


if __name__ == '__main__':
    unittest.main()
