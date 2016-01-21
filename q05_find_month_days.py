#find months days

#get input
year = input("Enter year:")
month = input("Enter month:")

#initialize variable
leap=False
months_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
months=["","January","February","March","April","May","June","July","August","September","October","November","December"]
try:
    #check input validity
    year = int(year)
    month = int(month)
    if month<1 or month>12:
        print ("Month must be between 0 and 12")
    else:
        #check if year is leap year
        if year%400==0 or (year%4==0 and year%100!=0):
            leap=True
        if leap and month == 2:
            #output for Feb of leap year
            print (year,"is a leap year.","February",year,"has 29 days.")
        else:
            #output
            print (months[month],year,"has",months_days[month],"days.") 
except ValueError:
    #error message
    print ("Invalid input")
