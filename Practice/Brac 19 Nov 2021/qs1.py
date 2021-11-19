"""𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 1:
Write a Python program that takes an integer input as height from the user  
and then print the pattern like the samples below. You can assume that the  
user will always enter the number between 1 to 9.
--------------------------------------------------------------------------
Sample Input 1:
4
Sample Output 1:
4321
+321
**21
+++1

--------------------------------------------------------------------------
Sample Input 2:
6
Sample Output 2:
654321
+54321
**4321
+++321
****21
+++++1

--------------------------------------------------------------------------
Sample Input 3:
9
Sample Output 3:
987654321
*87654321
++7654321
***654321
++++54321
*****4321
++++++321
*******21
++++++++1

Explanation/Hint:
Using the given height, try to find the pattern where the numbers are  
printed. Also, you have to find out the conditions to print the special  
symbols ('+' and '*') in a line. After applying the conditions in your  
code, you are expected to see the given outputs."""

num=int(input())
line=''.join([str(x) for x in range(num,0,-1)])
print(line)
for i in range(num-1):
    if int(line[i])%2==0:
        line_to_print='+'*(i+1)+line[i+1:]
        print(line_to_print)
    else:
        line_to_print='*'*(i+1)+line[i+1:]
        print(line_to_print)
    
