#program to print the positive defference of two numbers
num1=int(input("enetr first number:"))
num2=int(input("enter second number"))
if num1>num2:
    diff=num1-num2
else:
    diff=num2-num1
print("the positive difference of ",num1,"and",num2,"is",diff)
