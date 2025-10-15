class Person:
    def __init__(self, name, age):
        self.__name = name   # private attribute
        self.__age = age     # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

person1 = Person("Rahul", 20)
print(person1.get_name())   # Access via getter
person1.set_age(25)
print(person1.get_age())
