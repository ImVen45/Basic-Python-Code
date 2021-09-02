print("____________________________ if Statement ")

#age=14
#if age<16:
 #   print("you are not Able to registor an account")

price=20
qty=15
amount=price*qty
if amount>100:
    print("15% of discount on that")
    discount=amount*15/100
    amount=amount-discount
    print("amount payble",amount)

var1=None
if True:
    var1="hi Python"
print(var1)

print("____________________________ else Statement")

#a=10
#b=15
#if b<a:
    #print("B is greater then A")
#else:
 #   print

price=15
qty=20
amount=price*qty
if amount<100:
    print("15% discount")
    discount=amount*15/100
    amount=amount-discount
    print("amount payble",amount)
else:
    print("5% discount ")
    discount=amount*5/100
    amount=amount-discount
    print("amount payble",amount)

print("_____________________________ elif Statement")

x=2
if x==1:
    print("X is 1")
elif x==4:
    print("X is 4")

elif x==5:
    print("X is 5")
else:
    print("X is something Else")

print("=============================================")

price=60
qty=10
amount=price*qty

if amount>500:
    print("15% discount is given")
    discount=amount*15/100
    amount=amount-discount
    print("this payble amount is ",amount)
elif amount>400:
    print("10 % discount id given")
    discount = amount * 10 / 100
    amount = amount - discount
    print("this payble amount is ", amount)
else:
    print("No discount Given")

print("____________________________ Nested if else Statement")

var=-10
if var>0:
    print("positive number")
else:
    print("negative number")
    if -10<=var:
        print("Two digit are negative")

print("_______________________________ For Loop")

pl="c++","java","c"
for p in pl:
    print(p)
number=0
for val in range(1,7):
    number=number+val
    print(number)

print("_______________________________ While Loop")

x=5
while(x<6):
    print(x)
    x+=1
    print(x)
total=0
num=20
while(num<=25):
    total=total+num
    num=num+1
    print("Value of the total from the while loop",total)

print("__________________________________ Break Statement")

for char in "Python3":
    if(char=="o"):
       break
    print("character:",char)

print("________________________________ Continue Statement")

for char in "Python3":
    if(char=="o"):
       continue
    print("character:",char)

print("__________________________________ Pass Statement")

for char in "Python3":
    if(char=="o"):
       pass
    print("character:",char)

print("__________________________________ Nested Loop")

for num in range(3):
    for num1 in range(5,9):
        print(num,",",num1)
print("+++++++++++++")
a=1
b=4
while a<2:
    while b<5:
        print(a,",",b)
        b=b+1
        a=a+1

print("___________________________________ loops with else block of code")

for a in range(5):
    print(5)
else:
    print("The Loop has completed execution")

t=0
n=10
while(n<=10):
    t=t+n
    n=n+1
    print("Value of the total from the while loop is",t)
else:
    print("you have value is equal to 10")

print("______________________________________ Fibonacci Series")

num=12
i=0
v1=0
v2=1
while(i<num):
    if(i<=1):
        next=i
    else:
        next=v1+v2
        v1=v2
        v2=next
    print(next)
    i=i+1

def fibonacci():
    num = int(input("How many numbers that generates?:")) #taking user input here with input function
    i = 1 # the value of i here is 1
    if num == 0: #if num == 0 which means that if number will = to 0 then 
        fib = [] #this string will be printed
    elif num == 1: #if number == 1 so that will start from 1 and so on
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1]) #fibonacci logic
            i += 1
    return fib
print(fibonacci()) #printing fibonacci funtion here
input()
        


        
