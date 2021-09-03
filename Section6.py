print("________________________ Python Lists")

list=[]
print(list)
list1=[1,2,3,4,5,6]
print(list1[-5])
list2=[7,8,9,"python","there"]
print(list2)

print("________________________ Change List Item value")

list=["python","c++","java","php"]
print(list)
list[1]="ruby"
print(list)

print("_________________________ Mutable List")

list=[]
list.append("python")
list.append("java")
print(list)
list.remove("python")
print(list)

print("__________________________ Check if Item exists in List")

list=["python","java","php","ruby"]
if "java" in list:
    print("yes")
else:
    print("no")

print("___________________________ Tuples") 

tuple=()
tuple2=(9,8,7,6,5,4)
tuple3=("java","php","python")
tuple4=(67,80,"java","php")
print(tuple)
print(tuple2)
print(tuple3)
print(tuple4)

print("____________________________ Access Tuple Item")

tuple=("python","php","java")
print(tuple[0])
print(tuple[1])
print(tuple[2])

print("_____________________________ Delete Tuple")

tuple=("python","php","java")
del tuple
print(tuple)

print("______________________________ Iterating List")

list=[1,2,3,4,5,6,7,8,9]
for a in list:
    print(a)

print("_______________________________ Index and Slicing on Tuples")

tuple=(1,2,3,4,5,6)
print(tuple[2:])
print(tuple[1:4])
print(tuple[1::])
print(tuple[-2])
print(tuple[::])

print("______________________________ Using List as a Stack")

stack=["ven","will","be","lose"]
stack.append("in exam")
stack.append("not life")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

print("________________________________ Using List as a Queue")

from collections import deque
queue=deque(["lose","draw","win"])
print(queue)
queue.append("india")
print(queue)
print(queue.popleft())
print(queue)

print("________________________________ Shuffle Lists") 

import random
list=["Python","PHP","Java","C++"]
print(list)
random.shuffle(list,random.random)
print(list)

print("_________________________________ Concatenation List")

list2=["India","New Zeland","USA","UK"]
list3=["Brazil","Germany"]
list4=list2+list3
print(list4)

print("_________________________________ Dictionaries in python")

'''dict={
    "car":"BMW",
    "Model":"2020"
}
print(dict) '''

abc=dict(
    car="Audi"
)
print(abc)

print("_________________________________ Updating a Dictionary")

dict={"car":"BMW","Model":"2020"}
dict1={"car":"Ford"}
print("Original Dictionary:",dict)
dict.update(dict1)
print("Dictionary after update:",dict)

print("_________________________________ Concatenate two Dictionaries")

dict={"car":"BMW","Model":"2020"}
dict1={"plane":"indigo","cycle":"hero"}
dict1.update(dict)
print(dict)
print(dict1)

print("_________________________________ Sort a Dictionary")

dict={
    "BMW":"2020",
    "ford":"2019",
    "toyota":"2018",
    "BMW":"2012",
    "honda":"2015"
    }
for key1 in sorted(dict,key=dict.get):
    print(key1,dict[key1])

print("_________________________________ Delete Dictionary Elements")

dict={
    "BMW":"2012",
    "Ford":"2014"
    }
del dict['Ford']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)

print("____________________________ Length of Dictionary")

dict={
    "BMW":"2012",
    "Ford":"2014"
    }
print(len(dict))

print("_______________________________ Key Exits in Dictionary")

dict={
    "BMW":"2012",
    "Ford":"2014"
    }
if "BMW" in dict:
    print("Yes it is avaliable")
else:
    print("no, it is not avaliable in dictionary")

print("______________________________ Introduction to Sets")

s={2,2,3,4,5,6,7}
print(s)
s1=set([2,1,3,4,5,6,9,9,9])
print(s1)
print(len(s1))
s2=set()
s2.add("a")
s2.add("b")
s2.add("c")
s2.add("c")
s2.add("c")
print(s2)
s3={"d","e","f"}
s2.update(s3)
print(s2)

print("________________________________ Convert Dictionary into Lists")

dict={
    "BMW":"2012",
    "Ford":"2014"
    }
list=[]
for a in dict:
    b=(a,dict[a])
    list.append(b)
print(list)

print("_______________________________ Using Pop Method to delete Item in Dictionary")

dict={
    "BMW":"2012",
    "Ford":"2014",
    "toyota":"2020",
    "honda":"2019"
    }
dict.pop("BMW")
del dict["Ford"]
dict.popitem()
print(dict)

print("___________________________ Nested Loop Using Lists")

list=[["python","c","php","javascript"],["c++","ruby","java"]]
for a in list:
    print(a)
    for  b in list:
        print("_____________")
        for a in b:
            print(a)