#find the sum of all positive numbers enterd by the user  till the user enters a negative  number
entry=0
sum1=0
print("enter numbers to find their sum ,negative number ends the loop:")
while True:
    entry=int(input())
    print(entry,end=" ")
    if entry <0:
        break
    sum1+=entry
print("sum=",sum1)
