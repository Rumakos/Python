# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

# fname = input('Файл: ')
# f = open(fname,'w')
# while True:
#     s = input()
#     if s == '': break
#     f.write(s+'\n')
# f.close()

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# f = open('text.txt')
# line = 0
# for i in f:
#     line += 1
#
#     flag = 0
#     word = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#             flag = 0
#
#     print(i, len(i), 'симв.', word, 'сл.')
#
# print(line, 'стр.')
# f.close()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# staff = []
# employee = {}
#
# try:
#     with open(r'files/task3.txt') as task3:
#         for string in task3.readlines():
#             lst = list(string.replace("\n", "").split(" "))
#             if len(lst) == 2:
#                 employee = {
#                     "name": lst[0],
#                     "salaries": float(lst[1])
#                 }
#             staff.append(employee)
#
#     # print(staff)
#
# except IOError:
#     print("Произошла ошибка чтения!")
#
# print('Фамилии сотрудников с окладом менее 20 тыс.:')
# sum_salaries = 0
# for empl in staff:
#     if empl['salaries'] < 20000.00:
#         print(empl['name'])
#     sum_salaries = sum_salaries + empl['salaries']
#
# print(f'Средний оклад сотрудника = {sum_salaries / len(staff)}')


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# f = open('dataRu.txt', 'w')
# x = []
# z = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
# for i in open('test.txt'):
#     i = i.replace(i[0:i.find(' ')], z[i[0:i.find(' ')]])
#     f.write(i)
#     x.append(i[:-1])
#
# f.close()

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# import random
#
# random_list = []
#
# i = 0
# n = random.randint(1, 20)
# sum_el = 0
#
# while i < n:
#     random_list.append(random.randint(1, 1000))
#     i += 1
#
# try:
#     with open(r'files/task5.txt', "w") as task5:
#         for el in random_list:
#             print(el, end=' ', file=task5)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
#
# try:
#     with open(r'files/task5.txt') as task5:
#         for string in task5.readlines():
#             for el in string.rstrip().split(" "):
#                 sum_el += int(el)
#     print(sum_el)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
# def get_number_from_str(s):
#
#     l = len(s)
#     number_list = []
#     i = 0
#     while i < l:
#         s_int = ''
#         a = s[i]
#         while '0' <= a <= '9':
#             s_int += a
#             i += 1
#             if i < l:
#                 a = s[i]
#             else:
#                 break
#         i += 1
#         if s_int != '':
#             number_list.append(int(s_int))
#     return number_list
#
#
# subjects = {}
# syllabus = []
#
# try:
#     with open(r'files/task6.txt') as task6:
#         for string in task6.readlines():
#             S = string.replace("\n", "").partition(": ")
#             subjects = {
#                 "subject": S[0],
#                 "hours": sum(get_number_from_str(S[2]))
#             }
#             syllabus.append(subjects)
#
#         print(syllabus)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")


# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с
# фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
# словарь (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.
# import json
#
# company = {}
# avg_profit = {}
# business = []
#
# try:
#
#     with open(r'files/task7.txt') as task7:
#
#         for string in task7.readlines():
#             lst = list(string.replace("\n", "").split(" "))
#             i = 0
#             if len(lst) == 4:
#                 profit = round((float(lst[2]) - float(lst[3])), 2)
#                 company[lst[0]] = profit
#         business.append(company)
#
#         i = 0
#         S = 0
#         for x in company.values():
#             if x > 0:
#                 S += x
#                 i += 1
#         avg_profit = {'average_profit': round(S / i, 2)}
#         business.append(avg_profit)
#
#     print(business)
# except IOError:
#     print("Произошла ошибка чтения!")
#
# with open(r'files/task7_1.txt', 'w') as task7_1:
#     json.dump(business, task7_1)
