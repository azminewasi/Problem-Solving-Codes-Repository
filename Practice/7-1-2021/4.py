"""Question: 1
Your inputs should be the number of eye drop medicines, usual  waking up 
time of the patient in a day in 24-hour format, usual bedtime in 24-hour 
format, name of the eye drops and how many times you should apply it in a 
day. Assume the number inputs to be always in integers.

Your output should print the times at which the eye drops are to be 
administered exactly as shown in the sample output. The times should be in 
a 24-hour format. See the sample input and output below to understand how 
to take your inputs and how to print your output.

Sample Input 1:
How many drops? 2
Waking Up time? 8
Bedtime? 23
Eye Drop name: Neopred
How many times in a day? 6
Eye Drop name: Besibac
How many times in a day? 3

Sample Output 1:
*****************************************
The Eye drop times are given below:
Neopred :
8:00, 10:00, 12:00, 14:00, 16:00, 18:00
==============================
Besibac :
8:00, 13:00, 18:00
==============================

Sample Input 2:
How many drops? 2
Waking Up time? 8
Bedtime? 23
Eye Drop name: Freshfil
How many times in a day? 4
Eye Drop name: NCL
How many times in a day? 6

Sample Output 2:
*****************************************
The Eye drop times are given below:
Freshfil :
8:00, 11:00, 14:00, 17:00
==============================
NCL :
8:00, 10:00, 12:00, 14:00, 16:00, 18:00
==============================


Question: 2
Implement the design of the BFC and Customer classes so that the following 
code generates the output below:

print(f"It's been a wonderful day! \nToday, we have already served 
{BFC.order_id} customers. Few more to go before we close for today.")
print("**************************************************")
outlet1 = BFC()
print("1.==========================================")
print("Chicken Menu:")
print(BFC.menu)
print("2.==========================================")
outlet1.addChicken('Regular',95,'Spicy',125)
print("3.==========================================")
print("Chicken Menu:")
print(BFC.menu)
print("4.==========================================")
c1 = Customer("Ariyan")
c1.order = "2xRegular"
outlet1.placeOrderof(c1)
print("5.==========================================")
c2 = Customer("Ayan")
c2.setOrder("2xRegular,3xSpicy")
print("6.==========================================")
outlet1.placeOrderof(c2)
print("7.==========================================")
print(c1)
print("8.==========================================")
print(c2)


OUTPUT:
It's been a wonderful day!
Today, we have already served 80 customers. Few more to go before we close 
for today.
**************************************************
1.==========================================
Chicken Menu:
{}
2.==========================================
3.==========================================
Chicken Menu:
{'Regular': 95, 'Spicy': 125}
4.==========================================
Order ID:81
Customer name:Ariyan
Order:
Burger:Regular , Quantity:2
5.==========================================
6.==========================================
Order ID:82
Customer name:Ayan
Order:
Burger:Regular , Quantity:2
Burger:Spicy , Quantity:3
7.==========================================
Bill of Ariyan is 190 taka
8.==========================================
Bill of Ayan is 565 taka

Question: 3
Implement the design of the Teacher class that inherit from Person class so 
that the following code generates the output below:

Hint: Each office room has a capacity of 2.

class Person:
     def __init__(self,name, nid):
         self.name = name
         self.nid = nid

     def info(self):
         print("Name:",self.name)
         print("NID:",self.student_id)

# Write your code here:
Teachers = []
P1 = Person("Fariha", 1357924680)
P1.info()
print("1.======================================")
T1 = Teacher("Sabur",8346349712, 3515, "Math", "Physics")
T2 = Teacher("Hamid", 8423657216, 9523,"Economics")
T3 = Teacher("Rufaidah", 3578951236, 
7236, "Math","Chemistry", "Biology", "Physics")
T4 = Teacher("Rimon", 1930667892, 4228, "Physics")
Teachers.extend([T1, T2, T3, T4])
print("2.======================================")
for i in range(len(Teachers)):
     Teachers[i].info()
     print(f"{i+3}.======================================")
print("Number of Teachers:", Teacher.teachers)

OUTPUT:
Name: Fariha
NID: 1357924680
1.======================================
2.======================================
Teacher's Details:
Name: Sabur
NID: 8346349712
Employee_ID: 3515
Subjects: Math, Physics
Sabur will sit in office room no. 1.
3.======================================
Teacher's Details:
Name: Hamid
NID: 8423657216
Employes_ID: 9523
Courses: Economics
Hamid will sit in office room no. 1.
4.======================================
Teacher's Details:
Name: Rufaidah
NID: 3578951236
Employee_ID: 7236
Subjects: Math, Chemistry, Biology, Physics
Rufaidah will sit in office room no. 2.
5.======================================
Teacher's Details:
Name: Rimon
NID: 1930667892
Employee_ID: 4228
Subjects: Physics
Rimon will sit in office room no. 2..
6.======================================
Number of Teachers who joined: 4"""


"""How many drops? 2
Waking Up time? 8
Bedtime? 23
Eye Drop name: Neopred
How many times in a day? 6
Eye Drop name: Besibac
How many times in a day? 3"""

from math import floor

numOfDrops=int(input("How many drops? "))
WakeTime=int(input("Waking Up time? "))
BedTime=int(input("Bedtime? "))
medicines={}
for i in range(numOfDrops):
    medName=input("Eye Drop name: ")
    medTime=int(input("How many times in a day? "))
    medicines[medName]=medTime

print("*****************************************")
print("The Eye drop times are given below:")

for med in medicines:
    print (med+" :")
    temp=floor((BedTime-WakeTime)/medicines[med])
    times=[str(WakeTime)+":00"]
    time=WakeTime
    for i in range (medicines[med]-1):
        time=time+temp
        times.append(str(time)+":00")
    print(', '.join([str(x) for x in times]))
    print("==============================")




"""Neopred :
8:00, 10:00, 12:00, 14:00, 16:00, 18:00
==============================
Besibac :
8:00, 13:00, 18:00
=============================="""