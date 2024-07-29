def add(x,y):
    return x+y
def subtract(x, y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error"
    else:
        return x/y
    

def calculator():
    print("Select any operation: ")
    print("1.Addition")
    print("2.Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter the second number: "))


    if choice =="1":
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice =="2":
        print(num1,"-",num2,"=",subtract(num1,num2))    
    elif choice =="3":
        print(num1,"*",num2,"=",multiply(num1,num2))    
    elif choice =="4":
        result =divide(num1,num2)
        if isinstance(result,str):
            print(result)
        else:

            print(num1,"/",num2,"=",result)
    else:
        print("Invalid input operation")

calculator()