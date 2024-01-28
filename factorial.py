num = int(input("Enter the number:"))
fact = 1
#check if the number is negative ,positive  or zero
if num<0:
    print("sorry ,factoruial does not exist for negative numbers")
elif num==0:
    print("the factorial of 0 is 1")
else:
    
    for i in range(1, num + 1):
        fact *= i
    print("Factorial of", num, "is", fact)

