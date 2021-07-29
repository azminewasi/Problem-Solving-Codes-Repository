inp=input()
words=inp.split()
reversed=[]
for word in words:
    reversed.append(word[::-1])
print(words)
print(" ".join(reversed))