"""𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻:
Write a python program that operates in the following way-
- The program asks the user to input an integer, X that is greater than 1. 
- The program will print “Invalid Input” if the user inputs otherwise.
- The program asks for X number of positive integers where each number has the length of X.
- The program then calculates and prints the summation of every first digit and every last digit of all the numbers.

[You can not use String concept/String indexing to solve the task]

Sample input 1:
3
015
906
222

Sample output 1:
Summation of every first digit: 11
Summation of every last digit: 13

Explanation 1:
The program asks the user to input an integer that is greater than 1.
The user enters 3.
Then the program asks the user to input 3 numbers where each number has 3 digits.
The user enters 015, 906 and 222 respectively.
The program then calculates the summation of every first digit,  (0+9+2 = 11) and every last digit, (5+6+2 = 13) of all the numbers. 
Finally, the program prints:
“Summation of every first digit: 11”
“Summation of every last digit: 13” 

====================================================

Sample input 2:
5
15468
65668
12762
16873
01357

Sample output 2:
“Summation of every first digit: 9”
“Summation of every last digit: 28”

Explanation 2:
The program asks the user to input an integer that is greater than 1.
The user enters 3.
Then the program asks the user to input 3 numbers where each number has 3 digits.
The user enters 15468, 65668, 12762, 16873 and 01357 respectively.
The program then calculates the summation of every first digit,  (1+6+1+1+0 = 9) and every last digit, (8+8+2+3+7 = 28) of all the numbers. 
Finally, the program prints:
“Summation of every first digit: 9”
“Summation of every last digit: 28”

====================================================

Sample input 3:
1

Sample output 3:
Invalid Input

Explanation 3:
The program asks the user to input an integer that is greater than 1.
The user enters 1 which is an invalid input.
So, the program prints “Invalid Input”."""


x=int(input())
if x<=1:
    print("Invalid Input")
    
else:
    first=0
    last=0
    for i in range(x):
        number=input()
        first=first+int(number[0])
        last=last+int(number[-1])
        
    print("Summation of every first digit:",first)
    print("Summation of every last digit:",last)

