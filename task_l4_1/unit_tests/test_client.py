"""Unit-тесты клиента"""

import sys
import os
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, \
    ACTION, PRESENCE,  RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT
from client import create_presence, process_ans

class TestClass(unittest.TestCase):
    '''
    Класс с тестами
    '''

    def test_def_presense(self):
        """Тест коректного запроса"""
        test = create_presence()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
                          # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})
        
    def test_presense_username(self):
        """Тест формирования регистрации с новым username"""
        test = create_presence('Anonymous')
        test[TIME] = 2.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 2.1, USER: {ACCOUNT_NAME: 'Anonymous'}})
    
    def test_presense_username_as_number(self):
        """Тест формирования регистрации с явно заданным username как число"""
        test = create_presence(666)
        test[TIME] = 3.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 3.1, USER: {ACCOUNT_NAME: 666}})

    def test_200_ans(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """Тест корректного разбора 400"""
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()

#
