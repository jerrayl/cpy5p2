#find greatest common divisor

#initialize variable
i=0
#get input
n1=input("Enter first number:")
n2=input("Enter second number:")
#check input validity
try:
    n1=int(n1)
    n2=int(n2)
    #check for smaller number
    if n1<n2:
        i=n1
    if n2<n1:
        i=n2
    elif n1==n2:
        print("The two numbers are equal. The greatest common divisor is",n1)

    #find gcd
    while i>0:
        if n1%i==0 and n2%i==0:
            #output
            print("The greatest common divisor is",i)
            break
        else:
            i-=1
except ValueError:
    #error message
    print ("Invalid input")

