# this is used  in print a streat line for print
print("*"*40)
print("hello Enddrave tech innovaction")
print("*"*40)
# 
# this function used in if elif and else
def calculator(num1 ,num2,operator):
    if operator == '+':
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
         print("cant divide")
        return None
    else:
        print("invalid ")
    # this is used in get function for input
def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("invalid message")

    #  this is used in run_calculator in def function 
def run_calculator():
    num1 = get_number("Enter the number :")
    num2 = get_number("Enter the number : ") 
    
    operator = input("Enter  operator (+,-,*,/ ): ").strip()
    
    if  operator not in ["+","-","*","/"] :
        print("invalid operator")
        return
    result = calculator(num1,num2 ,operator)
    
    if result is not None:
        print("Result:", result)

    
#    this is main function # 
def main():
    while True:
        run_calculator()
        
        repeat = input("DO you want to repeat (yes/no) :").strip().lower()
            
        if repeat != "yes":
            print("\n thank you  for use")                
            break
#  this is you in init function
if __name__ == "__main__":
    main() 
                 