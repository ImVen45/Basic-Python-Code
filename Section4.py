def LMS():
    print("Books")
    print("Auther")
    print("Student")
    print("Staff")
LMS() # calling function

print("__________________________ Function")

def avg():
    x=3
    y=5
    print("Average of ",x,"and",y,"is",(x+y)/2)
avg() # calling function

print("_______________________ Function Arguments and Return")

def sum(n1,n2=1): # n1,n2 are parameters
    return n1+n2
s1=sum(67,80) # s1,s2,s3 are Arguments
s2=sum(11)
s3=sum(12)

print(s1)
print(s2)
print(s3)

print("_______________________ Nested Function")
 
def outerfunction():
    print("Hello i am Outer Fuction")
    def innerfunction():
        print("Hello i am  Inner Function")
    innerfunction() 
outerfunction()

print("____________________")
def num(x):
    def num1(y):
        return x*y
    return num1
result=num(20)
print(result(2))

print("_____________________ Module in Python")

import math
print("The value of tangent is:",math.tan(3))
print("The value of sine is:",math.sin(3))
