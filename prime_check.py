#program to check if the input number is prime or not
num=int(input("enter  the number to be checked"))
flag=0
if num>1:
    for i in range(2,int(num/2)):
        if num%i==0:
            flag=1  #num is not prime number
            break   #no need to check any number
    if flag==1:
        print(num,"is not a prime number")
    else:
        print(num,"is prime number")
else:
    print("enterd number is  <=1,excute again!")
