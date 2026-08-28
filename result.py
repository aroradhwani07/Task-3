#Student Result Analyser
names=[]   #list of names
marks=[]   #list of marks
std_pass=0 #counter for pass
std_fail=0 #counter for fail
n=int(input("Enter the number of students:"))

#loop to enter n number of entries
for i in range(n):
    name=input("Enter name of student:")
    mark=int(input("Enter marks of the student:"))
    names.append(name)  #append name to list named names
    marks.append(mark)  #append marks to list named marks

print("name\tmark\tgrade")
for i in range(n):      #loop for grading as per marks
    if marks[i]>=85:
        grade="A"
    elif marks[i]<85 and marks[i]>=75:
        grade="B"
    elif marks[i]<75 and marks[i]>=55:
        grade="C"
    elif marks[i]<55 and marks[i]>=45:
        grade="D"
    else:
        grade="F"
    print(names[i],"\t",marks[i],"\t",grade)
    if marks[i]>=40:
        std_pass+=1
    else:
        std_fail+=1

average = sum(marks) / n   #sum(),min(),max() are built-in functions
highest = max(marks)
lowest = min(marks)
highest_name = names[marks.index(highest)]
lowest_name = names[marks.index(lowest)]
pass_percentage=(std_pass/n)*100


print("Class Average:", average)
print("Highest scorer:", highest_name)
print("Lowest scorer:", lowest_name)
print("Number of sudents who passed:",std_pass)
print("Number of students who failed:",std_fail)
print("Pass Percentage:", pass_percentage, "%")
    
