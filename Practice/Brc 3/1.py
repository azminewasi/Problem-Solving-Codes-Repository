inp=input()
data=inp.split(" ")

book={"Airtel":{},"Robi":{},"Grameenphone":{},"Others":{}}

for i in range (0,len(data),2):
    if data[i+1][0:3]=="016":
        book["Airtel"][data[i]]=data[i+1]
    elif data[i+1][0:3]=="017" or data[i+1][0:3]=="013":
        book["Grameenphone"][data[i]]=data[i+1]
    elif data[i+1][0:3]=="018":
        book["Robi"][data[i]]=data[i+1]
    else:
        book["Others"][data[i]]=data[i+1]

def sorting_1st(temp_dict1):
  return {k: v for k, v in sorted(temp_dict1.items())}

def sorting_nested(td_2):
  return {k: sorting_1st(v) for k, v in sorted(td_2.items())}


print(sorting_nested(book))