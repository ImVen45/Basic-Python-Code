print("________________________ Arithmetic Operators")

print (10//3)
print (5+3)
print (10*3)
print (22*2)
print (23/5)
print (20/2)

print("_________________________ Assignment Operator")

a=10
a=a+1
print(a)
a+=1
print(a)
b=10
c=0
c=b
print(b)
c=b=a
print(c)

a=68
b=80
a-=1
print(a)
c=a+b
print(c)

print("_________________________ Short Hand of Operatot")

var=2
var+=10
print(var)
var-=10
print(var)
var*=10
print(var)
var/=10
print(var)
var%=10
print(var)

print("__________________________ Comparsion Operator")

print(2==2)
print(2==3)
print(2!=3)
print(2!=2)
print(2>3)
print(2>=3)
print(2<3)
print(2<=3)

print("__________________________ Assignment")
a=20
b=20
c=40
print(a==b)
print(a!=b)
print(c>a)
print(c<a)
print(c<=40)
print(a>=40)

print("_____________________________ Equal/Not Equal Operator")

rest="Clean"
count=5
is_clean=rest=="Clean"
is_count=count==6
is_not_clean=rest!="Clean"
print(is_clean)
print(is_count)
print(is_not_clean)
print(4!=5)
print(4==5)

print("_____________________________ Logical Operators")

a=True
b=False
print("a and b",a and b)
print("a or b",a or b)
print("a not",not a)

print("_____________________________ IS and ISNOT in Python")

var=None
car="BMW"

is_none=var is None
is_not_none=car is not "White"



print("______________________________ Inverting Boolean in Python")

v=False
print(v is False)
print(not v)
v1=True
v=not v1
print(v)

print("_______________________________ Bitwise Operator")

print(4&5)
print(4|5)
print(~4)
print(4^6)

a=10
b=9
c=0
c=a&b
print("This and Bitwise operator",c)
c=a|b
print("This is Or bitwise operator",c)

c=a<<2;
print(c)
c=a>>2;
print(c)