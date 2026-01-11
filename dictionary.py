
# dic2={
#     344:"tanya",
#     456:"shivam",
#     789:"shivanya",

# }
# print(dic2[344])

# info ={
#     "name":"tanya",
#     "age":20,
#     "city":"delhi",
#     "is_student":True,
# }
# print(info["name"])
# print(info.get("age"))
# print(info.keys())
# print(info.values())
# print(info.items())

# ep1={122:45, 123:67, 124:89}
# ep2={125:90, 126:78, 127:56}
# ep1.update(ep2)
# print(ep1)
# ep1.clear()
# print(ep1)
# ep1.pop(122)
# print(ep1)

# for loop with else in python
# for i in range(5):
#     print(i)
# else:
#     print("loop is ended")
# excepio handling

# a=input("enter the number")
# print("multication table of",a  )
# try:
#     for i in range(1,11):
#         print(f"{a} x {i} = {int(a)*i}")
# except Exception as e:
#     print("invalid input",e)

# print(" important codes")


# finally - 
# l = [1, 2, 3, 4, 5]

# try:
#     i = int(input("Enter the index: "))
#     print(l[i])

# except IndexError:
#     print("Index out of range")

# finally:
#     print("Execution completed")

#  raising custom exception
# a=(int(input("enter any value between 5 and 9: ")))

# if(a<5 or a>9):
#     raise ValueError("value should be between 5 and 9 ")

# if else in one line 
# print("a") if(a>b) else print("b")  

# enumerate function in python 
# l=["shivam","shivanya","ankit"]
# for index, value in enumerate(l):
#     print(f"index is {index} and value is {value}")
#     if(value=="shivam"):
#         print("found the value shivam  here ",index)
#         break
# # print(list(enumerate(l)))

marks=[12, 23, 89, 45, 67, 233,12]
for index ,marks in enumerate(marks):
    print(marks)
    if (index==3):
        print("found tanya  at index ",index)
       



