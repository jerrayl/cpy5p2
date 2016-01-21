# find factors

#initialize variables
i=2
factors=""
#get input
number = input("Enter a number:")
#calculate factors and add to string
try:
    number=int(number)
    while i<number:
        if number%i==0:
            factors+=str(i)
            factors+=","
            number=(number/i)
        else:
            i+=1
    number=int(number)
    factors+=str(number)
    #output
    print (factors)
except ValueError:
    #error message
    print("Invalid input")
