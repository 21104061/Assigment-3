#Question 1

print("Question 1")
print()

string = input("Enter A Sentence:-")  #Entered By the User
list1 = []                            
list2 = string.split()                #converts the String into a list
now = len(list2)                      #Tells the number of enteries in the list
d1 = dict()
d2 = dict()
if len(list2) == 1:                   #If there's only one word
    for i in string:                  #list with the characters
        list1.append(i) 
    for j in list1:                   #A condition with all unique keys
        if j in d1:                   #add 1 and when a key repeats itself 
            d1[j] = d1[j] + 1               
        else:
            d1 [j] = 1
    print(d1)        

else:
    for i in list2:                   #this is for multiple words
        if i in d2:
            d2[i] = d2[i] + 1 
        else:
            d2[i] = 1
    print(d2) 
    print("completed") 

print()

#Question2 

print("Question 2")
print()
Month = int(input("Enter the month:-"))          #Entered By The User


if(Month in[1,3,5,7,8,10,12]):                   #For Months with 31 Days
    Date = int(input("Enter The date:-"))
    if(1 <= Date <= 31):
        Year = int(input("Enter The Year:-"))
        if(1800 <= Year <= 2025):
            print("Date-", Date, "/", Month, "/", Year)
            if(Month == 12 and Date == 31):
                print("Next Date-", "1/1/", Year+1)
            elif(Date == 31):
                print("Next Date-", "1/", Month+1, "/", Year)
            else:
                print("Next Date-", Date+1, "/", Month, "/", Year)
        else:
            print("invalid Year")
    else:
         print("invalid Date")
elif(Month in[4,6,9,11]):                         #For months with 30 days
    Date = int(input("Enter The Date:-"))
    if(1 <= Date <= 30):
        Year = int(input("Enter the Year:-"))
        if(1800 <= Year <= 2025):
            print("Date:-", Date, "/", Month, "/", Year)
            if(Date == 30):
                print("Next Date:-", "1/", Month+1, "/", Year)
            else:
                print("Next Date:-", Date+1, "/", Month, "/", Year)
        else:
            print("invalid Year")
    else:
         print("invalid Date")
elif(Month == 2):                                    #For month with 28\29 days
    Year = int(input("Enter The year:-"))
    if(1800 <= Year <= 2025):
        Date = int(input("Enter The Date:-"))
        if(Year%4 == 0):
            if(1 <= Date <= 29):
                print("Date-", Date,"/", Month, "/", Year)
                if(Date == 29):
                    print("Next Date-", "1/", Month+1, "/", Year)
                else:
                    print("Next Date-", Date+1, "/", Month, "/", Year)              
            else:
                print("invalid Date")
        else:
            if(1 <= Date <= 28):
                print("Date-", Date, "/", Month, "/", Year)
                if(Date == 28):
                    print("Next Date-", "1/", Month+1, "/", Year)
                else:
                    print("Next Date-", Date+1, "/", Month, "/", Year)       
            else:
                print("invalid Date")     
    else:
        print("invalid Year")
else:
    print("invalid Month")
print("Completed") 

print()
#Question 3

print("Question 3")
print()

list3 = [1,2,3,4,5,6,7,8,9,10]
list_with_tuples=[]
for i in list3:
    list_with_tuples.append((i,i**2))
print(list_with_tuples)
print("Compeleted")

print()
#Question 4
print("Question 4")
print()

Grade_points = int(input("Enter A Number Between 4 And 10 Including Them:-"))
if(Grade_points == 4):
    print("Performance = Poor")
    print("Grade = D")
elif(Grade_points == 5):
    print("Performance = Below Average")
    print("Grade = C")
elif(Grade_points == 6):
    print("Performance = Average")
    print("Grade = C+")
elif(Grade_points == 7):
    print("Performance = Good")
    print("Grade = B")
elif(Grade_points == 8):
    print("Performance = Very Good")
    print("Grade = B+")
elif(Grade_points == 9):
    print("Performance = Excellent")
    print("Grade = A")
elif(Grade_points == 10):
    print("Performance = Outstanding")
    print("Grade = A+")
else:
    print("Fail")
print("Competed")

print()

#Question 5
print("Question 5")
print()

Word = "ABCDEFGHIJK"

counter = 1

while(counter<7):
    print(" "*(counter-1), Word[0:11-((counter-1)*2)])
    counter = counter+1

print("Compeleted")
print()


#Question 6
print("Question 6")
print()
student_info=dict()
Yes="y"
alistsid=[]

#6(a)
print("Oestion 6(a)")

print()
while(Yes == "y"):                                     #keep a while loop that goes for infinite times
    SID = int(input("Enter The SID (A number):-"))     #It will ask for SID 
    Name = input("Enter Your Name:-")                  #and Names repeatedly 
    student_info[SID] = Name                           #and will add them to dictonary
    Yes = input("give a letter y or n:")
    alistsid.append((SID,Name))                        #Used if statement so that it can exit the loop
print("The required dictionary--",student_info)
print("The list will be used in further parts--")
print("The required list--",alistsid)
print("Compeleted")

print()

#Question 6(b)
print("Question 6(b)")
print()

print("Previous Dictionary:-")
print(student_info)
#Exchange the key value pair and make a new dictionary and a new list.
newdict = dict()
alistname = []
for (k,v) in student_info.items():
    newdict[v] = k
    alistname.append((v,k))
print("Exchanged the key value pair but not sorted yet:-")
print(newdict)
print("The unsorted list:-")
print(alistname)
#To sort our dictionary based on names we iterated dict.items()
alistname.sort()
#sorted list
print("The sorted list:-")
print(alistname)
#sorted dictionary from sorted list
print("The sorted dictionary:-")
#To sort our dictionary based on names we iterated dict.items()
sorted_dict=dict(alistname)                                             
print(sorted_dict)
#exchange the key value pair of the sorted_dict
required_dict_name=dict()
for (k,v) in sorted_dict.items():
    required_dict_name[v]=k
print("Dictionary sorted on the basis of name:-")
print(required_dict_name)
print("Compelted")

print()

#Question 6(c)
print("Question 6(c)")
print()

#To sort the dictionary on the basis of SID
 
print("The list We have:-")
print(alistsid)
alistsid.sort()
print("Sorted List:-")
print(alistsid)
#To cover the list into Dictonary
sorted_student_SID = dict(alistsid) 
print("Sorted dictionary based on SID:-",sorted_student_SID)
print("Compeleted")

print()

#Question 6(d)
print("Question 6(d)")

