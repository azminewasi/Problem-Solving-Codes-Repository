inp=input()
inp=inp.split(",")
vowels="aeiou"
cons="qwrtypsdfghjklmnbvczx"
solution=dict()
for i in range (len(inp)):
    line=inp[i]
    v,c=0,0
    for letter in line:
        if letter in vowels:
            v=v+1
        elif letter in cons:
            c=c+1
    solution[i+1]=(v,c)

print(solution)