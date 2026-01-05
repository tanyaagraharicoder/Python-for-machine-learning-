# def fact(n):
#     """Compute the factorial of n recursively.

#     Args:
#         n (int): A non-negative integer.

#     Returns:
#         int: The factorial of n.
#     """
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
# number = 5
# result = fact(number)
# print(f"The factorial of {number} is {result}")

#  set
name ={"tanya", "agrahari", "tanya"}
print(name)
name.add("hello")
print(name)
name.remove("agrahari")
print(name)
name.discard("notfound") # no error
print(name)
info ={"carlo" , 19 , True ,5.6}
# set method 
# joining sets
# set1 ={1,2,3}
# set2 ={4,5,6}
# set3 = set1.union(set2)
# print(set3)
# set1.update(set2)
# print(set1)

cities1 ={"tokyo", "newyork", "delhi"}
cities2 ={"delhi", "paris", "london"}
common = cities1.intersection(cities2)
print(common)
diff = cities1.difference(cities2)
print(diff)
symmetric_diff = cities1.symmetric_difference(cities2)
print(symmetric_diff)
issubset = cities1.issubset(cities2)
print(issubset)
issuperset = cities1.issuperset(cities2)
print(issuperset)
# pop
del cities1
print(cities1)






