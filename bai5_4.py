class Student:
    def __init__(self, name, classroom, school, address, family):
        self.name = name
        self.classroom = classroom
        self.school = school
        self.address = address
        self.family = family

    def introduce_school_class(self):
        print("🏫 SCHOOL & CLASS INTRODUCTION 🏫")
        print(f"👤 Name: {self.name}")
        print(f"📚 Class: {self.classroom}")
        print(f"🏫 School: {self.school}")
        print(f"📍 Address: {self.address}")
        print("❤️ I really love my school and my class!\n")

    def introduce_family(self):
        print("👨‍👩‍👧‍👦 FAMILY INTRODUCTION 👨‍👩‍👧‍👦")
        print(f"🏡 My family includes: {self.family}")
        print("💞 My family always loves and supports each other.")
        print("😊 I am very happy to be in my family!\n")



student1 = Student(
    name="Trong",
    classroom="6/5",
    school="Phan Văn Trị Secondary School",
    address="hông biết nữa , hông nhớ nữa",
    family="me ,......................:))........."
)


student1.introduce_school_class()
student1.introduce_family()
