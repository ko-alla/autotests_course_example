class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand                 # 1. Марка
        self._engine_power = engine_power  # 2. ЗАЩИЩЕННЫЙ (protected) атрибут engine_power - Мощность двигателя
        self.year = year                   # 3. year - Год выпуска
        self.color = color                 # 4. color - Цвет
        self.max_speed = max_speed         # 5. max_speed -максимальная скорость


    @property
    def info(self):
        return "Марка автомобиля: " + self.brand + " Цвет: " + str(
            self.color) + "Год выпуска: " + self.year + "Мощность двигателя: " + self.engine_power


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed
        self.passengers = passengers
        self.__park = park
        self._fare = fare

    @property
    def park(self):
        if (int(self.__park) < 9999 and int(self.__park) > 1000):
            return int(self.park)


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed
        self.__route = route
        self.path = path
        self._fare = fare

    @property
    def how_long(self):
        time = self.max_speed / (4 * self.path)
        return time
