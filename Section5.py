print("_________________________ Regular Index")

var="Venkat"
print(var[0:3])

print("__________________________ Negative Index")

var="Hello World"
print(var[-6:-2])

print("___________________________ Slices")

str="Hello World"
s1=slice(3)
s2=slice(1,3,2)
print("Python Programming")
print(str[s1])
print(str[s2])

print("__________________________ Remove the Character  of index value")
def value(str):
    result=""
    for a in range(len(str)):
        if a%2==0:
            result=result+str[a]
        return result
print(value('string'))
print(value('python 3'))

print("_________________________ Append in Python")

list=[1,2,3,4,5,6]
print(list)
list.append(10)
print(list)

print("_________________________ String Format Method ")

var="for only in {price:2f} Dollars"
print(var.format(price=100))

print("_________________________ String Indexing and Slicing")

a="ABCDEFGHI"
print("a[-4]=%s" % a[-4])
print("a[5]=%s" % a[5])
print("a[1:3]=%s" % a[0:3])

print("________________________ Neutralize Uppercase")

def upper1(str):
    uppervar=0
    for i in str[:4]:
        if i.upper()==i:
            uppervar+=1
    if uppervar>=2:
        return str.upper()
    return str

print(upper1("Python"))
print(upper1("PyThon"))

var="ven"
print(var.capitalize())
name="code"
print(name.capitalize())

print("_________________________ Max Character")

var=max("abcxyz")
print(var)
var2=max(1,2,3,90)
print(var2)

print("_________________________ Taking Input in Python")

print("Taking a User Input:")
print("Enter Your Name:")
i=input()
print('Hello '+i)

