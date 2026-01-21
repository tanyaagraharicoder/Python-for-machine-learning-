x=(1, 2,3)
print(dir(x))
print(x.__add__)


# dict method 

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1= person("tanya",20)
print(p1.__dict__)

print (help(person))

