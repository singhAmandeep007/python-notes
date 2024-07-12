class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def legs(self):
        return 4


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def legs(self):
        return 4
