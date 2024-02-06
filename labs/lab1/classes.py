# Excercise 1
class Person:
    def __init__(self, name):
        self.name = name

    def greets(self, person):
        print(f'{self.name}: "Hello, {person.name}" ')


alice = Person("Alice")
bob = Person("Bob")
alice.greets(bob)


# Excercise 2


class Employee:
    def __init__(self, first_name, last_name, salary=10000):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def print_email(self):
        print(f"{self.first_name}.{self.last_name}@company.com")

    def increase_salary(self, rate):
        self.salary *= rate


jeff = Employee("Jeff", "Pepperoni")

print(jeff.get_fullname())
jeff.print_email()
print(jeff.salary)
jeff.increase_salary(5)
print(jeff.salary)
