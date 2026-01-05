# tup =(1,2,4)
# print(tup)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# print(tup[2])
# countries = ('India', 'USA', 'UK', 'Canada')
# print(countries)
# temp = list(countries)
# temp[0] = 'China'
# countries = tuple(temp)
# print(countries)
# # countries[0] = 'China'  # This will raise an error because tuples are immutable
# print(countries.count('India'))
# tuple1=(0,1,3,4,5,6)
# print(tuple1.index(3, 1,3))
# print(len(tup))


# # f-string
# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")
# print("My name is {} and I am {} years old.".format(name, age)) 


#  docstring
# def add(a, b):
#     """This function adds two numbers and returns the result."""
#     return a + b
# result = add(5, 3)
# print(f"The result of addition is: {result}")
# print(add.__doc__)

# PEP 8
def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    import math
    area = math.pi * radius ** 2
    return area
radius = 5
area = calculate_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")



