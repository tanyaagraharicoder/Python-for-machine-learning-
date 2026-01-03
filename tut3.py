def calculateGmean(a,b):
    """Calculate the geometric mean of two numbers a and b."""
    gmean = (a * b) ** 0.5
    return gmean


a= 9
b= 16
print("Geometric mean of", a, "and", b, "is",     calculateGmean(a,b))     



def isGreater(a,b):
    """Check if a is greater than b."""
    if(a > b):
        return True
    else:
        return False 

isGreater(45,78)
print(isGreater(45,78))



def isLesser(a,b):
    pass
#  default augment
def average(a=9, b=1):
    print (" the average is ", (a+b)/2)

average()


# keyword argument
def personDetails(name, age=90):
    print("Name:", name)
    print("Age:", age)
personDetails(name="Alice")

#  variable argument
def sumAll(*args):
    total = 0
    for num in args:
        total += num
    return total

