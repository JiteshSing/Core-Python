# person class
'''class Person:
    name = ""
    dob = ""
    address = ""

    def setName(self,name,dob,address):
        self.name = name
        self.dob = dob
        self.address = address

    def getName(self):
        return self.name,self.dob,self.address
     #   return self.dob

obj = Person()
obj.setName("rays","04-22-33","President Tower")
print(obj.getName())'''

# Account class
'''class Account:
    number = ""
    type = ""
    balance = ""

    def setDetails(self, number, type, balance):
            self.number =number
            self.type = type
            self.balance = balance


    def getDetails(self):
        return self.number,self.type,self.balance


obj = Account()
obj.setDetails("322214563", "saving", "4595")
print(obj.getDetails())'''

# Automobile
'''class Automobile:
    color =""
    speed = 0
    makers = "TATA"

    def setColor(self, color):
        self.color = color

    def setspeed(self,speed):
        self.speed = speed

    def setmakers(self, makers):
        self.makers = makers

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    def getMakers(self):
        return self.makers

obj = Automobile()
obj.setColor("Blue")
#obj.setspeed(80)
obj.setmakers("Honda")
print(obj.getColor())
print(obj.getSpeed())
print(obj.getMakers())'''

# default constructor
'''class A:
    age = 10
    print(age)

obj = A()'''

'''class A:
    "learn coding "
    age = 10
    print(age)

obj = A()
print(obj.age)
print(A.age)
print(obj.__doc__)
print(A.__doc__)'''

# 3
'''class A:
    age = 10
    def fun(self):
        "hi I AM fRee"
        name = "learn coding"

        print(name)

obj = A()
obj.fun()
print(obj.age)
print(A.age)
print(A.fun.__doc__)'''

'''class B:
    laptop = "DELL"
   def computer(self):
        "It's a new laptop"

        name = "MSI Laptop"

        print(name)

obj = B()
obj.computer()
print(obj.laptop)
print(B.laptop)
print(obj.computer.__doc__)'''

# Call by Constructor

'''class C:

    def __init__(self, name, age, address):
        print(f"{name} {age} {address}")

    def fun(self,age,name,address):
        print(f"{age} {name} {address}")

obj = C("Rays", "20" , "Indore")
obj.fun("25","Tech","BHopal")'''

'''class Calculator:
    def sum(self,a,b):
        c= a+b
        print("Sum = ",c)

    def multi(self,a,b):
        print("Multi = ", a*b)

    def subt(self,a,b):
        print("Subtraction = ",a-b)

    def divison(self,a,b):
        if(b==0):
            print("It's not divide by 0")
        else:
            print("Divide = ",a/b)


obj = Calculator()
obj.sum(4,5)
obj.multi(5,6)
obj.subt(10,5)
obj.divison(10,0)
obj.divison(20,2)'''

#
'''class A :
    a = 10
    _b = 20
    __c =30

   # print(a," ",_b," ",__c)

obj = A()
print(obj.a)
print(obj._b)
#print(obj.__c)'''

###
'''class C :
    a= 10
    _b=20
    __c= None

    def Add(self):
        self.__c = self.a + self._b
        print("Add ",self.__c)

obj = C()
obj.Add()
print(obj.a)
print(obj._b)
#print(obj.__c)'''

##
'''class A :
    a =10
    _b= 20
    __c = None

class B(A):

    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)

obj = B()
obj.show()
'''

###

'''class A:
    a = 10
    _b = 20
    __c = None
    print(a,"",_b,"",__c)

class B :
    def show(self):
        print(A.a)
        print(A._b)
        print(A.__c)

obj =B()
obj.show()'''

'''class Math:
    def max(a,b):
        if(a>b):
            print(a)
        else:
            print(b)

Math.max(5,10)

obj = Math()'''

