# inheritance turlari
# single a dan b voris oladi
# multilevel a dan b b dan c voris oladi
# multiple buni otalari ko'p
# gibrid single + multiple aralash inheritance
# heirarchial buni bolalari ko'p
# 


# class Person():
#     def __init__(self,name,age,adress):
#         self.name=name
#         self.age=age
#         self.adress=adress
    
#     def gapir(self,name):
#         print(f"salom mening ismim {name}")

# class Student1(Person):
#     def __init__(self, name, age, adress,university):
#         super().__init__(name, age, adress)
#         self.university=university
    
#     def __gt__(self,other):#taqqoslash kattami
#         return self.age>other.age

# class Student(Person):
#     def __init__(self, name, age, adress,university):
#         super().__init__(name, age, adress)
#         self.university=university
    
#     def __gt__(self,other):
#         return self.age>other.age
    


# person=Person("Odinaxon",22,"farg'ona")
# student=Student("Odinaxon",22,"Farg'ona","FarDU")
# student1=Student1("Odinaxon",23,"Farg'ona","FarDU")
# print(student>student1)





# danr metodlar classlarni taqqoslash uchun
# __gt__ kattami
# __eq__ tengmi
# __dte__ katta yoki tengmi
# __str__ stringmi
# 




# polimorphizm 3 hil
# 1 operatoroverload-matematik va boshqa operatorlarni qayta qayta ishlatish
# 2 methodoverload-methodlarni qayta qayta ishlatish 
# 3 methodoverride-ikkita clasni ichida bir hil method bo'lsa va ustiga yana  yozsam
# 4 gucktyping-ikkita clasni ichida bir hil method bo'lsa va shu method qayta qayta ishlasaa


# 1,2
# print(12+13)
# print(16+13)

# 3,4
# class Person:
#     def __init__(self,name) :
#         self.name=name
#     def gapir(self,name):
#         print(f"salom mening ismim {name}")

# class Student(Person):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def gapir(self,name):
#         print(f"hammaga salom ismim {name}")

# person=Person("Odinaxon")
# student=Student("Odinaxon")
# for i in [student,person]:
#     i.gapir("Odinaxon")



# imtihon
# 1.list touple dict set data type 
# touple da 2 ta metod bor index va count
# 2.anonim funksiya lambda funksiya o'zi qiymat qaytaradi
# 3.loop operatorlari  
# 4.funksiyalar
# 5.xatoliklar bilan ishlash
# 6.fayllar bilan ishlash







































