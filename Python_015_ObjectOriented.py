# __method name__ is builtin method for object

class Student:
    age = 18

    def __init__(self, name):
        self.__name = name  # add __ to become private

    def get_name(self):
        return self.__name

    def __str__(self):
        return "Student: %s" % student.__name

    def __set_name(self, name):
        self.__name = name

    @classmethod
    def student_play(cls):
        cls.age += 1

    @staticmethod
    def play():
        print("Static play")


student = Student("bill");

print(student._Student__name)  # cheating private
print(student.get_name())
print(student)
print(Student.age)
print(student.age)

Student.student_play()
Student.play()
