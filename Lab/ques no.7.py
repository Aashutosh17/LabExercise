# You live 4 miles away from university.The bus drives at 25mph but spends 2 min at each of the 10
# stops on the way.How long will the bus journey take? Alternatively,you could run to university.You jog
# first mile at 7mph; then run the next two at 15mph; before jogging the last at 7mph again.
# will this be quicker or slower than the bus?
distance_of_university= 4
speed_of_bus= 25
time_to_reach_university=(distance_of_university/speed_of_bus)*60
# 2 minutes in each stop
time_spends=20
total_time = time_to_reach_university+time_spends
print(f"Total time taken  by bus is{total_time} ")

jog_one =((1/7)*60)
jog_two =((2/15)*60)
jog_three =((1/7)*60)
total_walk_time = jog_one+jog_two+jog_three
print(f"Time taken by running is {total_walk_time}")

if(total_time>total_walk_time):
    print("Taking bus is slower than running !!")
else:
    print("Taking bus is quicker than running !!")
