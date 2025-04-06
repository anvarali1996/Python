# Small Python Project Demonstrating Design Patterns: Singleton, Factory, and Observer

# 1. Singleton Pattern
class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.settings = {}
        return cls._instance

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings.get(key)


# 2. Factory Pattern
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Unknown animal type")


# 3. Observer Pattern
class NewsPublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, news):
        for sub in self.subscribers:
            sub.update(news)

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news: {news}")


# Demo All Patterns Together
def main():
    print("--- Singleton Demo ---")
    config1 = AppConfig()
    config2 = AppConfig()
    config1.set("theme", "dark")
    print(config2.get("theme"))  # should be "dark"

    print("\n--- Factory Demo ---")
    for animal_type in ["dog", "cat"]:
        animal = animal_factory(animal_type)
        print(f"{animal_type.capitalize()} says: {animal.speak()}")

    print("\n--- Observer Demo ---")
    publisher = NewsPublisher()
    alice = Subscriber("Alice")
    bob = Subscriber("Bob")

    publisher.subscribe(alice)
    publisher.subscribe(bob)

    publisher.notify("Python 3.13 Released!")
    publisher.unsubscribe(bob)
    publisher.notify("New Design Pattern Tutorial Out!")

if __name__ == "__main__":
    main()
