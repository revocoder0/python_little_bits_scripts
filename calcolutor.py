#!/usr/bin/python3
#programmer name RevoCoder
#date 4/7/2023




while 1:
    f_number = float(input("Enter first number : "))
    operator = input("Enter operator you want..+,-,*,/,% : ")
    s_number = float(input("Enter second number : "))

    plus = f_number + s_number
    minus = f_number - s_number
    milti = f_number * s_number
    divided = f_number / s_number
    
    if operator == '+' :
        print(plus)
    elif operator == '-' :
        print(minus)
    elif operator == '*':
        print (milti)
    elif operator == '/':
        print (divided)
    else:
        print("wrong operator : Bye")

    

    