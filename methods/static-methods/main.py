# STATIC METHODS
# joob = input("Enter job: ")
class Employee:

    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position
    
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Alex", "Cashier")
employee3 = Employee("Ali", "Cook")
# print(joob)
print("=====================")
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# print(Employee.is_valid_position(joob))

