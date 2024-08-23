class Talaba:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Kurs:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students_count = 0
        self.students = []

    def add(self, new_student):
        self.students.append(new_student)
        self.students_count += 1
        print(f"{new_student.name} ismli talaba {self.name} kursga qo'shildi.")

    def delete(self, student):
        if student in self.students:
            self.students.remove(student)
            self.students_count -= 1
            print(f"{student.name} ismli talba  {self.name} kursdan chiqarildi.")

    def info_course(self):
        print(f"kurs nomi: {self.name}")
        print(f"kurs o'qituvchsi: {self.teacher}")
        print(f"talabalar soni: {self.students_count}")
        print("talabalar ro'yhati:")
        for student in self.students:
            print(f"- {student.name}")

# kurs nomi va ustozi
kurs1 = Kurs("Python", "Odinaxon")
kurs2 = Kurs("Data Science", "Zarina")

# 10 talaba qo'shish
for i in range(1, 11):
    talaba = Talaba(f"Student {i}", 20)
    kurs1.add(talaba)
    kurs2.add(talaba)

# 2 ta talaba o'chirish
kurs1.delete(kurs1.students[0])
kurs1.delete(kurs1.students[1])
kurs2.delete(kurs2.students[0])
kurs2.delete(kurs2.students[1])

kurs1.info_course()
print()
kurs2.info_course()