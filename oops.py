class Person:
    name="Harry"
    occupation= "Software Developer"
    netwoth=10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
print(a.name);  
print(a.info()) 