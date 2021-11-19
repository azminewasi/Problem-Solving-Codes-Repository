"""𝗤𝘂𝗲𝘀𝘁𝗶𝗼𝗻 2:
Write a Python program to extract all integer numbers (not just specific  
digits) from a string that is taken as input from the user. Add the  
extracted substrings typecast to integers into a list and calculate their  
average without using a loop.

Note: You are not allowed to use any member function from Python’s string  
class. You also have to handle the spaces.

Hint: Make use of a list to identify the digit characters.

Sample input 1:
Asc6YdgTSEW702Po SSEQwj9825Jsg at41

Sample output 1:
Numbers: [6, 702, 9825, 41]
Average: 2643.5

Explanation: Any and all characters other than digits (0-9) are considered  
to be delimiters (separators) for the numbers. Thus the “Asc” is ignored to  
extract 6 and the “YdgTSEW” is ignored to extract 702 and so on.


Sample Input 2:
ga sdv65.76 3,%41_2*_Rsf  a$#2^9{{-+==)()}7&52

Sample Output 2:
Numbers: [65, 76, 3, 41, 2, 2, 9, 7, 52]
Average: 28.555555555555557

Explanation: Symbols like . , % etc. are also considered to be delimiters  
for the numbers. Thus “ga sdv” is ignored to extract 65,“.” is ignored to  
extract 76 and “ “ is ignored to extract 3 and so on."""

inp=input()
numberbox=list()
new_number=False

for i in range (len(inp)):
    if inp[i].isdigit():
        if new_number==False:
            new_number=True
            numberbox.append(inp[i])
        else :
            numberbox[-1]=numberbox[-1]+inp[i]
    else:
        new_number=False

numberbox=[int(x) for x in numberbox]
print(numberbox)
print(sum(numberbox) / len(numberbox))


