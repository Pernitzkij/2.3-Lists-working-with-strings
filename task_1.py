index_list = input("Введите строку: ")
index_list_push = []
count = 0
index_list = list(index_list)

redact = ";"
for i in index_list:
    if i == ":":
        index_list_push.append(';')
        count += 1
    else:
        index_list_push.append(i)


print(f"Исправленная строка: {(''.join(index_list_push))}")
print(f'Кол-во замен: {count}')
