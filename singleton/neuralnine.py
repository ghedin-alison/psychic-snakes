from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def print_data(self):
        pass

class PersonSingleton(IPerson):

    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Pattern Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


p = PersonSingleton("Mike", 30)
print(p)
p.print_data()

# p2 = PersonSingleton("Ana", 28)
p2 = PersonSingleton.get_instance()
print(p)
p.print_data()
