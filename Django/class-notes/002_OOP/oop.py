
print("-----------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
# test = [122, 'victor', [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]
# print_types(test)

print("-----------------------------------")

# class Person:
#     name = "victor"
#     age = 32

# person1 = Person()
# person2 = Person()

# print(person1.name)
# Person.job = "developer"
# print(person2.job)
# print(person2.name)
# print(person1.job)

print("-----------------------------------")

#! class attributes vs instance attributes (Person class ı ve onun test, set_details, get_details, salute methodları)

# class Person:
#     company = "clarusway"
    
#     def test(self):
#         print("test")
        
#     def set_details(self, name, age):
#         self.name = name
#         self.age = age
        
#     def get_details(self):
#         print(self.name, self.age)
    
#     @staticmethod
#     def salute():
#         print("Hi there!")

# person1 = Person()
# person2 = Person()

# person1.location = "Turkey"
# print(person1.location) #! person1 ile person2 farklı dır location person2 de hata verecektir
# print(person2.location)

# person2.age = 25
# print(person1.age)
# print(person2.age)

# person1.test()
# Person.test(person1)
# person1.set_details("barry", 20)
# person1.get_details()
# print(person1.name)

# person1.salute()
# person2.salute()

print("-----------------------------------")


#! special methods ( init, str)

class Person:
    company = "clarusway"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
        
    def get_details(self):
        print(self.name, self.age)
    
    def __str__(self):
        return f"{self.name} - {self.age}"
    
person1 = Person("henry", 18)
person1.get_details()

person2 = Person("selçuk", 22)
person2.get_details()

print(person1)
print(person2)


#! OOP Principles (4 pillars)

#. encapsulation
#. abstraction
#. polymorhism
#. inheritance


#? encapsulation and abstraction
# class Person:
#     company = "clarusway"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self._id = 5000
#         self.__id = 3000
        

#     def __str__(self):
#         return f"{self.name} - {self.age}"

#     def get_details(self):
#         print(self.name, self.age)
 