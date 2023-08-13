#!/usr/bin/python3
""" Write beautiful code that passes the pycodestyle checks. """

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        return self.age >= 18

# Example usage
if __name__ == "__main__":
    person1 = Person("John", "Doe", 25)
    print("Full Name:", person1.get_full_name())
    print("Is Adult:", person1.is_adult())

