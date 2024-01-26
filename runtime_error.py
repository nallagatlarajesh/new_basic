#example of a program which generates runtime error 
#runtime error example
num1=10
num2=int(input("num2="))
#if user inputs a string  or a zero ,it leadss leads to runtime error
print(num1/num2)


#if we enter 0 the error will be showing like this

 # ZeroDivisionError                         Traceback (most recent call last)
#Cell In [25], line 6
#        4 num2=int(input("num2="))
#       5 #if user inputs a string  or a zero ,it leadss leads to runtime error
# ----> 6 print(num1/num2)
# 
# ZeroDivisionError: division by zero
