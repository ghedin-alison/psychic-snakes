from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

    @abstractmethod
    def person_method(self):
        """Interface Method
            Abstract class can not be instatiate
            For interface classes there's a convention to use I before the class name, like IPerson
        """
        pass

class Student(IPerson):

    """
        To instantiate a class that inherit from interface method you should overwrite
        the method of the main class.
        We need to do that to hava an abstract class
    """

    def __init__(self):
        self.name = "Basic Student name"

    def person_method(self):
        print("I am a student")


# s1 = Student()
# print(s1)

class Teacher(IPerson):

    """
        To instantiate a class that inherit from interface method you should overwrite
        the method of the main class.
        We need to do that to hava an abstract class
    """

    def __init__(self):
        self.name = "Basic Teacher name"

    def person_method(self):
        print("I am a teacher")


s1 = Student()
s1.person_method()

t1 = Teacher()
t1.person_method()


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        elif person_type == "Teacher":
                return Teacher()
        else:
            print("Invalid Type")

if __name__ == "__main__":
    choice = input("What type of person do you want to create: \n")
    person = PersonFactory.build_person(choice)
    print(person)
    person.person_method()



