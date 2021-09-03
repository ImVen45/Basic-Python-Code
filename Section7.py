print("___________________________ Handling Exception")

try:
    text=input("Enter a value:")
except EOFError:                           # Ctrl+D or Ctrl+Z
    print("EOF Error")
except KeyboardInterrupt:                  # Ctrl+C
    print("You Cancelled the Operation")
else:
    print("You Entered".format(text))

print("____________________________ Raising Exceptions")

a=123   # a="Python"
if not type(a) is int:
    raise TypeError("Please Enter only Interger No.")

a=1  # a="Python" a=-1
if a<0:
    raise Exception("Please enter integer number")

print("____________________________ try except finally")

#b=15
try:
    print(b)
except:
    print("Something is wrong, b is not Declared")
finally:
    print("try Except is Finished right here")

try:
    c=open("Section1.py")
finally:
    c.close()

print("_____________________________ Breaking Math Operation & Use ZeroDivisionError")

def divide():
    while True:
        try:
            x=int(input("Enter the Numerator:"))
            y=int(input("Enter the DeNumerator:"))
            print(x/y)
        except:
            print("Please Enter a valid integer or DeNumerator")
divide()



