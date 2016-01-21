#determine grade

#get input
grade = input("Enter score:")

try:
    #check input validity
    grade = int(grade)
    #check if input is between 0 and 100
    if grade>100 or grade<0:
        print ("Invalid! Score must be within 0 - 100.")
    else:
        #output
        if grade<=35:
            print ("U")
        elif grade<=44:
            print ("S")
        elif grade<=49:
            print ("E")
        elif grade<=54:
            print ("D")
        elif grade<=59:
            print ("C")
        elif grade<=69:
            print ("B")
        elif grade<=100:
            print ("A")
except ValueError:
    #error message
    print ("Invalid input")
