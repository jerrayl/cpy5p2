#greatest common divisor

#intialize variable
i=0

#get input
n1=input("Enter first number:")
n2=input("Enter second number:")


try:
    #convert to integer, check input validity
    n1=int(n1)
    n2=int(n2)
    #check for the smaller number
    if n1<n2:
        i=n1
    elif n1>=n2:
        i=n2
    #check for the greatest common divisor
    while i>0:
        if n1%i==0 and n2%i==0:
            break
        else:
            i-=1
    #output
    print("The greatest common divisor is",i)
except ValueError:
    #error message
    print("Invalid input")
