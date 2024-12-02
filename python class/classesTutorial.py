class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def capitalize(word):
        return word[0].upper() + word[1:]

    def greet(self):
        return f"Hello there {Person.capitalize(self.name)}, and apparently your age is {self.age}"


person1 = Person("manuj", 19)
print(person1.greet())

person2 = Person("akshay", 20)
print(person2.greet())
