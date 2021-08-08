# Q1
inp=input()
number=int(inp)
for r in range (number):
    i=r+1
    print("=== Iteration "+str(i)+" ===")
    if i%2==0:
        for j in range (1,i+1,1):
            print('X'*j)


    else:
        for j in range (i):
            print(''.join([str(int) for int in range(i+1)])[1:])