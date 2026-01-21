# class Person:
#     name="Harry"
#     occupation= "Software Developer"
#     netwoth=10

#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a=Person()
# print(a.name);  
# a.name= "tanya"
# print(a.info()) 


# class Person:
#     def __init__(self,n,o):
#         print("Hey i m a person")
#         self.name=n
#         self.occ= o

#     def info(self):
#         print(f"{self.name} is a {self.occ}")    
        

# a=Person( "tanya","dev")
# a.info()

# decorators


# def greet(fx):
#     def mfx():
#         print("Good morning")
#         fx()
#         print("Have a nice day")

#     return mfx


# # @greet
# def hello():
#     print("hello world")


# # hello()

# greet(hello)




#  without getter and setter 

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p= Person("tanya",20)
# print(p.age)  # direct access to age attribute

# p.age= -5  # direct modification to age attribute
# print(p.age)  # incorrect age value

# # with getter and setter


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.set_age(age)

#     def get_age(self):
#         return self._age

#     def set_age(self,age):
#         if age < 0:
#             print("Age cannot be negative. Setting age to 0.")
#             self._age = 0
#         else:
#             self._age = age




# p= Person("tanya",20)
# print(p.get_age())  # access age via getter
# p.set_age(-5)  # attempt to set a negative age
# print(p.get_age())  # age is now corrected to 0



# inheritance in python 

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary= salary

#     def info(self):
#         print(f"{self.name} earns {self.salary} per month")


# class Developer(Employee):
#     def __init__(self,name,salary,lang):
#         super().__init__(name,salary)
#         self.lang= lang

#     def info(self):
#         super().info()
#         print(f"{self.name} works with {self.lang}")


# d= Developer("tanya",5000,"python")
# d.info()
# e= Employee("harry",7000)
# e.info()



#  access moifiers in python

# class Employee:
#     def __init__(self):
#         self.name="tanya"      # public
#         self._salary=5000      # protected
#         self.__networth= 10000  # private

# a= Employee()
# print(a.name)          # public access
# print(a._salary)       # protected access (conventionally should be treated as non-public)

# # print(a.__networth)    # private access (will raise AttributeError)
# print(a._Employee__networth)  # accessing private attribute using name mangling



# Static method and class method in python

# class MathOperations:
#     @staticmethod
#     def add(x, y):
#         return x + y

#     @classmethod
#     def multiply(cls, x, y):
#         return x * y


# # Using static method
# sum_result = MathOperations.add(5, 3)
# print(f"Sum: {sum_result}")
# # Using class method
# product_result = MathOperations.multiply(5, 3)
# print(f"Product: {product_result}")


# instance variable 

# class Person:
#     def __init__(self,name,age):
#         self.name=name      # instance variable
#         self.age=age        # instance variable

# p1= Person("tanya",20)
# p2= Person("harry",25)
# print(p1.name, p1.age)  # Output: tanya 20
# print(p2.name, p2.age)  # Output: harry 25


# #  class variable 

# class student:
#     school_name= "ABC High School"   # class variable

#     def __init__(self,name,grade):
#         self.name=name        # instance variable
#         self.grade=grade      # instance variable

# s1= student("tanya","A")
# s2= student("harry","B")

# print(s1.name, s1.grade, s1.school_name)  # Output: tanya A ABC High School

#  class method in python 


class Employee:

    company= "Apple"

    def show(self):
        print(f"Employee works at {self.company}  and name is {self.name}")

        @classmethod
        def changeComapny(cls,new_company):
            cls.company= new_company

e1= Employee()
e1.name= "tanya" 

e1.show()

e1.changeComapny("Google")
e1.show()
print(Employee.company)































