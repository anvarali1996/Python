class Student:

    class_year = 2022
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sam", 26)


# print(Student.num_students)
print(f"My gruduating class of {Student.class_year} has {Student.num_students}")