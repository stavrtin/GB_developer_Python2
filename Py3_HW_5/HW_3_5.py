# '''Задание №2
# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку. '''
# # def str_do_dict(text):
# #     # return {i: ord(i) from i ni text}
# #     return {i: ord(i) for i in text}
# #
# # text = 'Задание'
# # ssstr = (str_do_dict(text))
# # print(ssstr)
#
# '''Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.'''
#
# # def str_do_dict2(text):
# #     # return {i: ord(i) from i ni text}
# #     res = iter({i: ord(i) for i in text}.items())
# #     print([i for i in next(res)])
# #     # print(next(res))
# #     # return res
# #
# # str_do_dict2('asdasdasasd')
# #
#
# '''Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.'''
# #
# # def gen():
# #     # print(i for i in range(0,101) if (i // 10 + i % 10 != 8) and i % 2 == 0)
# #     res = (i for i in range(0,101) if (i // 10 + i % 10 != 8) and i % 2 == 0)
# #     return res
#
# # for i in gen():
# #     print(i)
# #
# # print([i for i in gen()])
#
# '''Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.'''
#
# # for i in range(1,101):
# #     if (i % 3 == 0) and (i % 5 == 0):
# #         print('«FizzBuzz»')
# #     elif i % 5 == 0:
# #         print('«Buzz»')
# #     elif (i % 3 == 0):
# #         print('«Fizz»')
# #     else: print(i)
#
# # def gen_3_5():
# #     # res = ['«FizzBuzz»' if ((i % 3 == 0) and (i % 5 == 0)) else i for i in range(1,101)]
# #     res = ('«FizzBuzz»' if (i % 15 == 0) else '«Fizz»' if (i % 3 == 0) else '«Buzz»'if (i % 5 == 0) else i for i in range(1,101))
# #     return res
# #
# # print(gen_3_5())
# # for i in gen_3_5():
# #     print(i)
# '''Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.'''
#
# # def tab_multy():
# #     print(*(f'{i}x{j} = {i * j}' for i in range(2, 11) for j in range(2, 11)))  # for k in range(2,4)))
# #     # return res
#
# # tab_multy()
#
# '''Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».'''
#
# # def gen_netural(n):
# #     print(n)
# #     for i in range(2,n):
# #         nat_flag = 0
# #         for j in range(2,10):
# #             if (i > j ) and i % j == 0:
# #                 nat_flag = 1
# #         if nat_flag == 0:
# #             print(i)
# #     # res = (i for i in range(2,n + 1))
# #     # print(*res)
# #
# # gen_netural(120)
# #


# -------------------task 5/1--------------
'''
Урок 5. Интераторы и генераторы
1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''
print('\n-------------------task 5/1--------------')
file_abs = "C:/Users/stavr/Downloads/Семинар 5. Погружение в Python. Итераторы и генераторы.pdf"

def path_name(name):
    full_file_name = file_abs.split('/')[-1:][0]
    full_path = file_abs.split(full_file_name)[0]
    exten_file = full_file_name.split('.')[-1:][0]
    return (full_path, full_file_name, exten_file)

res_out = path_name(file_abs)
print(res_out)

# -------------------task 5/2--------------
'''2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь 
с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка 
умноженная на процент премии'''
print('\n-------------------task 5/2--------------')
list_1 = ['var1', 200, '12.25%']
list_2 = ['var2', 300, '13.25%']
list_3 = ['var3', 400, '14.25%']

def gen_premiya_one_str(name1, name2, name3):
    res_gen = ({i[0]: i[1] * float(i[2].split('%')[0])} for i in iter([name1, name2, name3]))
    yield res_gen

for i in gen_premiya_one_str(list_1, list_2, list_3):
    print(*i)


# -------------------task 5/3--------------
'''
3. Создайте функцию генератор чисел Фибоначчи (см. Википедию)'''
print('\n-------------------task 5/3--------------')


def fibon(n):
    ' первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел'
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fibon(10)))

# fibon(5)
