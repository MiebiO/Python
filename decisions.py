import random

#Use random.randint(0,10) to generate a random integer between 0 and 10 including 10 and save that to variable called "number"
number = random.randint(0,10)

if number>6:
    print('Big Number')
    
elif number <6:
    print('Small Number')

print(number)