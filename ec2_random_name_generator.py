
import random
import string

#EC2 instance name will have 4 random alphabetical characters and 4 random numbers
instance_number =int(input('How many instances do you need?\n'))
dept_name = (str(input('What department is this instance(s) for?\n'))).lower()

if dept_name.lower() == 'marketing' or dept_name == 'accounting' or dept_name == 'finops':
    #Use a for loop to create names based on how many instances were specified
    for num in range (instance_number):
        chosen_chars = ''
        i = 0
        
        #Using a while loop to pick 4 letters and 4 digits
        while i < 4:
            chosen_chars += random.choice(string.digits)
            chosen_chars += random.choice(string.ascii_letters)
            i +=1
        #Use the f string to include the department name before the chosen characters
        print(f'{dept_name}-{chosen_chars}')
else:
    print('You have entered in an Invalid Department. Only the Marketing, Accounting and FinOps departments should use this tool.')


