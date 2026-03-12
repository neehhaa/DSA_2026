class Student:
    def __init__(self,name):
        print(id(self))
        self.name = name

    def info(self):
        print("name: ", self.name)


s = Student("neha")
s1 = Student("xyz")
print(id(s))
print(id(s1))