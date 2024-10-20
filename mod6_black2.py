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
        super().move()

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0):
        super().__init__(x_distance)
        super().__init__(y_distance)
        super().run()
        super().fly()


    def move(self):
        super().run()
        super().fly()



    def get_pos(self):
        return self.x_distance, self.y_distance

p1 = Pegasus()
print(p1.get_pos())
p1.move(100, 13)
