sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}


# while prompt != 'EXIT':
#     prompt = input('Enter a word in English or EXIT: ')
#     if prompt in sample_dict:
#         print('Translation: ',sample_dict[prompt])
#     elif prompt not in sample_dict:
#         print('No match!')
#     elif prompt == 'EXIT':
#         print('Bye!')

while True:
    prompt = input('Enter a word in English or EXIT: ')
    if prompt == 'EXIT':
        print('Bye')
        break
    elif prompt in sample_dict:
        print('Translation: ',sample_dict[prompt])
    elif prompt not in sample_dict:
        print('No match!')
        
        
#Answer I received is below

# while True:
#     user_input = input('Enter a word in English or EXIT: ')
#     if user_input == 'EXIT':
#         break
#     if user_input in sample_dict:
#         print ('Translation:', sample_dict[user_input])
#     else:
#         print('No match!')
 
# print('Bye!')