from math import *
class Segment:
    def __int__(self, x: tuple, y: tuple):
        self.x1, self.y1 = x  # координаты первой точки
        self.x2, self.y2 = y  # координаты второй точки

    def length(self):
        dlina_otr = round(sqrt(self.x2 - self.x1) + sqrt(self.y2 - self.y1))
        return dlina_otr

    def x_axis_intersection(self):
        if self.y1 * self.y2 < 0:
            return True
        else:
            return False

    def y_axis_intersection(self):
        if self.x1 * self.x2 < 0:
            return True
        else:
            return False

data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')