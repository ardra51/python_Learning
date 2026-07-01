'''
class students:
    institute="oneteam"

    def get_details(self,n,p):
        self.name=n
        self.place=p
    def display(self):
        print(f"hello {self.name} you are from{self.place}")


std1=students()
std2=students()

std1.get_details("akshay","kochi")
std2.get_details("joyal","kottayam")

std1.display()
std2.display()
'''

'''
class students:
    institute="oneteam"

    def __init__(self,n,p):
        self.name=n
        self.place=p
    def display(self):
        print(f"hello {self.name} you are from {self.place}")


std1=students("ardra","kochi")
std2=students("paru","kannur")

std1.display()
std2.display()

'''

'''
class students:
    institute="oneteam"
    age=21

    def __init__(self,n,p,m):
        self.name=n
        self.place=p
        self.mark=m
    def display(self):
        print(f"hello my name is {self.name} i am from {self.place} i got {self.mark} ")

std1=students("ardra","kollam",80)
std2=students("lekshmi","kollam",90)

std1.display()
std2.display()

'''

'''
class students:
    institute="oneteam"

    def __init__(self,n,p):
        self.name=n
        self.place=p
    def display(self):
        print(f"hello {self.name} you are from {self.place}")

class pythonstudents(students):
    def __init__(self,c,n,p):
        self.course=c
        super().__init__(n,p)

pstd1=pythonstudents("python fullstack","akshay","kochi")
pstd1.display()'''