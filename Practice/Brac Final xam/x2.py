given_data = [["Alice", ["A"]], ["Sam", [ "A", "E", "B"]]]

grade_points={"A":5,"B":4, "C":3, "D":2, "E":0}

results={}

for student in given_data:
    name=student[0]
    grades=student[1]
    if len(grades)<2:
        print(name+": You must have at least 2 subjects in A level.")
    elif grades.count("A")+grades.count("B")+grades.count("C")+grades.count("D")<2:
        print("Sorry "+name+" the grades allowed in your top 2 grades are only A/B/C/D")
    else:
        temp_grades=[]
        for grade in grades:
            temp_grades.append(grade_points[grade])
            temp_grades.sort(reverse=True)
        GPA= (temp_grades[0]+temp_grades[1])/2
        print("Based on the A level result "+name+"'s minimum GPA is "+str(GPA))
        results[name]=GPA

print(results)
