# x=(1, 2,3)
# print(dir(x))
# print(x.__add__)


# # dict method 

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1= person("tanya",20)
# print(p1.__dict__)

# print (help(person))

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        super().show()   # call parent method
        print("This is Child class")
c= Child()
c.show_child()

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed
d = Dog("Buddy", "Golden Retriever")
print(d.name)  # Output: Buddy







