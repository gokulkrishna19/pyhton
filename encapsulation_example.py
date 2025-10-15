class Student:
    def __init__(self, name, age):
        # private attributes (encapsulated)
        self.__name = name
        self.__age = age

    # getter method for name
    def get_name(self):
        return self.__name

    # setter method for name
    def set_name(self, name):
        self.__name = name

    # getter method for age
    def get_age(self):
        return self.__age

    # setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

# creating an object
student1 = Student("Gokul", 21)

# accessing private data using getter
print("Name:", student1.get_name())
print("Age:", student1.get_age())

# modifying private data using setter
student1.set_age(22)
print("Updated Age:", student1.get_age())

# trying to access private variable directly (will fail)
# print(student1.__age)  # ❌ AttributeError
