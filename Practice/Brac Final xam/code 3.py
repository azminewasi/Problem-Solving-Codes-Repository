def printH(n):
    if n%2==0:
        for i in range (n):
            x=[]
            x.append((n/2)-1)
            x.append((n/2))
            if i in x:
                print('*'*7)
            else:
                print("**   **")

    else:
        for i in range (n):
            if i==((n+1)/2)-1:
                print('*'*7)
            else:
                print("**   **")


printH(6)