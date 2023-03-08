import sys

sys.set_int_max_str_digits(0)  # Чтобы избежать ошибки ValueError и лимит в 4300 символов, снимаем ограничение.

num = []
numbers_count = 0

# В следующем цикле создаётся массив чисел от 1 до 4095,
# а после каждый его элемент сразу переводится в четверичную с.с.
for i in range(4095):
    n1 = ''
    n2 = ''
    while i > 0:
        n1 = n1 + str(i % 4)
        i = i // 4
    n1 = list(reversed(n1))
    for j in range(len(n1)):
        n2 += n1[j]
    num.append(n2)

num = ''.join(map(str, num[1::]))  # Соединение всех элементов списка в одно число, причём исключая первый элемент,
# так как это не число, а пустая строка "".
num = hex(int(num, 4))  # Перевод получившегося числа в шестнадцатеричную с.с.

# Подсчёт всех чисел в num.
for i in range(len(num)):
    if num[i].isdigit():
        numbers_count += 1

print('Число содержит', numbers_count, 'цифр.')  # Вывод ответа.
