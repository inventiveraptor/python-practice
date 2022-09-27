#!/usr/bin/env python3
# 20% of caffeine lost per hour
# initial arguments
start_time = input("When did you drink your 1st cup of coffee? (please use 24hr format) ")
start_time = int(start_time)
caffeine_start = input("How many mg of caffeine is in each cup of coffee? ")
caffeine_start = int(caffeine_start)
current_time = input("What time is is now? (please use 24hr format) ")
current_time = int(current_time)

# initial calculation
hours = (current_time - start_time) / 100

# caffeine calculation 
i = 0
caffeine = caffeine_start
while i <= hours:
    print("caffeine levels at hour ",str(start_time + i*100),": ",caffeine,"mg")
    caffeine = 0.8 * caffeine
    i += 1


# how many hours until there is less than half of the caffeine left in the body
t = 0
caffeine = caffeine_start
while caffeine >= caffeine_start/2:
    caffeine = 0.8 * caffeine
    t += 1
print("Time until less than half caffeine left in system is ",t*100+start_time)


# amount of caffeine left in the body after 8 hours
l = 0
caffeine = caffeine_start
while l < 8:
    caffeine = 0.8 * caffeine
    l += 1
print("After eight hours, there will be ",caffeine,"mg of caffeine in your system.")

# assuming you start coffee at 8am and drink another cup of coffee at the end of each hour until 6pm, how much caffeine will be in your system at the ten hour mark (6pm)?
m = 0
start_time = 800
caffeine = caffeine_start
while m <= 10:
    print(caffeine,"mg caffeine at hour ",m*100+start_time)
    caffeine = 0.8 * caffeine + caffeine_start
    m += 1
