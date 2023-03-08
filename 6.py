# Блок ввода данных
n = int(input('Введите коэффициент n: '))
m = int(input('Введите коэффициент m: '))
k = int(input('Введите коэффициент k: '))
t = int(input('Введите коэффициент t: '))

if n != 0:
    # Если n не равно 0, то для решения задачи воспользуюсь формулой Кардано для решения уравнений 3-ей степени.
    # Найдём коэффициенты p и q:
    p = ((3 * n * k) - (m ** 2)) / (3 * (n ** 2))
    q = ((2 * m ** 3 - 9 * n * m * k) + (27 * n ** 2 * t)) / (27 * (n ** 3))
    # Вычислим коэффициент Q, при помощи которого можно выяснить кол-во корней кубического уравнения:
    Q = ((p / 3) ** 3) + ((q / 2) ** 2)
    # По формуле Кардано:
    if Q > 0:
        print('Уравнение имеет 1 действительный корень.')
    elif Q < 0:
        print('Уравнение имеет 3 действительных корня.')
    elif Q == 0:
        if p == q and p == 0:
            print('Уравнение имеет 1 действительный корень.')
        else:
            print('Уравнение имеет 2 действительных корня.')
else:
    if m != 0:
        # Если n равно 0, а m не равно 0, то для решения задачи воспользуюсь формулой решения квадратного уравнения.
        D = (k ** 2) - (4 * m * t)
        if D > 0:
            print('Уравнение имеет 2 действительных корня.')
        elif D == 0:
            print('Уравнение имеет 1 действительный корень.')
        elif D < 0:
            print('Уравнение не имеет корней.')
    else:
        if k != 0:
            # Если n равно 0, m не равно 0, а k не равно 0, то получается линейное уравнение,
            # которое всегда имеет 1 корень.
            print('Уравнение имеет 1 действительный корень.')
        else:
            # Если n равно 0, m не равно 0, a k равно 0, то получается линейное уравнение.
            if t == 0:
                # Уравнение имеет бесконечно много корней, т.е. их точное количество определить невозможно.
                print('*')
            else:
                print('Уравнение не имеет корней.')
