"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
'''
wrd_dev = "разработка"
wrd_adm = "администрирование"
wrd_prot = "protocol"
wrd_stnd = "standard"
'''

list_of_words = ["разработка", "администрирование", "protocol", "standard"]
list_of_words_byte = list()

# преобразование из строкового представления в байтовое

for i in range(len(list_of_words)):
	list_of_words_byte.append(list_of_words[i].encode("utf-8"))
	print(list_of_words_byte[i], type(list_of_words_byte[i]))


# преобразование из байтового представления в строковое
print()
print("преобразовние из байтового представления в строковое:")
print()

for i in range(len(list_of_words_byte)):
	print(list_of_words_byte[i].decode("utf-8"), type(list_of_words_byte[i].decode("utf-8")))
