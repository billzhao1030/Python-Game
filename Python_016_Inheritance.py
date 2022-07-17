class Animal:
    def sleep(self):
        print("animal sleep")


class Plant:
    @staticmethod
    def grow():
        print("grow")

    def sleep(self):
        print("plant sleep")


class Dog(Animal):
    def sleep(self):  # override
        super().sleep()  # use super class method
        print("dog sleep")


class Grass(Plant, Animal):
    pass


if __name__ == "__main__":
    dog = Dog()
    dog.sleep()

    grass = Grass()
    grass.sleep()
