from learn.Person import Person

class Student(Person):
    def __init__(self,name,age):
        super().__init__()
        self.name = name
        self.__age = age

    def foo1(self):
        print("foo 被调用了")

    def __foo2(self):
        print("_foo2 被调用了")

    def run(self):
        print(f'{self.name} is running...')