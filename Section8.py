print("______________________ Class and Objects")

class car: # creating class
    model=2020
    name="BMW"
c=car()    #creating object
print(c.model,c.name)

print("______________________ Python Constructor")

class Constructor_Example:

	# default constructor
	def __init__(self):
		self.name = "Mars"

	# a method for printing data members
	def print_name(self):
		print(self.name)


# creating object of the class
obj = Constructor_Example()

# calling the instance method using the object obj
obj.print_name()

print("_______________________ Initializing the Objects")

class car:
    def __init__(self,name,model):
        self.name=name
        self.model=model
c=car("Ford",2020)
print(c.name,c.model)

print("_________________________ Run a Simple Empty Class Example")

class car:
    pass
c=car()
c.name="Ford"
c.model=2020
c.color="White"
print(c.model,c.name,c.color)

print("__________________________ Instance Method with Classes and Objects")

class car:
    """ This is a instance method """
    model=2020
    def cartype(self):
        print("Sports Car")
c=car()
print(c.model)
c.cartype()
print(car.__doc__)

print("____________________________ Object Methods")

class car:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def cardetails(self):
        print("Name of Car:",self.name)
        print("Color of Car:",self.color)
c=car("Ford","Orange")
c.cardetails()

print("____________________________ Self Parameter")

class car:
    def __init__(selfcar,name,color): # Selfcar is a Self Parameter
        selfcar.name=name
        selfcar.color=color
    def car_details(selfcar):
        print("Name of Car:",selfcar.name)
        print("Color of Car:",selfcar.color)
c=car("BMW","Black")
c.car_details()

print("_____________________________ Delete Object Property")

class car:
    def __init__(self,name,color,model):
        self.name=name
        self.color=color
        self.model=model
c=car("Ford","Orange",2020)
c2=car("BMW","Black",2019)
print(c.name,c.color,c.model)
print(c2.name,c2.color,c2.model)
del c2.name # to delete a attribute of a Object
print(c2)
print(c2.color,c2.model)
del c2  # to delete Whole Object

print("____________________________ Accessing Class Attributes from Instances")

class car: 
    model=2020
    name="BMW"
    color="Black"
    def display(self):
        print(self.name)
        print(self.color)
        print(self.model)
c=car()
print(getattr(c,"name"))
print(hasattr(c,"name"))
print(setattr(c,"model",2015))
print(c.model)
print(getattr(c,"color"))
print(delattr(c,"model"))
print(c.name,c.model,c.color)

print("___________________________ Inheritance")

class parent: #Creating Parent Class
    parentname=" "
    chlidname=" "
    def show_parent(self):
        print(self.parentname)
# This is Child Class which is inherites from parent
class child(parent):
    def show_child(self):
        print(self.childname)
#This Object of Child Class
c=child()
c.parentname="Disney"
c.childname="Marvel"
c.show_parent()
c.show_child()

print("________________________ Multiple Child Classes Inheritances")

class parent: 
    parentname=" "
    chlidname=" "
    def show_parent(self):
        print(self.parentname)

class son(parent):
    def show_child(self):
        print(self.childname)

class daughter(parent):
    def show_child(self):
        print(self.childname)

s=son()
s.parentname="bob"
s.childname="Dravid"
s.show_parent()
s.show_child()
d=daughter()
d.parentname="bob"
d.childname="siri"
d.show_parent()
d.show_child()

print("___________________________ Multi-Level Inheritances")

class family: 
    def showfamily(self):
        print("This is Family of 2 People")

class father(family):
    def fathername(self):
        print("Father Name is BOB")

class son(father):
    def sonname(self):
        print("Son Name is POP")
f=son()
f.showfamily()
f.fathername()
f.sonname()

print("_____________________________ Multiple Inheritances")

class father: 
    def Driving(self):
        print("Father Enjoys Driving")

class mother:
    def Cooking(self):
        print("Mother Enjoys Cooking")

class son(father,mother):
    def Playing(self):
        print("Son Enjoys Playing")
c=son()
c.Driving()
c.Cooking()
c.Playing()

print("___________________________ Method Over-riding")

class car():
    def __init__(self):
        self.name="BMW"
    def show_detail(self):
        print(self.name)
class BMW(car):
    def __init__(self):
        self.name="This is BMW Name"
    def show_detail(self):
        print(self.name)
c=car()
c.show_detail()
c1=BMW()
c1.show_detail()

print("__________________________ Polymorphism")

class animal:
    def noise(self):
        raise NotImplementedError
class cat(animal):
    def noise(self):
        print("Meow")
class dog(animal):
    def noise(self):
        print("woof")
a=cat()
a.noise()
a=dog()
a.noise()

print("___________________________ Data Abstraction")

from abc import ABC,abstractmethod 
class payment(ABC):                       # Abstract class
    def printslip(self,amount):
        print("Purchase Amount is:",amount)
    def payment(self,amount):              # Abstract Method
        pass
class cardpayment(payment):
    def payment(self,amount):
        print("Credit Card Payment of:",amount)
class walletpayment(payment):
    def payment(self,amount):
        print("wallet Payment of:",amount)
c=cardpayment()
c.payment(200)
c.printslip(200)
print(isinstance(c,payment))
c=walletpayment()
c.payment(300)
c.printslip(300)
print(isinstance(c,payment))

print("_________________________ Setters and Getters")

class employee:
    def __init__(self):
        self.job="None"
    def getjob(self):
        return self.job
    def setjob(self,job):
        self.job=job
bob=employee()
pop=employee()
bob.setjob("Developer")
pop.setjob("Tester")
print(bob.job)
print(pop.job)

print("__________________________ Super Class")

class A:
    def method(self):
        print("I am Calling Parent Class")
class B(A):
    def method(self):
        print("Calling the Child Class")
        super().method()
c=B()
c.method()

print("_________________________ Python Encapsulation")

class number():
    a=5
    _b=10
    __c=40
    def set_data(self,p):
       self.__c=p
    def get_data(self):
      return self.__c
n=number()
n.set_data(30)
print(n.a)
print(n._b)
print(n.get_data())
print(n.__c)