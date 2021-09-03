print("______________________ Lambda Fuction")

a=lambda b:b+1
print("Sum of ",a(50))

print("______________________ Dictionary Comprehension")

d={}
for i in range(5):
    d[i]=i**2
    print(d)

dc={i:i**2 for i in range(5)} # Dictionary Comprehension
print(dc)

print("_____________________ Map in Python")

def abc(a):
    return len(a)
b=map(abc,("PHP","Python","java"))
print(b)
print(list(b))

print("_____________________ Filter in Python")

def abc(a):
    if a>5:
        return a 
c=filter(abc,(1,2,3,4,9))
print(list(c))

print("_____________________ Reduce in Python")

from functools import reduce 
def sum(a,b):
    return a+b 
print(reduce(sum,[2,5,6,4]))

print("______________________ Iterator in Python")

iterable="Python Iterator Program"
iterable_obj=iter(iterable)
while True:
    try:
        item=next(iterable_obj)
        print(item)
    except StopIteration:
        break

