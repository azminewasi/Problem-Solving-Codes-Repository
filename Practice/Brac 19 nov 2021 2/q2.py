"""𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 1:
Question 1(List,Tuple,Dictionary,String,Function)
Suppose, you are working at Bangladesh Road Transportation Authority 
(BRTA). You have to create a report which will show the number of different 
vehicles registered in different cities from the captured images of the 
number plates.

vehicle_chart = {'KA': 'Private Car', 'KHA': 'Private Car', 'GA': 'Private 
Car', 'GHA':'Jeep', 'CH':'Microbus','CHA':'Laguna','JA':'Minibus','JHA':'Big 
bus','TA':'Big truck','THA':'Pick-up','DO':'Medium 
Truck','NO':'Pick-up','PO':'Taxi-cab','VO':'Private 
Car', 'MO':'Pick-up','DA':'CNG','TH':'CNG', 'HA':'Motorbike','LA':'Motorbike','E':'Truck','ZO':'PM 
Office Vehicles'}

Input Example: DHAKA METRO- CHA 67-1234
Given input will strictly follow this format and must contain a Bangla 
alphabet from the above chart. (here, CHA)

Task: Now, write a python program which takes the vehicle’s number plate 
data and prints the registered vehicles in the expected output format.
Here, the first line of input contains the number of vehicle data followed 
by vehicle number plate data which will be provided by the user.

Sample Input 1
4
DHAKA METRO- CHA 12-1289
DHAKA METRO- KA 67-1281
DHAKA METRO- KHA 54-1112
DHAKA METRO- NO 10-1092

Expected Output 1
Registered vehicles:
{'Laguna': [1, ['12-1289']], 'Private Car': [2, 
['67-1281', '54-1112']], 'Pick-up': [1, ['10-1092']]}

Output explanation:
Output will be a dictionary with the number of vehicles in the same 
category and their vehicle number.

Sample Input 2
5
CHATTA METRO- CHA 98-1209
DHAKA METRO- CHA 11-1211
KHULNA METRO- CHA 13-1098
CHATTA METRO- KHA 21-1222
DHAKA METRO- DO 98-1209

Expected Output 2
Registered vehicles:
{'Laguna': [3, ['98-1209', '11-1211', '13-1098']], 'Private Car': [1, 
['21-1222']], 'Medium Truck': [1, ['98-1209']]}
"""

vehicle_chart = {'KA': 'Private Car', 'KHA': 'Private Car', 'GA': 'Private Car', 'GHA':'Jeep', 'CH':'Microbus','CHA':'Laguna','JA':'Minibus','JHA':'Big bus','TA':'Big truck','THA':'Pick-up','DO':'Medium Truck','NO':'Pick-up','PO':'Taxi-cab','VO':'Private Car', 'MO':'Pick-up','DA':'CNG','TH':'CNG', 'HA':'Motorbike','LA':'Motorbike','E':'Truck','ZO':'PM Office Vehicles'}
ans=dict()
num=int(input())
for i in range(num):
    car_number=input()
    details=car_number.split()

    type_of_car_n=details[2]
    number=details[3]
    type_of_car=vehicle_chart[type_of_car_n]

    data_2 = ans.get(type_of_car, "0")
    if data_2 == "0":
        ans[type_of_car]=[number]
    else:
        data_2.append(number)
        ans[type_of_car]=data_2

for i,j in ans.items():
    ans[i]=[len(j),j]
print(ans)