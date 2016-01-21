#triangle

#get input
side1 = input("Please side 1:")
side2 = input("Please side 2:")
side3 = input("Please side 3:")

try:
    #check input validity
    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)
    #check if input is a triangle
    array = [side1,side2,side3]
    array.sort()
    if (array[0]+array[1])>array[2]:
        #output
        print ("Perimeter = ", sum(array))
    else:
        #error
        print ("Invalid triangle!")
except ValueError:
    #error message
    print ("Invalid input")
