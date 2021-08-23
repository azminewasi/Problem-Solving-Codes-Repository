text=input()
number=int(input())
ans=""
if number%2==0:
    for i in range(len(text)):
        if i%2==0:
            ascii=ord(text[i])
            ans=ans+chr(ascii+1).upper()
else:
    for i in range(len(text)):
        if (i%2)!=0:
            ascii=ord(text[i])
            ans=ans+chr(ascii+1).upper()
print(ans)