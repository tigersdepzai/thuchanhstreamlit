class Student:
    all_students = []

    def __init__(self, name, math, literature, english):
        self.name = name
        self.math = math
        self.literature = literature
        self.english = english

        Student.all_students.append(self)

    def count_students():
        return len(Student.all_students)

    def average_all_students(cls):
        if len(cls.all_students) == 0:
            return 0
        
        total = 0
        for student in cls.all_students:
            total += (student.math + student.literature + student.english) / 3
        
        return total / len(cls.all_students)

    def average(self):
        return (self.math + self.literature + self.english) / 3


s1 = Student("Long ", 8, 7, 9)
s2 = Student("tâm", 6, 9, 8)
s3 = Student("Trọng", 10, 9, 9)


print("Tổng số học sinh:", Student.count_students())
print("Điểm TB của tất cả học sinh:", Student.average_all_students())
