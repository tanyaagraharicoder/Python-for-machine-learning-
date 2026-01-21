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


def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Have a nice day")

    return mfx


# @greet
def hello():
    print("hello world")


# hello()

greet(hello)
