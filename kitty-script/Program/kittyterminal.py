#my imported librarys
from ensurepip import version
import math
import time
import random
import json

#these define functions
def say():
    a53ff64efd169c1b4d085d6e7075c8d7 = input("what do you wan't to say?\n:")
    print(a53ff64efd169c1b4d085d6e7075c8d7)

def addnum():
    # Store input numbers
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

# Add two numbers
    sum = float(num1) + float(num2)

# Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


def Divide():
    a = int(input("first number\n:"))
    b = int(input("second number\n:"))
    print(a / b)

def genaratenumber():
    x = random.randint(1,9999999999)

    print(x)

def helpme():
    print("""1. use the say command to print to the console

    2.use the add num command to add numbers and use the divide() command to devide numbers

    3. use the store() command to store a variable and use the outputstore1() command to output the variable 

    4. use the genaratenumber() command to genarate a random number""")


print("For help you can type helpme()")

terminal_input = input(">>>")



if terminal_input == "say()":
    say()



if terminal_input == "addnum()":
    addnum()


if terminal_input == "store()":
    vastr1 = input("store>>>")
    


if terminal_input == "Divide()":
    Divide()

    
if terminal_input == "genaratenumber()":
    genaratenumber()

if terminal_input == "helpme()":
    helpme()

if terminal_input == "outputstore1()":
    print(vastr1)

if terminal_input == "writefile()":
    zy = input("what to write inside file?\n:")
    gore = input("what to name file?\n:")
    fp = open(gore + '.txt', 'w')
    fp.write(zy)
    fp.close()

if terminal_input == "file.read()":
    file_name = input("file name?\n:")
    f = open(file_name, 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

if terminal_input == "version()":
    print("1.2.1")


