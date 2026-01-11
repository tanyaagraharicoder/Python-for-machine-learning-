# f= open('myfile.txt', 'r')
# # print (f)
# text= f.read()
# print(text)
# f.close()

# f= open('myfile.txt', 'w')
# f.write("Hello World!\n")
# f.close()


# with open('myfile.txt', 'r') as f:
#     text= f.read()
#     print(text)

# f = open('myfile.txt', 'r')

# i = 0
# while True:
#     line = f.readline()
#     if not line:
#         break

#     i += 1
#     line = line.strip()   # remove newline

#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])

#     print(f"Marks of student {i} in Maths is: {m1 * 2}")
#     print(f"Marks of student {i} in Science is: {m2 * 2}")
#     print(f"Marks of student {i} in English is: {m3 * 2}")
#     print()

# f.close()

# tell method -- returns the current position of the file pointer 
f = open("sample.txt", "r")

print(f.tell())      # 0 (start of file)
f.read(5)
print(f.tell())      # 5

f.close()



# seek method -- moves the file pointer to a specific position
f = open("sample.txt", "r")

f.read(10)
print(f.tell())   # 10

f.seek(0)
print(f.tell())   # 0

f.close()













