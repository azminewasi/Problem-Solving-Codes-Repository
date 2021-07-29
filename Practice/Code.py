inp=input()

digits="0123456789"
letters_list=[]
digits_list=[]
for letter in inp:
    if letter in digits:
        digits_list.append(letter)
    else:
        letters_list.append(letter)

if len (digits_list)==0:
    print("There is no digit in the string")
elif len(letters_list)==0:
    print("There is no alphabet in the string")
else:
    digits_list.sort()
    print(digits_list)
    sum= sum(int(x) for x in digits_list)
    print(sum)
