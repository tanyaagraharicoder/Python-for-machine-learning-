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



class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

d= Dog()
d.sound()  # Output: Dog barks

# operator overloading 

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)   
v3 = v1 + v2
print(v3)
# Output: Vector(6, 8)
# Output: This is Parent class






