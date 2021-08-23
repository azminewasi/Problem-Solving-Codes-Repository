n=input()
ans=dict()
a1=[]
a2=[]
a3=[]
for i in range(int(n)):
    temp=input()
    if temp[2]=='1':
        a1.append(temp)
    elif temp[2]=='3':
        a3.append(temp)
    elif temp[2]=='2':
        a2.append(temp)

all=[]
all.append("Spring")
all.append(a1)
all.append("Summer")
all.append(a3)
all.append("Fall")
all.append(a2)
ans={all[i]: all[i + 1] for i in range(0, len(all), 2)}
ans = {i:j for i,j in ans.items() if j != []}
print(ans)

