import math
def userinput():
    num1 = int(input("Enter your first number \n"))
    num2 = int(input("Enter your second number \n"))
    m = 0
    x=input("add(+), sub(-), mul(*), div(/), factorial(!),power(^)")
    if x=="+":
        add(a,b,m)
    elif x=="":
        subtract(a,b,m)
    elif x=="*":
        multiply(a,b,m)
    elif x=="/":
        div(a,b,m):
    elif x=="":
        factorial(a,b,m)
    elif x=="":
        power(a,b,m)
    else:
        print("i didnt understand what you want to execute")
        userinput()


def add(a, b, m):
    print(a+b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(a+b)

def subtract(a, b, m):
    print(a-b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(a-b)

def multiply(a, b, m):
    print(a*b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(a*b)

def factorial(a,b,m):
    print(math.factorial(a))
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory((math.factorial(a)))

def div(a,b,m):
    print(a/b)
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(a/b)

def power(a,b,m):
    print("a^b =" a**b
    userChoice = input("would you like to add to memory?")
    if userChoice == "yes" or userChoice == "y":
        addtoMemory(a**b)


def addtoMemory(x):
    m = x
