from time import localtime

if(localtime().tm_hour<12):
    print("Good Morning!")
elif(localtime().tm_hour<18):
    print("Good Afternoon!")

else:
    print("Good Evening!")
# match statement
day= input(" enter day ")
match day:
    case "monday":
        print (" today is monday")
    case "tuesday":
        print (" today is tuesday")
    case "wednesday":
        print (" today is wednesday")
    case "thursday":
        print (" today is thursday")
    case "friday":
        print (" today is friday")
    case "saturday":
        print (" today is saturday")
    case "sunday":
        print (" today is sunday")
    case _:
        print (" invalid day")
 # loops in python
for i in range (1,11):
    print (i)
name = 'tanya agrahari'
for char in name:
    print (char)
colors =["red", "green", "blue", "yellow"]
for color in colors:
    print (color) 
    for i in color :
        print (i)     
# while loop  
j=0
while (j<10):
    print (j)
    j+=1

#       