# # 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# # Об окончании ввода данных свидетельствует пустая строка.
# my_list =[]
# print("Введите информацию для сохранения в файл:")
# while True:
#     my_string = input()
#     my_list.append(my_string)
#     if my_string == "":
#         break
# try:
#     with open("My_first_text.txt", "a+") as f_obj:
#         for el in my_list:
#             f_obj.write(str(el)+"\n")
# except IOError:
#     print("Произошла ошибка ввода-вывода!")

# 2.Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

# second_file = open("new 1.txt")
# content = second_file.readlines()
# second_file.close()
# string_count = 0
# words_in_string_count = []
# for el in content:
#     string_count +=1
#     el.strip()
#     new_string = el.split(" ")
#     words_count = 0
#     for new_el in new_string:
#         words_count += 1
#     words_in_string_count.append(words_count)
#
# print(f"Количество строк: {string_count}")
# print(f"Слов в строках {words_in_string_count}")

# 3.Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
#
# second_file = open("salary2.txt")
# content = second_file.readlines()
# second_file.close()
#
# surname = []
# salary = []
# string_count = 0
# for el in content:
#     el.strip()
#     new_string = el.split(" ")
#     surname.append(new_string[0])
#     salary.append(int(new_string[1]))
#
# average_salary = 0
# over_twenty = []
# for el in range(len(salary)):
#     average_salary += int(salary[el])
#     if salary[el] > 20000:
#         over_twenty.append(el)
#
# print(f"Средняя зарплата:{average_salary / len(salary)}")
# print("Фамилии сотрудников с зарплатой более 20000:")
# for el in range(len(over_twenty)):
#     print(surname[over_twenty[el]])




# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# second_file = open("ex4.txt")
# content = second_file.readlines()
# second_file.close()
# cont = []
# my_dict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
# for el in range(len(content)):
#     cont.append(str(content[el]).split(" "))
# for el in (cont):
#     el[1] = my_dict.get(el[1])
#     print(el)
#
# print(content)



#
# 5.Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# import random
# s = " "
# first_list = [ str(random.randint(0, 100)) for el in range(0, random.randint(0, 100), 1)]
# new_string = s.join(first_list)
#
# second_file = open("sum.txt", "w")
# second_file.writelines(new_string)
# second_file.close()
#
# second_file = open("sum.txt", "r")
# content = second_file.readlines()
# second_file.close()
#
# print(f"Содержимое файла {content}")
# for el in content:
#     content = str(el).split(" ")
#
# amount = 0
# for el in content:
#     amount += int(el)
#
#
# print(f"Сумма числе в файле {amount}")


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
# и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
#

# second_file = open("les.txt", "r")
# content = second_file.readlines()
# second_file.close()
# discipline = []
# hours = []
# print(f"Содержимое файла {content}")
#
# for el in content:
#     my_string = str(el)
#     pos = my_string.find(":")
#     discipline.append(my_string[0:int(pos)])
#     my_string = my_string[(pos + 1):len(my_string)]
#     my_string = my_string.strip()
#     my_string = my_string.split(" ")
#     for ell in my_string:
#         try:
#            my_string.remove("")
#         except ValueError:
#             ell = ell
#     hours_count = 0
#     for ell in my_string:
#         pos = str(ell).find("(")
#         if (pos != -1): hours_count += int(ell[0:pos])
#     hours.append(hours_count)
# my_dict = dict()
# my_dict = dict(zip(discipline, hours))
# print(f"Получился словарь:{my_dict}")


# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json

second_file = open("firms.txt", "r")
content = second_file.readlines()
second_file.close()
firm  = []
hours = []
profit = []
firm_dict = dict()
profit_dict = dict()

print(f"Содержимое файла {content}")

for el in content:
    my_string = str(el)
    my_string = my_string.strip()
    my_string = my_string.split(" ")

    for ell in my_string:
        try:
           my_string.remove("")
        except ValueError:
            ell = ell
    firm.append(my_string[0])
    hours_count = 0
    for ell in range(len(my_string)):
        if ell == 3 : profit.append(int(my_string[ell-1])-int(my_string[ell]))


    hours.append(my_string)
average_profit = 0
final_list =[]
for el in profit:
    if int(el) >0 : average_profit +=int(el)
average_profit = average_profit / len(profit)
firm_dict = dict(zip(firm, profit))
profit_dict = dict(zip(["average_profit"], [average_profit]))
final_list.append(firm_dict)
final_list.append(profit_dict)

print(f"Получился словарь:{hours}")
print(f"Фирмы:{firm}")
print(f"Фирмы:{profit}")
print(f"Фирмы:{average_profit}")
print(f"Словарь Фирмы:{firm_dict}")
print(f"Словарь Profit:{profit_dict}")
print(f"Финальный список:{final_list}")


with open("my_file.json", "w") as write_f:
    json.dump(final_list, write_f)
