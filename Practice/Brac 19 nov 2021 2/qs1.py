"""𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 1:
Suppose you are working as a Software Engineer in an online streaming 
service. You are given the following tuple where all the information of a 
movie is given as [Actor’sCountry MovieName Actor’sName].

my_tuple = ("UK NoTimeToDie DanielCraige", "USA MissionImpossible 
TomCruise", "USA TopGun TomCruise", "USA Troy BradPitt", "UK Skyfall 
DanielCraige", "UK TheTheoryOfEveryting EddieRedmayne", "UK FantasticBeast 
EddieRedmayne", "USA Seven BradPitt")

Your task is to write a python program that will create an ID for all the 
movies and store it in a dictionary and then print the dictionary. Your 
dictionary should be as expected output and while generating the ID ensure 
the following criteria are met. Finally print the dictionary.

For the first digit, if country is UK = 2 and USA = 1
Then, if actor is DanielCraige = 04, TomCruise = 03, BradPitt = 02 and 
EddieRedmayne = 01
Use the tuple’s index number as the last digit.

Expected Output:
{'USA': [('MissionImpossible', 1031), ('TopGun', 1032), ('Troy', 1023), 
('Seven', 1027)], 'UK': [('NoTimeToDie', 2040), ('Skyfall', 2044), 
('TheTheoryOfEveryting', 2015), ('FantasticBeast', 2016)]}

Explanation: ID of MissionImpossible is 1031. This actor is from the USA so 
the first digit is 1, as the actor is TomCruise so 2nd and 3rd digits are 
03 and last digit 1 represents that item is situated at index 1 in the 
my_tuple. You must store the movie name and movie ID in a tuple and save 
that tuple in a list as the value of the dictionary. You Must Store The ID 
as an Integer.
"""
my_tuple = ("UK NoTimeToDie DanielCraige", "USA MissionImpossible TomCruise", "USA TopGun TomCruise", "USA Troy BradPitt", "UK Skyfall DanielCraige", "UK TheTheoryOfEveryting EddieRedmayne", "UK FantasticBeast EddieRedmayne", "USA Seven BradPitt")
ans_dict={}
uk=[]
usa=[]
for i in my_tuple:
    data=i
    data=data.split()
    code=str()
    if data[0]=="UK":
        code=str(code)+"2"
    elif data[0]=="USA":
        code=str(code)+"1"

    if data[2]=="DanielCraige":
        code=str(code)+"04"
    elif data[2]=="TomCruise":
        code=str(code)+"03"
    elif data[2]=="BradPitt":
        code=str(code)+"02"
    elif data[2]=="EddieRedmayne":
        code=str(code)+"01"


    code=str(code)+str(my_tuple.index(i))
    code=int(code)


    if data[0]=="UK":
        uk.append((data[1],code))
    elif data[0]=="USA":
        usa.append((data[1],code))
    

ans_dict["USA"]=usa
ans_dict["UK"]=uk

print(ans_dict)