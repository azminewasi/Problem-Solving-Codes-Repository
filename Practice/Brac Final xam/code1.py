inp=input()
numbers_in_str=inp.split(",")

numbers= [int(i) for i in numbers_in_str]
seats=0

for number in numbers:
    if number<=100:
        seats=seats+1
    elif number>100 and number<150:
        seats=seats+2

print(str(seats)+" seats")