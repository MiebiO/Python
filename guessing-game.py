#Guessing game to ask when Python was released. Correct answer is 1994. Two methods shown below

#Method 1
while True:
    answer = int(input('When was Python 1.0 released? '))
    if answer > 1994:
        print('It was earlier than that!')
    elif answer < 1994:
        print('It was later than that!')
    else:
        print('Correct!')
        break

#Method 2 - my attempt
# correct_guess = 1994
# user_guess = int(input('When was Python 1.0 released? '))

# while user_guess != correct_guess:
#     if user_guess < correct_guess:
#         print('It was later than that!')
#         user_guess = int(input('When was Python 1.0 released? '))
#     else:
#         print('It was earlier than that!')
#         user_guess = int(input('When was Python 1.0 released? '))
# print('Correct!')
