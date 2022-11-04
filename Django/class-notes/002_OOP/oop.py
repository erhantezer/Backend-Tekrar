print("hello")
print("-----------------------------------")
# def print_types(data):
#     for i in data:
#         print(i, type(i))
        
# test = [122, 'victor', [1,2,3], (1,2,3), {1,2,3}, True, lambda x:x]
# print_types(test)


class Person:
    name = "victor"
    age = 32

person1 = Person()
person2 = Person()

print(person1.name)
Person.job = "developer"
print(person2.job)
print(person2.name)
print(person1.job)

#! class attributes vs instance attributes 
