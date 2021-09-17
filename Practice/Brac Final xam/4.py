"""Write a Python program which will take a list of course codes from the 
user. Create a dictionary from those course codes that will hold the course 
codes level wise.

Sample Input:
CSE110 CSE111 CSE221 CSE260 CSE320 CSE340 CSE370 CSE421 CSE423
Sample Output:
{"100 Level" : ["CSE110", "CSE111"], "200 Level" : 
["CSE221", "CSE260"], "300 Level" : ["CSE320", "CSE340" , "CSE370"],  "400 
Level" : ["CSE421", "CSE423"]}"""

inp=input()
course_info=inp.split()
levels=[]
courses=[]
data={}
for code in course_info:
    if code[3]+"00 Level" in levels:
        inx=levels.index(code[3]+"00 Level")
        courses[inx].append(code)
    else:
        levels.append(code[3]+"00 Level")
        courses.append([code])

for i in range(len(levels)):
    data[levels[i]]=courses[i]

print(data)