# 继承
from oop import User


class Student(User):
    def __init__(self, no, name, score):
        # not super.__init__(no, name)
        super().__init__(no, name)
        self.__score = score

    def to_string(self):
        print('--------- Student ---------')
        super().to_string()
        print('{score: %s}' % self.__score)


student = Student(2, 'Stock', 100)
student.to_string()
