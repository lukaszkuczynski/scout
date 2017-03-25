class SlowJuicer:
    def squeeze(self, fruit):
        print('squeezing fruit %s' % fruit.name)

    def prepare_juice(self, fruits):
        for fruit in fruits:
            self.squeeze(fruit)


class Fruit:
    def __init__(self, name):
        self.name = name



if __name__ == '__main__':
    banana1 = Fruit("banana")
    banana2 = Fruit("banana")
    orange1 = Fruit("orange")
    orange2 = Fruit("orange")
    fruits = [banana1, banana2, orange1, orange2]
    slow_juicer = SlowJuicer()

    def oranges_generator(fruits):
        print("start yielding")
        for fruit in fruits:
            if fruit.name == "orange":
                print("yielding fruit.." + fruit.name)
                yield fruit
        print("no yields anymore.")

    slow_juicer.prepare_juice(oranges_generator(fruits))
