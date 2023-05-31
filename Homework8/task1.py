import unittest

def treatment_sum(our_tuple: tuple):
    try:
        if len(our_tuple) == 2:
            summa = our_tuple[0] + our_tuple[1]
            return summa
        elif len(our_tuple) < 2:
            return 'Недостаточно данных'
        else:
            return 'Много данных'

    except TypeError:
        return 'Нельзя сложить эти данные'


class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, 5), (3, '7'), (3,), (), ('23', '32')]

        test_data = [8, 'Нельзя сложить эти данные', 'Недостаточно данных', 'Недостаточно данных', '2332']

        for i, d in enumerate(data):
            assert treatment_sum(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
            print(f'Тестовый набор {d} прошёл проверку')

        with self.assertRaises(Exception):
            treatment_sum((3, 4, 5))
        try:
            treatment_sum((3, 4, 5))
        except Exception as e:
            assert e.args[0] == 'Много данных', 'Исключение имеет неправильный текст'
        print('Всё ок')


if __name__ == '__main__':
    unittest.main()