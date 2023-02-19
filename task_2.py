index_list = input("Введите строку: ")
index_number = int(input("Номер символа: "))

index_number -= 1
left_index_number = index_number - 1
ring_index_number = index_number + 1
index_list_push = []
count = 0
index_list = list(index_list)
long_ist = len(index_list)


if left_index_number < ((long_ist - long_ist) + 1):
    print('Символ слева: - ')
else:
    print(f'Символ слева: {index_list[left_index_number]}')


if ring_index_number > (long_ist-1):
    print('Символ справа: - ')
else:
    print(f'Символ справа: {index_list[ring_index_number]}')


if index_number == ring_index_number and index_number == left_index_number:
    print('Есть два таких же')
elif index_number == ring_index_number or index_number == left_index_number:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет')
