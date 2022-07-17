class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("Play game")


class Puppy(Dog):
    def game(self):
        print("Puppy play")


class Person:
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s with %s" % (self.name, dog.name))

        dog.game()

dog = Puppy("UU")
person = Person("bill")

person.game_with_dog(dog)