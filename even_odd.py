#!/usr/bin/python3
#even and odd program in python

print("This script will be Even or Odd, you entered Number")
print("****************************************************")

num1 = 0

while num1 >= 0:
    num1=int(input("Enter a number : "))
    if(num1%2 == 0): 
        print(str(num1) + " is EVEN number.")
    else :
        print(str(num1) + " is ODD number.")
        
