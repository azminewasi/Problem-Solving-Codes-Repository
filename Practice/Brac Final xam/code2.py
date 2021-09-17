items=[]
quantities=[]

count=1
while True:
    item=input("Please enter item "+str(count)+": ")
    if item=="Complete":
        break
    else:
        items.append(item)
        quantity=input("Please enter the quantity: ")
        quantity=int(quantity)
        quantities.append(quantity)
        count=count+1

if count==1:
    print("Nothing in the list")
else:
    print("The complete list is:")
    data=dict()
    for i in range(count-1):
        print(items[i]+" - "+str(len(items[i]))+" - "+str(len(items[i])*quantities[i]))
        data[items[i]]=[len(items[i]),(len(items[i])*quantities[i])]
    print(data)
    sum=0
    for i in range(count-1):
        sum=sum+(len(items[i])*quantities[i])
    print("Total price = "+str(sum))
    
    