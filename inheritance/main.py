  
class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.is_alive = True

    def sleeping(self):
        print(f"{self.name} is sleeping")
    
    def eat(self):
        print(f"{self.name} is eating")

    def ages(self):
        print(f"{self.name} is {self.age} years old")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUIK!")

dog = Dog("Scooby", 5)
cat = Cat("Garfield", 3)
mouse = Mouse("Mickey", 2)

print(dog.name)
dog.speak()
# print(dog.is_alive)
# dog.eat()
# dog.sleeping()
# dog.ages()
print("=================")
print(cat.name)
cat.speak()
# print(cat.is_alive)
# cat.eat()
# cat.sleeping()
print("=================")
print(mouse.name)
mouse.speak()