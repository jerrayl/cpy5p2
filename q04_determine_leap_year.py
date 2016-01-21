#determine leap year

#get input
year = input("Enter year:")

try:
    #check input validity
    year = int(year)
    #output
    if year%400==0:
        print("Leap")
    elif year%4==0 and year%100!=0:
        print("Leap")
    else:
        print("Non-Leap")
except ValueError:
    #error message
    print ("Invalid input")
