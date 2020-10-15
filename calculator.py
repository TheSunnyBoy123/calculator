import math
m = 0

def userinput(m):
    a = input("Enter your first number \n")
    b = input("Enter your second number \n")
    if (a=="m"):
        a=m
    else:
        a= int(a)
    if(b=="m"):
        a=m
    else:
        b =int(b)

    x=input("add(+), sub(-), mul(*), div(/), factorial(!),power(^)")
    if x=="+":
        add(a,b,m)
    elif x=="-":
        subtract(a,b,m)
    elif x=="*":
        multiply(a,b,m)
    elif x=="/":
        div(a,b,m)
    elif x=="!":
        factorial(a,b,m)
    elif x=="^":
        power(a,b,m)
    else:
        print("i didnt understand what you want to execute")
        userinput()


def add(a, b, m):
    print(a+b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(int(a+b))

def subtract(a, b, m):
    print(a-b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(int(a-b))

def multiply(a, b, m):
    print(a*b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(int(a*b))

def factorial(a,b,m):
    print(math.factorial(a))
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(int(math.factorial(a)))

def div(a,b,m):
    print(a/b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(float(a/b))

def power(a,b,m):
    print("a^b =", a**b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(int(a**b))


def addtoMemory(y):
    m = y
    print(m)
    userinput(m)
userinput(m)
