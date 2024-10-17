class Horse:
    def __init__(self,x_distance=0, sound='Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance



class Eagle:
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat' ):
        self.y_distance = y_distance
        self.sound = sound

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle ):
    def __init__(self, x_distanse=0, y_distanse=0):
        super().__init__()
        self.x_distance = x_distanse
        self.y_distance = y_distanse


    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print('I train, eat, sleep, and repeat')


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()