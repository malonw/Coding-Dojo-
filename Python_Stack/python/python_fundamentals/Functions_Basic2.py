# 1. Countdown
startNum = int(input("Enter a starting number:"))
def countDown():
    for z in range(startNum, 0, -1):
        print(z)
countDown()

print("-----")
# 2. Print and return
num1=int(input("Enter a number:"))
num2=int(input("Enter a second number:"))
def print_and_return():
    print(num1)
    return num2
# print_and_return()
print(print_and_return())

print("-----")

# First plus length
num1=int(input("Enter a number:"))
num2=int(input("Enter a second number:"))
num3=int(input("Enter a Third number:"))
num4=int(input("Enter a Forth number:"))
num5=int(input("Enter a Fifth number:"))
array=[num1,num2,num3,num4,num5]
def firstPlus() :
    sum=array[0] + len(array)
    print("the sum of the First number plus the length is:", sum)
firstPlus()
print("-----")
# Values Greater than Second
list=[5,2,3,21,4,1]
newlist=[]
def greaterThan() :
    for x in range (len(list)):
        if list[x]>list[1] :
            newlist.append(list[x])
        elif len(list) < 2 :
            return False
            
    print("Values greather than second number:", len(newlist))
    return newlist
    
greaterThan()
print(newlist)  
# This Length, That Value
print("-----")
num1=int(input("Enter a number:"))
num2=int(input("Enter a second number:"))
arr = []

def value() :
    for x in range(num1) :
        arr.append(num2)
    print(arr)
value()