#write a program  to create simple calculator performing only four basic operations
#requirements
#accept two numbers from the user 
#ask user to input any operator(+-*/)
#an error message displayed if the  user enters anything eles
#display only [ositive difference in case of the opertor -]
#display message "plese enetr a value other than 0",if user enetrs second number as 0,and operator /

#program to create a four function calculator
result=0
val1=float(input("enter value 1:"))
print("value 1 is:",val1)  #no need this lines
val2=float(input("enter value2 :"))
print("value 2 is:",val2) #no need this lines 
op=input("enetr any one of the operator(+-*/):")
print("operator to calculate the given values:",op) #no need this lines 
if op=="+":
    result=val1+val2
elif op=="-":
    if val1>val2:
        result=val1-val2
    else:
        result=val2-val1
elif op=="*":
    reult=val1*val2
elif op=="/":
    if val2==0:
        print("error !division by zero  is not allowed .program terminated")
    else:
        result=val1/val2
else:
    print("wrong input program terminated ")
print("the result is ",result) 
               
        
            

