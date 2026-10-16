# this print 
print("hello Enddrave tech of innovaction company")

# this is a input variable
num1 = float(input("enter the num :"))

num2 = float(input("enter the num :"))

# this is a input operator
operator = input("enter the operator ( +, - , *, / ):")


# this is if elif and else condication for calculator 
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
    
    
while input("Do you want to repeat this calculator (yes/no): ").lower() == "yes":
    
  num1 = float(input("enter the num :"))

  num2 = float(input("enter the num :"))

# this is a input operator
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