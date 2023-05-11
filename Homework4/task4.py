num = 1
def digits(num):
    digs = []
    while num != 0:
        digs.append(num % 10)
        num = num // 10
    return digs

def multiplication_chain(num):

    count_multy = 0
    while num > 9:
        digs = digits(num)
        mul = 1
        for digit in digs:
            mul = mul * digit
        num = mul
        count_multy+= 1

    return count_multy



data = [
    39, 4, 25, 999, 5050, 222333444
]

test_data = [
    3, 0, 2, 4, 1, 4
]


for i, d in enumerate(data):
    assert multiplication_chain(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')