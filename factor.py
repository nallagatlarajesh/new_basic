#program to find the factores of a whole numbers using while loop
#find the factors of a number using while loop
num=int (input("enter the number to find the factores :"))
print(1,end=" ")  #1 is a factor of every number
factor=2
while factor<=num/2:
    if num%factor ==0:
        print(factor,end=" ")
    factor+=1
print(num,end=" ")  #every number is a factor of its self
