#making a simple calculator
a = int(input("enter 1st number = "))
operator = input ("Enter operator (+, -, *, /): ") 
b =  int(input("enter 2nd number = "))

if operator == "+" :
    print("RESULT" , a + b)

elif operator == "-" :
    print("RESULT" ,a - b) 

elif operator == "*" :
    print("RESULT" ,a * b) 

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
 
else :
    print("invalid")