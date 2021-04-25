# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
numbers={}
for i in range(n):
    data=input()
    data=data.split()
    if len(data)==2:
        numbers[data[0]]=data[1]
    else:
        numbers[data[0]]=""
        
while (True):
    try:
        check=input()
        if check in numbers:
            print(check+"="+numbers[check])
        else:
            print("Not found")
    except:
        break
    
        
