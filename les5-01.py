# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_list =[]
print("Введите информацию для сохранения в файл:")
while True:
    my_string = input()
    my_list.append(my_string)
    if my_string == "":
        break
try:
    with open("My_first_text.txt", "a+") as f_obj:
        for el in my_list:
            f_obj.write(str(el)+"\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")