"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

word_class = b"class"
word_function = b"function"
word_method = b"method"

list_of_word = [word_class, word_function, word_method]

for i in list_of_word:
	print(f"содержимое: {i}, тип: {type(i)}, длина: {len(i)}")
