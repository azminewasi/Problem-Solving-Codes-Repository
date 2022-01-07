import math

num_of_eyedrops=input("How many drops? ")
num_of_eyedrops=int(num_of_eyedrops)

time_of_waking_up=input("Waking Up time? ")
time_of_waking_up=int(time_of_waking_up)

bed_time=input("bed_time? ")
bed_time=int(bed_time)

eye_drops_data={}

for i in range(num_of_eyedrops):
    eye_drop_name=input("Eye Drop name: ")
    eye_drop_how_many_eye_drop_giving_time_a_day=int(input("How many eye_drop_giving_time in a day? "))
    eye_drops_data[eye_drop_name]=eye_drop_how_many_eye_drop_giving_time_a_day




print("\n\n\n*****************************************")

print("The Eye drop eye_drop_giving_time are given below:")

for eye_drop in eye_drops_data:

    print (eye_drop+" :")

    calculation_of_period_time=math.floor((bed_time-time_of_waking_up)/eye_drops_data[eye_drop])
    eye_drop_giving_time=[str(time_of_waking_up)+":00"]
    starting_time=time_of_waking_up

    for i in range (eye_drops_data[eye_drop]-1):
        starting_time=starting_time+calculation_of_period_time
        eye_drop_giving_time.append(str(starting_time)+":00")

    print(', '.join([str(time) for time in eye_drop_giving_time]))

    print("==============================")
print("\n\n\n*****************************************")