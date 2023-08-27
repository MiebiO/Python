while True:
    name = input('Enter your name or EXIT to close the program: ')
    if (name == 'EXIT'):
        break
    print('Hello', name)
    
for number in range (1,21):
    if number % 5 == 0:
        continue
    print(number)
    
