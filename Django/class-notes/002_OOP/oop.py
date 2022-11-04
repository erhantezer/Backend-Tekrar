
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

class Person:
    company = "clarusway"
    
    def test(self):
        print("test")
        
    def set_details(self, name, age):
        self.name = name
        self.age = age
        
    def get_details(self):
        print(self.name, self.age)
    
    @staticmethod
    def salute():
        print("Hi there!")

person1 = Person()
person2 = Person()
