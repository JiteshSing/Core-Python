'''file = open("file.txt","r")
cont = file.read()

print(cont)
print(file.closed)
print(file.mode)
file = open("file.txt")
for line in file:
    print(line)
file.close()'''
######write mode##########
'''file = open("Test.txt","w")
file.write("Hi\n")
file.write("This is Python file")
file.close()
file = open("Test.txt","r")
cont = file.read()
print(cont)'''
####with statement###########
'''with open("Test.txt","w") as file:
    file.write("Hello\n")
    file.write("Hello this is file io")
'''
#####with statement read######
'''with open("Test.txt","r") as file:
    print(file.read())
    print( file.tell())
    print(file.seek(0,2))'''
import  os
#os.rename("Test.txt","Test1.txt")
os.remove("file.txt")