# 2.Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

second_file = open("new 1.txt")
content = second_file.readlines()
second_file.close()
#print(second_file)


string_count = 0
words_in_string_count = []
for el in content:
    string_count +=1
    el.strip()
    new_string = el.split(" ")
    words_count = 0
    for new_el in new_string:
        words_count += 1
    words_in_string_count.append(words_count)

print(f"Количество строк: {string_count}")
print(f"Слов в строках {words_in_string_count}")