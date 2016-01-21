#check even

#get input
number = input("Please enter a number:")

try:
    #check input validity
    number = int(number)
    #check if number is odd or even
    if number%2==0:
        #output
        print (number, " is even")
    else:
    #output
        print (number, " is odd")
except ValueError:
    #error message
    print ("Invalid input")
