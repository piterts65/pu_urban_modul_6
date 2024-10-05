class Animal:
    alive = True  #(живой)
    fed = False  #(накормленный)

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = Plant.edible
        if self.food is False:
            print(f'{self.name} съел {food.name}')
            return Animal.fed == True
        elif self.food is not False:
            print(f'{self.name} не стал есть {food.name}')
            return Animal.alive == False

class Mammal(Animal):
    pass
class Predator(Animal):
    pass

class Plant:
    edible = False  #(съедобность)

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)