
#public

class Student:
    def __init__(self):
        self.name = "Alice"

obj = Student()
print(obj.name)

#protected members

class student:
    def __init__(self):
        self._age = 20
obj = student()
print(obj._age)

#private

class Student:
    def __init__(self):
        self.__marks = 90

obj = Student()

# print(obj.__marks)   # Error
class Student:
    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

obj = Student()
print(obj.get_marks())