class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return "Student(name = %s, age = %s)" % (self.name, self.age)

    def show(self):
        print("name = %s, age = %s" % (self.name, self.age))

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")


s = Student("Timothy", 23)

with s as s1:
    s1.show()
