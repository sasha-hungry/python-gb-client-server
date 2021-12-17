"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

list_of_words = ["attribute", "класс", "функция", "type"]

for i in list_of_words:
	try:
		print(bytes(i, 'ascii'))
	except UnicodeEncodeError:
		print("\"", i,"\", невозможно записать в байтовом виде", sep="")