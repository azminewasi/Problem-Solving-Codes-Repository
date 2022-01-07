"""Question: 1
A Special Number is a number when the sum of the factorial of digits is  
equal to the original number (given number). For example, 145 is a Special  
Number because 145 = 1! + 4! + 5!.

Your task is to write a Python code that takes some numbers as user input  
(separated by a comma) in a single line and groups the Special &  
Non-Special numbers in a dictionary. Note that the values corresponding to  
the keys in that dictionary must be in tuple format.

Sample Input 1:
145, 346, 2, 83221, 7999888
Sample Output 1:
{'Special': (145, 2), 'Non-Special': (346, 83221, 7999888 )}
-----------------------------------------------------------------
Sample Input 2:
1431, 69716, 353, 7969828
Sample Output 2:
{'Special': (), 'Non-Special': (1431, 69716, 353, 7969828)}"""



def factorial_maker(num):
    factorial=1; 
    if(num==0):
        return factorial
    else:
        while(num>0):
            factorial=factorial*num
            num=num-1
        return factorial

number_str=input().split(", ")
numbers=[int(x) for x in number_str]
ans={'Special':0,'Non-Special':0}

for number in numbers:

    temp_sum=0
    for i in str(number):
        temp_sum=temp_sum+factorial_maker(int(i))
    if temp_sum==number:
        if ans.get('Special',0)==0:
            ans['Special']=[number]
        else:
            ans.get('Special').append(number)
    else:
        if ans.get('Non-Special',0)==0:
            ans['Non-Special']=[number]
        else:
            ans.get('Non-Special',0).append(number)

if ans['Special']==0:
    ans['Special']=()

if ans['Non-Special']==0:
    ans['Non-Special']=()

ans['Special']=tuple(ans['Special'])
ans['Non-Special']=tuple(ans['Non-Special'])
print(ans)