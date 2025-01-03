# CLASS METHODS

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa) -> None:
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"total of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
        
student1 = Student("Spongebob", 3.2)
student2 = Student("Alex", 2.0)
student1 = Student("Spongebob", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())
