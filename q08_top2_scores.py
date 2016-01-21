#top 2 scores

#initialize variables
names=[]
scores=[]

#get input
number_of_students = input("Enter number of students:")                           
try:
    number_of_students=int(number_of_students)
    for i in range(number_of_students):
        names.append(input("Enter student " +str(i+1)+ " name:"))
        scores.append(float(input("Enter student "+str(i+1)+ " score:")))
except ValueError:
    #error message
    print("Invalid input")

#find top two scores
first=sorted(scores)[-1]
second=sorted(scores)[-2]
#find index of scores
first=scores.index(first)
second=scores.index(second)
#output
print ("Highest scorer is",names[first],"with a score of",scores[first])
print ("Second-highest scorer is",names[second],"with a score of",scores[second])