###
'''class A :
    a= 10
    _b= 20
    __c = 30

    print(a,"",_b,"",__c)

obj = A()
print(obj.a)
print(obj._b)
print(obj.__c)'''
##
'''class C:
    a = 10
    _b = 20
    __c = None

    def Add(self):
        self.c = self.a + self._b
        print("Add = ",self.c)


obj = C()
obj.Add()
print(obj.a)
print(obj._b)
print(obj.__c)'''

##
'''class C :
    a = 10
    _b = 20
    __c = None

class B(C):
    def show(self):
        print(C.a)
        print(C._b)
        print(C.__c)

obj = B()
obj.show()
'''
###
'''class D:
    a = 10
    _b = 20
    __c = None
    print(a,"",_b,"",__c)
class F(D):
    def show(self):
        print(D.a)
        print(D._b)
        print(D.__c)

obj = F()
obj.show()'''
##
'''class A :
    a= 10
    _b = 20
    __c=30
    print(a,_b,__c)

obj = A()
print(obj.a)
print(obj._b)
print(obj.__c)'''

'''class B :
    a =10
    _b =20
    __c =None

    def show(self):
     self.__c=self.a+self.__b
     print("Sum = ",self.__c)


obj = B()
obj.show()
print(obj.a)
print(obj._b)
print(obj.__c)
'''
## single level inheritance
'''class A:
    l = 20
    b = 10
   # a = None

    def area(self):
       self.a = self.l * self.b
       print("Area = ",self.a)

class B(A):
    def are(self):
        print("This is subclass")

obj = B()
obj.area()'''
#obj.showdisB()
#obj.showdisA()

class Shape:
    def __init__(self,color):
        self.color = color

    def display_color(self):
        print(f"THe shape is {self.color}")


class Rectangle(Shape):
    def __init__(self,color,width,height):
        super(). __init__(color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height

    def display_color_and_area(self):
        super().display_color()
        area = self.calculate_area()
        print(f"The area of the rectangle is : {area}")

rectangle = Rectangle("REd",8,6)
rectangle.display_color_and_area()

##Multi-level Inheritance

'''class A:
    def showdisplayA(self):
        print("This is class A")

class B(A):
    def showdisplayB(self):
        print("This is class B")

class C(B):
    def showdisplayC(self):
        print("This is class C")

obj = C()
(obj.showdisplayA())
(obj.showdisplayC())
(obj.showdisplayB())'''

##Multiple inheritance
'''class A:
    def showdisplayA(self):
        print("This is class A")

class B():
    def showdisplayB(self):
        print("This is class B")

class C(A,B):
    def showdisplayC(self):
        print("This is class C")

obj = C()
(obj.showdisplayA())
(obj.showdisplayC())
(obj.showdisplayB())

'''
##Even number in class
'''class A:
    def even(self,a,b):
     for i in range(a,b+1):
         if(i%2==0):
             print(i)

obj = A()
obj.even(12,28)

'''
## Prime Number
'''class B:
     a=0
     def prime(self,b):
        for i in range(1,b):
         if(b%i==0):
             self.a = +1


        if(self.a == 2):
            print("It's a prime number")
        else:
            print("It's a non-prime number")

obj = B()
obj.prime(2)
'''
## Destructor __del__

'''class A :

    def sum(self):
        a=10
        b=20
        c = 30
        print("This is constructor",c)

    def __del__(self):
        A = self.__class__.__name__
        print("Destroying",A)
obj = A()'''
#obj.sum()

##
'''class Shape:
    l = 23
    b = 25

    def area(self,l,b):
        Are = (l*b)

class Reactangle(Shape):
    def area(self):
        Are = (l*b)'''

'''class Father:
    surname = "Flatron"

    def show(self):
        print("The surname is ",self.surname)


class Son1(Father):
    def disp(self):
        print("The name is Dell",self.surname)

class Son2(Father):
    def Disp(self):
        print("The name is Lenovo",self.surname)

s1 = Son1()
s2 = Son2()
s1.disp()
s2.Disp()
s2.show()'''
#### Hierarchical Inheritance

'''class A:
    def showdisplayA(self):
        print("This is dispaly A")'''