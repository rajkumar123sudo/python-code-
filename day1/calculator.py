
print("hello Enddrave tech of innovaction company")

num1 = float(input("enter the num :"))

num2 = float(input("enter the num :"))

operator = input("enter the operator ( +, - , *, / ):")

if operator == "+":
    print("result", num1 + num2 )
elif operator == "-":
    print("Result" , num1 - num2)
elif operator == "*":
    print("result" , num1 * num2)
elif operator == "/":
    if num2 != 0 :
     print("result",num1 / num2)
    else:
        print("can not divide it")
        
else:    
    print("please the valid operator")
    
    