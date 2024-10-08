class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner: str, model: str, color='white', engine_power=1000):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color


    def get_model(self, __model):
        return f'Модель: {__model}'

    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {__engine_power}'

    def get_color(self, __color):
        return f'Цвет: {__color}'

    def print_info(self):

        print(self.get_model(self.__model))
        print(self.get_horsepower(self.__engine_power))
        print(self.get_color(self.__color))
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color='white'):
        color_variants = list(map(str.upper, self.__COLOR_VARIANTS))
        if new_color.upper() not in color_variants:
            print(f"Нельзя сменить цвет на {new_color}")
        else:
            self.__color = new_color
            return self.__color


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5




# Текущие цветa
__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

