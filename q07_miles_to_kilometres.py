#miles to kilometers

#initialize variables
array = [0,20,25,30,35,40,45,50,55,60,65]

#print title
print ("Miles Kilometers Kilometers Miles")
#print table
for number in range(1,11):
        print ("{0:<6}{1:<8.3f}{2:>5}{3:>15.3f}".format(number,number*1.609,array[number],array[number]*(1/1.609)))
        
