#  string method
#  string are immutable
a="Tanya!!!!!!!!!!"
print(len(a))
print(a.lower())
print(a.upper())
print(a.rstrip("!"))
print(a.replace("Tanya", "Ankita"))
print(a.split(" "))
blogHeading = "this is my first blog  "
print(blogHeading.capitalize())

str1 ="this is string with leading and trailing spaces"
print(len(str1))
print(len(str1.center(50)))
#  conditional statements
age= int(input("enter ur age"))
print (" your age is ", age)
#  conditonal operator
# > ,< , >= , <= , == , !=
if (age>18):
    print (" you can drive")
else:
    print (" you can not drive")
    #  elif
num= 19 
if(num< 0):
    print (" number is negative")
elif (num==0):
    print (" number is zero")
else:
    print (" number is positive")
     





