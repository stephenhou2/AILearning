from learn.Student import Student


class School:
    def __init__(self):
        pass


    def test(self):
        student = Student("张三",10)
        student.foo1()
        print(student.name)

        student._Student__foo2()
        print(student._Student__age)

    def run(self):
        print("school is running...???")



sch = School()
sch.test()





