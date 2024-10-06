class Vehicle:
    __COLOR_VARIANTS = []

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = __engine_power
        self.__color = str(__color)

    def get_model(self, __model):
        return f'Модель: {__model}'

    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {__engine_power}'

    def get_color(self, __color):
        return f'Цвет: {__color}'

    def print_info(self, owner, __model, __engine_power, __color):
        return self.get_model(), self.__engine_power(), self.__color(), f'Владелец: {owner}'


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
    pass


# Текущие цветa
__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()